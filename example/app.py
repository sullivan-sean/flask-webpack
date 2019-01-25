import os
from flask import Flask, render_template_string
from flask_webpack_js import Webpack

app = Flask(__name__)

config = {
  'WEBPACK_STATS_FILE': './react_app/webpack-stats.json',
  'WEBPACK_BUNDLE_PATH': '/static/',
}

webpack = Webpack(config=config)
webpack.init_app(app)

@app.route('/')
def hello():
    template = """
        <body>
            <div id="root"></div>
            {% webpack "hello" %}
        </body>
    """

    return render_template_string(template)
