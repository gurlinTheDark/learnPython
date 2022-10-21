employees = [
    {"name": "Naveen",
    "sales": 20},
    {"name": "Ashwin",
    "sales": 50},
    {"name": "Asha",
    "sales": 100},
    {"name": "Archana",
    "sales": 50},
    {"name": "Rajkumar",
    "sales": 90},
    ]
    
best_sm = ""
max_sales = 0
for i in employees:
    if i['sales'] > max_sales:
        max_sales = i['sales']
        best_sm = i['name']
print("The best salesman of the year is %s" % best_sm)
