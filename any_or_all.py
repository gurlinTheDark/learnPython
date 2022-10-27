patients = [{"name":"Ashwin","is_covid_positive":False, "is_adult":True},{"name":"Archana","is_covid_positive":True, "is_adult":True},{"name":"Asha","is_covid_positive":False, "is_adult":True},{"name":"Rajkumar","is_covid_positive":True, "is_adult":True}]

if any(i["is_covid_positive"]==True for i in patients):
    print("The list has covid positive patients, please maintain social distancing")
else:
    print("The list is safe")

if all(i["is_adult"]==True for i in patients):
    print("The list has no children")
else:
    print("The list has children")
