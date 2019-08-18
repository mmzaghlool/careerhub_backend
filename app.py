from flask import Flask, request

import firebase_admin
from firebase_admin import credentials, firestore, auth, db
# from "./src/auth" import auth
app = Flask(__name__)

from routes import *
app.register_blueprint(routes)
# app.register_blueprint(auth)

# Use the application default credentials
cred = credentials.Certificate('./aiet-bae93-13ecac79617e.json')
firebase_admin.initialize_app(cred, {"databaseURL": "https://aiet-bae93.firebaseio.com/"})

# db = firestore.client()

@app.route('/')
def index():
    return 'Hello, World!'

    # doc_ref = db.collection(u'users').document(name)
    # doc_ref.set({
    #     u'first': u'Ada',
    #     u'last': u'Lovelace',
    #     u'born': 1815
    # })
    return "name"

if __name__ == "__main__":
    app.run(debug=True)