no_of_Subs = int(input("Enter number of subjects"))
scores = []
for i in range(1,no_of_Subs+1):
    marks = int(input("Enter the marks"))
    scores.append(marks)
    avg = (sum(scores))/no_of_Subs
print("The average for %d subjects is %d" % (no_of_Subs,avg))
