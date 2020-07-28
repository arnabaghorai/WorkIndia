"""
    Routes for the endpoint /app

"""

from flask import Flask, request, jsonify, make_response
import uuid
import hashlib 
from app import app, db, ma
from app.models import User, Note, notes_schema
from flask import Blueprint


api = Blueprint('api',__name__,url_prefix='/app')

@api.route('/user', methods=['POST'])
def create_user():

    """
        Creates a user, 
        - Creates user id , public_id
        - Stores username nad hashed password in the database

    """

    data = request.get_json()

    username=data['username']
    password=data['password']

    hashed_password =  hashlib.sha256(password.encode())
    hashed_password = hashed_password.hexdigest()
    

    user_exist = User.query.filter_by(username=username).first()

    if user_exist:
        return jsonify({'status':"Failed" , 'message' : 'Current username is already taken'}) , 409


    new_user = User(public_id=str(uuid.uuid4()), username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'status' : 'Account created!'}), 201

@api.route('/user/auth', methods = ["POST"])
def login():

    """
        Validates User Login

    """

    data = request.get_json()

    username=data['username']
    password=data['password']

    

    hashed_password =  hashlib.sha256(password.encode())
    hashed_password = hashed_password.hexdigest()


    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({'status' : 'Failed', 'message': 'User does not exist'}) , 404

    if( user.password == hashed_password):

        # return jsonify({'status' : 'Success' , "userId" : user.public_id})

        return jsonify({'status' : 'Success' , "userId" : user.id})
    else:
        return jsonify({'status' : 'Failed' , "Invalid Password" }) , 401



@api.route('/sites',methods = ['POST'])
def add_note():

    """
        Valid User with valid id can add a note

    """

    data = request.get_json()
    note_text = data['note']

    userId = request.args.get('user',None)

    if not userId:
        return jsonify({'status' : 'Failed', 'message': 'Provide userId in parameters'}) , 400
    
    user = User.query.get(userId)


    if not user:
        return jsonify({'status' : 'Failed', 'message': 'Invalid userId'}) , 404

    note = Note(note = note_text,user_id = userId)
    db.session.add(note)
    db.session.commit()

    return jsonify({'status' : 'success'}) , 201

@api.route('/sites/list/',methods = ['GET'])
def get_notes():


    """
        Get all the notes of the given user

    """

    userId = request.args.get('user',None)

    if not userId:
        return jsonify({'status' : 'Failed', 'message': 'Provide userId in parameters'}) , 400
    
    user = User.query.get(userId)
    


    if not user:
        return jsonify({'status' : 'Failed', 'message': 'Invalid userId'}) , 404

    notes = Note.query.filter_by(user_id=userId).all()

    notes = notes_schema.dump(notes)

    return jsonify({"notes":notes})