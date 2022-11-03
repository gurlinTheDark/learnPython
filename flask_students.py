from flask import Flask
from flask import request
import json 
app = Flask(__name__)

students = [{"Name":"Ashwin", "roll_id": 1, "parent": "Rajkumar"},{"Name":"Archana", "roll_id": 2, "parent": "Asha"},{"Name":"Asha", "roll_id": 3, "parent": "Vinaya"}, {"Name":"Rajkumar", "roll_id": 4, "parent": "Radhabai"}]

@app.route("/getDetails/<username>")
def get_details(username):
    for i in students:
        if username == i["Name"]:
            return i
    return "given username not there in the list"

@app.route("/getAllStudents")
def get_all_students():
    return students        

@app.route("/delete/<username>", methods=["DELETE"])
def del_students(username):
    for i in students:
        if username == i["Name"]:
            students.remove(i)
            return "The given username is removed from the list"
    return "given username is not in the list"