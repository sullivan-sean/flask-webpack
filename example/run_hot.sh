cd react_app
webpack-dev-server --config webpack-hot.config.js & disown
cd ..

export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=1
flask run --port=3000
