details = {}
no = int(input("How many people?"))
for i in range (1,no+1):
    name = input("Enter your name")
    age = int(input("enter your age"))
    details[name] = age
print(details)
for name,age in details.items():
    if age<18:
       print("%s is a youngster" % name)
    elif age>18 and age<60:
       print("%s is an adult" % name)
    else:
       print("%s is a senior citizen"% name)

fut_age = input("Do you want to know everyone's future age? choose an option 1) Y 2) N")
if fut_age == "Y":
    a = int(input("After how many years do you want to know your age?"))
    for name,age in details.items():
        f_age = age + a
        details[name] = f_age
        print("%s's current age is %d and after %d years will be %d" %(name,age,a,f_age))
        
print(details)
    
