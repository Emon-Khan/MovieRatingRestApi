from app import app
from model.AuthModel import AuthModel
from model.RatingModel import RatingModel
from flask import request
rating_obj = RatingModel()
auth = AuthModel()

@app.route('/rating/add', methods=['POST'])
@auth.token_auth()
def rating_add_controller():
    return rating_obj.rating_add_model(request.json)

@app.route('/rating/getall')
def rating_getall_controller():
    return rating_obj.rating_getall_model()