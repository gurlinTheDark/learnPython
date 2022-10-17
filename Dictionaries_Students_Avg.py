students = {"Ashwin":0, "Archana":0, "Asha":0, "Rajkumar":0}
no_of_Sub = 3
max_avg = 0
for name,avg1 in students.items():
    avg = int(input("Enter the Average marks for %s" % name))
    students[name] = avg
    if avg > max_avg:
        max_avg = avg
print('The max average is %d' % max_avg)
for name,avg in students.items():
    print("The average marks for %s is %d" %(name,avg))
    
print(students)
