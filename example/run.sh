cd react_app
webpack --config webpack.config.js &
cd ..

export FLASK_APP=app
export FLASK_ENV=development
flask run
