from flask import Flask
from flask import request
import json 
app = Flask(__name__)
user_details = []

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
