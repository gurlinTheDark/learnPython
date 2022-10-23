to_do = [{"Task":"Clean House", "Status":"Done"},{"Task":"Gardening", "Status":"Not Done"},{"Task":"Homework", "Status":"Not Done"},{"Task":"Cooking", "Status":"Done"},{"Task":"Washing Clothes", "Status":"Not Done"}]

while (1):
    option = int(input("Choose an option you want to do 1) Add a task,  2) Change a task 3) List all tasks 4) Delete a task "))
    if option == 1:
        task = input("Enter the task you want to add ")
        status = input("Update the status for above task ")
        to_do.append({"Task":task, "Status":status})
        #print(to_do)
    elif option == 2:
        task = input("Enter the task you want to change ")
        status = input("Update the status for above task ")
        for i in to_do:
            if i["Task"] == task:
                i["Status"] = status
        print(to_do)
    elif option == 3:
        for i in to_do:
            print("%s is %s" % (i["Task"],i["Status"]))
    elif option == 4:
        task = input("Enter the task you want to delete ")
        for i in to_do:
            if task == i["Task"]:
                to_do.remove(i)
            else:
                print("This Task does not belong to the list")
        print(to_do)
