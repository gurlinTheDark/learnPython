a = [{"Name": "Ashwin", "Marks": [37,20,29],"Place": "Goa"},{"Name": "Archana", "Marks": [25,34,18], "Place": "Bangalore"},{"Name": "Asha", "Marks": [26,14,38], "Place": "Kochi"}, {"Name": "Rajkumar", "Marks": [26,14,38], "Place": "Kochi"}, {"Name": "Naveen", "Marks": [26,14,38], "Place": "Bangalore"}]

city = input("Enter the city ")
count = 0
for i in a:
    if city.lower() == i["Place"].lower():
        count = count+1
print("%d people belong to %s" %(count,city))
