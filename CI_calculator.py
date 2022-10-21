sal = {"Ashwin":5000, "Archana":8000, "Asha":7000, "Rajkumar":10000, "Naveen":9000}

for name,salary in sal.items():
    name = input("Enter your name")
    if name in sal:
        r = float(input("Enter your hike per year"))
        n = int(input("Enter the number of years"))
        a = salary*(1+(r/100))**(1*n)
        print("%s, after %d years will make Rs %d as salary" %(name,n,a))
    else:
        print("You dont belong to the list, please try again")
