from flask import Flask, json, jsonify, request, make_response, Blueprint

import datetime

from ..models import user_models

from ..utils.validators import Verify

auth = Blueprint('auth', __name__, url_prefix='/api/v1/auth')

user_object = user_models.Accounts()

@auth.route('/signup', methods = ['POST'])
def register_user():
    '''endpoint to create an account'''
    data = request.get_json()
    if not data:
        return jsonify({"message": "Data set cannot be empty"}), 400
    email_address = data.get('email_address').strip()
    username = data.get('username').strip()
    password = data.get('password').strip()
    timestamp = datetime.datetime.now()

    
    result = jsonify(user_object.signup(email_address, username, password, timestamp))
    result.status_code = 201
    return result


@auth.route('/users', methods = ['GET'])
def member_list():
    '''endpoint to get all members on the site'''
    result = jsonify(user_object.get_all_users())
    result.status_code = 200
    return result


@auth.route('/users/<string:username>', methods = ['PUT'])
def edit_username(username):
    '''endpoint to edit the username'''
    current_username = user_object.get_single_user(username)
    data = request.get_json()["username"]
    current_username["username"] = data
    return jsonify(current_username)
    

@auth.route('/users/<string:username>', methods = ['DELETE'])
def delete_user(username):
    '''endpoint to delete a user'''
    search_username = user_object.get_single_user(username)
    user_models.user_accounts.remove(search_username)
    return jsonify(user_models.user_accounts)


    

