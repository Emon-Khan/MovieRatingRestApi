import mysql.connector
from flask import make_response, jsonify

class UserModel():
    def __init__(self):
        try:
            self.con = mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6696109",password="kR52xyVGF9",database="sql6696109")
            self.con.autocommit = True
            self.cur=self.con.cursor(dictionary=True)
            print("Connection Successful")
        except:
            print("Some Error")
            
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
        self.cur.execute(f"INSERT INTO users(name, password, phone, email)VALUES('{data['name']}', '{data['password']}', '{data['phone']}', '{data['email']}')")
        return  make_response({"message":"User Created Successfully"}, 201)
    
    def user_update_model(self, data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}' WHERE id={data['id']}")
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