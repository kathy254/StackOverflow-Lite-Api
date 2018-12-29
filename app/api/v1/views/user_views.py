from flask import Flask, json, jsonify, request, make_response, Blueprint

import datetime

from ..models import user_models

from ..utils.validators import Verify
from ..utils.auth import token_required

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

    email_found = user_object.get_user_email(email_address)

    if email_found == "User not found":
        if user_object.get_single_user(username) == "User not found":
        
            try:


                result = jsonify(user_object.signup(email_address, username, user_object.generate_hash(password), timestamp))
                result.status_code = 201
                return result
            
            except Exception as e:
                return make_response(jsonify({
                    "message": str(e),
                    "status": "Failed"
                }), 500)
        
        return make_response(jsonify({
            "status": "Failed",
            "message": "This username already exists. Please choose another one."
        }), 500)

    return make_response(jsonify({
        "status": "Failed",
        "message": "This email address already exists. Please log in"
    }), 500)



@auth.route('/login', methods=['POST'])
def login_user():
    '''endpoint to log into an account'''
    data = request.get_json()
    username = data.get("username").strip()
    password = data.get("password").strip()

    try:
        user_login = user_object.get_single_user(username)
        if user_login == "User not found":
            return make_response(jsonify({
                "status": "Failed",
                "message": "User does not exist"
            }), 200)

        if user_login and user_object.verify_hash(password, user_login['password']):
            username = user_login['username']
            token = user_object.encode_login_token(username, password)

            if token:
                return make_response(jsonify({
                    "status": "OK",
                    "message": "Welcome {}. You have logged in successfully".format(username),
                    "token": token.decode()
                }), 200)
        
        else:
            return make_response(jsonify({
                "status": "Failed",
                "message": "Password is incorrect. Please try again."
            }), 400)

    except Exception as e:
        return make_response(jsonify({
            "message": str(e),
            "status": "Failed"
        }), 500)


@auth.route('/users', methods = ['GET'])
@token_required
def member_list():
    '''endpoint to get all members on the site'''
    result = jsonify(user_object.get_all_users())
    result.status_code = 200
    return result


@auth.route('/users/<string:username>', methods = ['PUT'])
@token_required
def edit_username(username):
    '''endpoint to edit the username'''
    current_username = user_object.get_single_user(username)
    data = request.get_json()["username"]
    current_username["username"] = data
    return jsonify(current_username)
    


@auth.route('/users/<string:username>', methods = ['DELETE'])
@token_required
def delete_user(username):
    '''endpoint to delete a user'''
    search_username = user_object.get_single_user(username)
    user_models.user_accounts.remove(search_username)
    return jsonify(user_models.user_accounts)


