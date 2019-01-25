import json
import time
import re

from flask import current_app
from jinja2 import nodes
from jinja2.ext import Extension


DEFAULT_CONFIG = {
    'WEBPACK_IGNORE': [re.compile(I) for I in [r'.+\.hot-update.js', r'.+\.map']],
    'WEBPACK_STATS_FILE': './webpack-stats.json',
    'WEBPACK_BUNDLE_PATH': '/static',
}


class WebpackExtension(Extension):
    # use in the template as
    tags = set(['webpack'])

    def __init__(self, environment):
        super(WebpackExtension, self).__init__(environment)

        # add the defaults to the environment
        environment.extend(fragment_cache_prefix='', fragment_cache=None)
        self.get_bundle = getattr(environment, 'get_bundle')

    # https://stackoverflow.com/questions/29370542/jinja2-extension-outputs-escaped-html-instead-of-html-tag/29378286
    def parse(self, parser):
        lineno = next(parser.stream).lineno
        args = [parser.parse_expression()]

        if parser.stream.skip_if('comma'):
            args.append(parser.parse_expression())

        node = self.call_method('_render', args, lineno=lineno)
        return nodes.CallBlock(node, [], [], [], lineno=lineno)

    def _render(self, bundle_name, *a, extension=None, attrs='', **k):
        bundle = self.get_bundle(bundle_name, extension)
        tags = []
        script = '<script type="text/javascript" src="{}" %s></script>' % attrs
        link = '<link type="text/css" href="{}" rel="stylesheet" %s/>' % attrs
        for chunk in bundle:
            if chunk['name'].endswith(('.js', '.js.gz')):
                tags.append(script.format(chunk['url']))
            elif chunk['name'].endswith(('.css', '.css.gz')):
                tags.append(link.format(chunk['url']))
        return '\n'.join(tags)


class Webpack(object):
    def __init__(self, app=None, config=None):
        self.config = {**DEFAULT_CONFIG, **(config or {})}
        self.app = app
        self.assets = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        for k, v in self.config.items():
            app.config.setdefault(k, v)

        app.jinja_env.extend(get_bundle=self.get_bundle)
        app.jinja_env.add_extension(WebpackExtension)

    def get_assets(self):
        stats = current_app.config['WEBPACK_STATS_FILE']

        # If debug (hot reloading) the refetch every time without caching
        if current_app.debug or not self.assets:
            try:
                with open(stats, encoding="utf-8") as f:
                    assets = json.load(f)
                    if assets and assets.get('status') == 'done':
                        self.assets = assets
            except IOError:
                raise IOError('Error reading {0}'.format(stats))
        return self.assets

    def get_bundle(self, bundle_name, extension):
        assets = self.get_assets()
        if current_app.debug:
            while not assets or assets.get('status') == 'compiling':
                time.sleep(0.1)
                assets = self.get_assets()

        if assets.get('status') == 'error':
            assets = {'file': '', 'error': 'Unknown Error', 'message': '', **assets}
            error = u"\n{error} in {file}\n{message}\n".format(**assets)
            raise Exception(error)
        elif assets.get('status') != 'done':
            raise Exception(
                "The stats file does not contain valid data. Make sure plugin"
                "webpack-bundle-tracker is enabled and run webpack again"
            )

        chunks = assets['chunks'].get(bundle_name, None)
        if not chunks:
            raise Exception('Cannot resolve bundle {0}.'.format(bundle_name))

        bundle_path = current_app.config['WEBPACK_BUNDLE_PATH']
        ignore = current_app.config['WEBPACK_IGNORE']

        for chunk in chunks:
            name = chunk['name']
            valid = not extension or name.endswith('.{0}'.format(extension))
            if valid and not any(regex.match(name) for regex in ignore):
                chunk['url'] = chunk.get('publicPath') or f'{bundle_path}{name}'
                yield chunk
