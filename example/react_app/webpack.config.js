// require our dependencies
const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  entry: {
    hello: ['babel-polyfill', './index.jsx'],
  },
  output: {
    path: path.resolve('../static/'),
    filename: '[name]-[hash]-bundle.js',
    publicPath: '/static/',
  },
  devtool: 'source-map',
  module: {
    rules: [{
      test: /\.jsx?$/,
      loader: 'babel-loader',
      exclude: /node_modules/
    }]
  },
  plugins: [
    new BundleTracker({ filename: './webpack-stats.json' })
  ],
  mode: 'production'
};
