number = int(input("Enter an input "))

for rows in range(number+1):
    string = ""
    for columns in range(rows):
        string+= "*"
    print(string)
