students = [{"Name":"Ashwin", "roll_id": 1, "parent": ["Raj","Asha"]},{"Name":"Arch", "roll_id": 2, "parent": ["Raj","Asha"]},{"Name":"Asha", "roll_id": 3, "parent": ["S A Prabhu","Vinaya"]}, {"Name":"Raj", "roll_id": 4, "parent": ["G N Shenoy","Radhabai"]}]

is_parent = False
p_name = input("Enter parents name ")
for i in students:
    if p_name in i["parent"]:
        print("%s and %s are %s's Parents" %(i["parent"][0],i["parent"][1],i["Name"]))
        is_parent = True
if not is_parent:
    print("Please enter a valid name this person is not in the list")
