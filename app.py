from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello"

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/name')
def name():
    return 'Anshika'

@app.route('/age')
def age():
    return '19'
if __name__ == "__main__":
    app.run()