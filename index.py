from flask import Flask
import pyrebase

config = {
  "apiKey": "AIzaSyBv7hMsIJJ9RtaHEj7F4dDO2nsdiIUudnY",
  "authDomain": "aiet-bae93.firebaseapp.com",
  "databaseURL": "https://aiet-bae93.firebaseio.com",
  "storageBucket": "aiet-bae93.appspot.com"
}

firebase = pyrebase.initialize_app(config)

app = Flask(__name__)

# data to save
# data = {
#     "name": "Mortimer 'Morty' Smith"
# }

# Pass the user's idToken to the push method
# results = db.child("users").push(data, user['idToken'])
@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/user/<name>', methods=['GET'])
def login(name = 'None'):
    data = {
        "name": name
    }
    db.child("users").push(data)
    return name