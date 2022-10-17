students = {"Ashwin":0, "Archana":0, "Asha":0, "Rajkumar":0}
no_of_Sub = int(input("Enter the number of subjects"))
scores = []

for name,avg1 in students.items():
    for i in range (1,no_of_Sub+1):
        marks = int(input("Enter the marks for each subject for %s" % name))
        scores.append(marks)
        avg = (sum(scores))/no_of_Sub
        students[name] = avg
for name,avg in students.items():
    print("The average marks for %s is %.2f" %(name,avg))
print(students)
