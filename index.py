from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)

# firebaseConfig = {
#     'apiKey': "AIzaSyBv7hMsIJJ9RtaHEj7F4dDO2nsdiIUudnY",
#     'authDomain': "aiet-bae93.firebaseapp.com",
#     'databaseURL': "https://aiet-bae93.firebaseio.com",
#     'projectId': "aiet-bae93",
#     'storageBucket': "aiet-bae93.appspot.com",
#     'messagingSenderId': "204318189072",
#     'appId': "1:204318189072:web:6a2261ee33dff483"
# }

# Use the application default credentials
cred = credentials.Certificate('./aiet-bae93-13ecac79617e.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/user/<name>', methods=['POST'])
def login(name = None):
    doc_ref = db.collection(u'users').document(name)
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })
    return name

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        # doc_ref = db.collection(u'users').document(request.uid)
        # doc_ref.set({
        #     u'first': request.first,
        #     u'last': request.last,
        #     u'born': request.year
        # })
        return "Done"
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return "error"