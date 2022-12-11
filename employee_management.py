employees = [{"id": 1, "name": "Ashwin", "sal": 5000},{"id": 2, "name": "Archana", "sal": 45000},{"id": 3, "name": "Asha", "sal": 15000},{"id": 4, "name": "Rajkumar", "sal": 30000}]

while (1):
    opn = int(input("Enter an option 1) Add a new employee 2) Delete an employee 3) Edit an employee 4) List the employees "))
    if opn == 1:
        details = input("Enter the id, name and salary of the new employee ")
        details = details.split(",")
        details[0] = int(details[0])
        is_id = False
        for i in employees:
            if details[0] == i["id"]:
                is_id = True
                print("Please enter a new id")
        if not is_id:
            employees.append({"id" : details[0], "name" : details[1], "sal" : int(details[2])})
        print("The list of employees = ",employees)
    if opn == 2:
        details = int(input("Enter the id of the employee to be deleted "))
        for i in employees:
            if details == i["id"]:
                employees.remove(i)
        print("The employee with this id is removed")
        print("The list of employees =", employees)
    if opn == 3:
        details = int(input("Enter the id of the employee to be edited "))
        key = input("Enter the key to update ")
        if key.lower() == "id".lower():
            print("Sorry you cannot modify this field")
            continue
        if key.lower() == "name".lower():
            new_name = input("Please enter new name for this employee ")
            employees[details-1]["name"] = new_name
            print("Name for the above employee has been changed")
        if key.lower() == "salary".lower():
            new_sal = int(input("Please enter new salary for this employee "))
            employees[details-1]["sal"] = new_sal
            print("Salary for the employee has been changed")
        else:
            print("Please enter a valid key to be changed")
            continue
        print("The updated list of employees =", employees)
    if opn == 4:
        print("Here is the list of employees as per your request =", employees)
