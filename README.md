# flask-webpack-js

This flask extension provides a simple interface to conveniently import webpack bundles in jinja templates with hot reloading

## Installation

This package can be installed with pip:

```
  $ pip install flask-webpack-js
```

## Usage

Importing and initializing the webpack instance is simple:

```python

from flask import Flask
from flask_webpack_js import Webpack

app = Flask(__name__)

config = {
  'WEBPACK_STATS_FILE': './webpack-stats.json',
  'WEBPACK_BUNDLE_PATH': '/static/',
}

webpack = Webpack(config=config)
webpack.init_app(app)
```

with two configuration options exposed:

- `WEBPACK_STATS_FILE` indicates the relative path of the bundle tracking file produced by the npm package [webpack-bundle-tracker](https://github.com/owais/webpack-bundle-tracker)
- `WEBPACK_BUNDLE_PATH` indicates the relative output path of webpack as set in your webpack config 

Then, in any jinja template, you can import the webpack bundle with `{% webpack 'main' %}` where 'main' is the name of the webpack entrypoint as specified in the webpack config

### Example

An example of usage can be found in this repository. To run it, clone the repository, run `npm insall` in the react_app directory and then run `sh run.sh` in the example directory. This script will generate the webpack bundles and run flask simultaneously.

### Hot Reloading

Using [webpack-dev-server](https://github.com/webpack/webpack-dev-server) in your webpack config can enable hot reloading. This is also demonstrated in the example folder with a different webpack config file
