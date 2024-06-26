import os
from dotenv import load_dotenv, dotenv_values
import mysql.connector
import json
from flask import make_response, jsonify
from datetime import datetime, timedelta
import jwt
load_dotenv()

class RatingModel():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host=os.getenv('HOST'),port=os.getenv('PORT_NUMBER'),user=os.getenv('DATABASE_USER'),password=os.getenv('DATABASE_PASSWORD'),database=os.getenv('DATABASE_NAME'))
            self.con.autocommit = True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successful")
        except Exception as e:
            print("Error:", e)
        
    def rating_add_model(self, data):
        qry = "INSERT INTO rating(user_id, movie_id, rating) VALUES "
        for ratingdata in data:
            qry += f"({ratingdata['user_id']}, {ratingdata['movie_id']}, {ratingdata['rating']}),"
        finalqry = qry.rstrip(",")
        self.cur.execute(finalqry)
        return  make_response({"message":"Rating Created Successfully"}, 201) 
    
    def rating_getall_model(self):
        self.cur.execute("SELECT * FROM rating")
        result = self.cur.fetchall()
        if len(result)>0:
            return result
        else:
            return {"message":"No Data found"}   
