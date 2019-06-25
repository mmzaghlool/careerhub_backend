from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/user/<name>', methods=['GET'])
def login(name = None):
    return name