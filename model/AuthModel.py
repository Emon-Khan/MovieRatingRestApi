import os
from dotenv import load_dotenv, dotenv_values
import mysql.connector
import json
from flask import make_response, request
import jwt
import re
from functools import wraps
load_dotenv()

class AuthModel():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host=os.getenv('HOST'),port=os.getenv('PORT_NUMBER'),user=os.getenv('DATABASE_USER'),password=os.getenv('DATABASE_PASSWORD'),database=os.getenv('DATABASE_NAME'))
            self.con.autocommit = True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successful")
        except:
            print("Some Error")
    def token_auth(self):
        def inner1(func):
            @wraps(func)
            def inner2(*args, **kwargs):
                authorization = request.headers.get("authorization")
                if authorization is None:
                    return make_response({"ERROR": "Token is not given"}, 500)
                else:
                    if re.match("^Bearer *([^ ]+) *$", authorization, flags = 0):
                        # print(flags)
                        token = authorization.split(" ")[1]
                        try:
                            jwtdecoded = jwt.decode(token, "Emon", algorithms="HS256")
                        except jwt.ExpiredSignatureError:
                            return make_response({"ERROR":"TOKEN EXPIRED"}, 401)
                        user_id = jwtdecoded['payload']['id']
                        self.cur.execute(f"SELECT * FROM users where id = '{user_id}'")
                        result = self.cur.fetchall()
                        if len(result)>0:
                            return func(*args, **kwargs)
                        else:
                            return make_response({"ERROR": "You are not allowed to view this endpoint"}, 401)                             
                    else:
                        return make_response({"ERROR": "INVALID_TOKEN"}, 401)
            return inner2
        return inner1
