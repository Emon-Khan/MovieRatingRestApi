from app import app
from model.UserModel import UserModel
from flask import request
obj = UserModel()

@app.route('/users/getall')
def getall_controller():
    return obj.user_getall_model()

@app.route('/users/<id>')
def getbyid_controller(id):
    return obj.user_getbyid_model(id)

@app.route('/users/adduser', methods=['POST'])
def adduser_controller():
    return obj.user_add_model(request.form)

@app.route('/users/updateuser', methods=['PUT'])
def updateuser_controller():
    return obj.user_update_model(request.form)

@app.route('/users/deleteuser/<id>', methods=['DELETE'])
def deleteuser_controller(id):
    return obj.user_delete_model(id)