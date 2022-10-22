students = [
    {
    "name":"Ashwin",
    "eng":90,
    "math":99
},{
    "name":"Archana",
    "eng":70,
    "math":69
},{
    "name":"Navin",
    "eng":95,
    "math":89
},{
    "name":"Rajkumar",
    "eng":60,
    "math":59
},{
    "name":"Asha",
    "eng":94,
    "math":58
},{
    "name":"Brian",
    "eng":80,
    "math":78
}]
sum_marks = 0

for i in students:
    tot_marks = i['eng'] + i["math"]
    print(tot_marks)
    print(i["name"])
    if tot_marks>sum_marks:
        sum_marks = tot_marks
        name = i["name"]
print("The topper of the class is %s" % name)
