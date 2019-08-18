from flask import Flask, request, jsonify
from firebase_admin import auth, db
import requests
from . import routes


@routes.route('/registerUser', methods=['POST'])
def registerUser():
    firstName = request.json.get('firstName')
    lastName = request.json.get('lastName')
    email = request.json.get('email')
    password = request.json.get('password')
    phoneNumber = request.json.get('phoneNumber')

    # check data
    if((firstName == None) | (lastName == None) | (password == None) | (email == None) | (phoneNumber == None)):
        return {
            "success": False,
            "message": "Missing data"
        }
    
    # Create new user
    user = auth.create_user(
        email=email,
        email_verified=False,
        phone_number=phoneNumber,
        password=password,
        display_name='{0} {1}'.format(firstName, lastName),
        disabled=False
    )

    ref = db.reference(path='users/{0}'.format(user.uid))
    ref.set({
        'email': email,
        'phoneNumber': phoneNumber,
        'firstName': firstName,
        'lastName': lastName,
    })

    return {
        "success": True,
        "message": "User created"
    }
     


@routes.route('/getUser/<uid>', methods=['GET'])
def getUser(uid = None):

    # get user data
    userData = db.reference(path='users/{0}'.format(uid)).get()
    print('user',userData)
    if (userData == None):
        return {
            "success": False,
            "message": "wrong uid"
        }, 400
    else:
        return {
            "success": True,
            "user": userData
        }, 200
