from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/home')
def home():
    return '<h1>Hello World!</h1>'


@app.route('/<string:name>/<int:age>')
def check(name, age):
    return f'{name} is {age}.'


if __name__ == '__main__':
    app.run(debug=True)
