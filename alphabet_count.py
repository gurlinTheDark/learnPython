list = ["ashwin", "archana", "asha"]
letter = input("Enter the letter to be counted from the string ")
count = 0
for i in list:
    for j in i:
        if j.lower() == letter.lower():
            count+=1
print("The number of %s in the list is %d" %(letter,count))
