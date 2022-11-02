from flask import Flask
from flask import request
import json 
app = Flask(__name__)
user_details = []
init_message = [{"GET_/getDetails/<username>": "Get details of a user"}, {"POST_/addDetails": "Add a new User"}]

@app.route("/getDetails/<username>")
def get_user_details(username):
    print(username)
    for i in user_details:
        print('I am here %s', i['name'].lower())
        print(username.lower())
        if i['name'].lower() == username.lower():
            print("hello I am in here")
            return i
    return "Not found"        

@app.route("/addDetails",  methods=['POST'])
def add_user_details():
    data = json.loads(request.data)
    user_details.append(data)
    
    return "User Added" 

@app.route("/") 
def init_route():
    return init_message

@app.route("/getAllUsers")
def get_all_users():
    return user_details   

@app.route("/deleteUser/<username>", methods=['DELETE'])
def del_users(username):
    for i in user_details:
        if username == i["name"]:
            user_details.remove(i)
            return "User removed"
    else:
        return "sorry your username is not found"