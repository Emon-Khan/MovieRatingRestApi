import mysql.connector
import json
from flask import make_response, jsonify
from datetime import datetime, timedelta
import jwt

class UserModel():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6696109",password="kR52xyVGF9",database="sql6696109")
            self.con.autocommit = True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successful")
        except Exception as e:
            print("Error:", e)
            
    def user_getall_model(self):
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result)>0:
            return result
        else:
            return {"message":"No Data found"}
        
    def user_getbyid_model(self, id):
        self.cur.execute(f"SELECT * FROM users WHERE id = {id}")
        result = self.cur.fetchall()
        if len(result)>0:
            return result
        else:
            return make_response({"message":"User id not found"}, 500)
    
    def user_add_model(self, data):
        qry = "INSERT INTO users(name, email, phone, password) VALUES "
        for userdata in data:
            qry += f"('{userdata['name']}', '{userdata['email']}', '{userdata['phone']}', '{userdata['password']}'),"
        finalqry = qry.rstrip(",")
        self.cur.execute(finalqry)
        return  make_response({"message":"User Created Successfully"}, 201)
    
    def user_update_model(self, data, id):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}' WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"User Updated Successfully"}, 201)
        else:
            return make_response({"message":"Nothing to update"}, 204)
        
    def user_delete_model(self, id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return make_response({"message":"User Deleted Successfully"}, 202)
        else:
            return make_response({"message":"User id not found"}, 500)
    
    def user_login_model(self, data):
        self.cur.execute(f"SELECT id, name, email, phone FROM users WHERE email='{data['email']}' and password='{data['password']}'")
        result = self.cur.fetchall()
        if len(result)>0:
            userdata = result[0]
            exp_time = datetime.now() + timedelta(minutes=15)
            exp_epoc_time = int(exp_time.timestamp())
            payload = {
                "payload":userdata,
                "exp":exp_epoc_time
            }
            jwtoken = jwt.encode(payload, "Emon", algorithm="HS256")
            return make_response({"token":jwtoken}, 200)
        else:
            return make_response({"ERROR": "Incorrect Credentials"}, 401)