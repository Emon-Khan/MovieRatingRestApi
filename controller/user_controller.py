from app import app
from model.UserModel import UserModel
from model.AuthModel import AuthModel
from flask import request
obj = UserModel()
auth = AuthModel()

@app.route('/users/getall')
@auth.token_auth()
def getall_controller():
    return obj.user_getall_model()

@app.route('/users/<id>')
@auth.token_auth()
def getbyid_controller(id):
    return obj.user_getbyid_model(id)

@app.route('/users/adduser', methods=['POST'])
def adduser_controller():
    return obj.user_add_model(request.json)

@app.route('/users/updateuser/<id>', methods=['PUT'])
@auth.token_auth()
def updateuser_controller(id):
    return obj.user_update_model(request.form, id)

@app.route('/users/deleteuser/<id>', methods=['DELETE'])
@auth.token_auth()
def deleteuser_controller(id):
    return obj.user_delete_model(id)

@app.route('/users/login', methods=['POST'])
def user_login_controller():
    # request.form
    return obj.user_login_model(request.form)
    # return obj.user_login_model(request.form)