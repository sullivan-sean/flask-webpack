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
  devtool: 'inline-source-map',
  devServer: {
    contentBase: false,
    publicPath: '/static/',
    hot: true,
    host: '0.0.0.0',
    port: '5000',
    inline: true,
    proxy: [{
      context: ['**', '!/static/**'],
      target: 'http://0.0.0.0:3000',
    }],
    disableHostCheck: true,
  },
  module: {
    rules: [{
      test: /\.jsx?$/,
      loader: 'babel-loader',
      exclude: /node_modules/
    }, {
      test: /\.css$/,
      use: ['style-loader', 'css-loader']
    }]
  },
  plugins: [
    new webpack.NamedModulesPlugin(),
    new webpack.HotModuleReplacementPlugin(),
    new BundleTracker({ filename: './webpack-stats.json' })
  ],
  mode: 'development'
};

