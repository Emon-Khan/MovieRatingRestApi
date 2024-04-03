from app import app
from model.MovieModel import MovieModel
from model.AuthModel import AuthModel
from flask import request
movie_obj = MovieModel()
auth = AuthModel()

@app.route('/movie/add', methods=['POST'])
@auth.token_auth()
def movie_add_controller():
    return movie_obj.movie_add_model(request.json)

@app.route('/movie/getall')
def movie_getall_controller():
    return movie_obj.movie_getall_model()