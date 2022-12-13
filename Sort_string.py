sentence = "This is Ashwin and Iam learning python"
list = sentence.split(" ")
temp = ""
for i in range(len(list)-1):
    for j in range(0,i):
        if len(list[i]) > len(list[j]):
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
print(list)
