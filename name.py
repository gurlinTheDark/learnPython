name = input("Please enter a name ")
letter = input("Please enter the letter to be counted ")
pos = int(input("please enter the position to be modified "))
count = 0
for index in range(len(name)):
    if name[index] == letter:
        name = name[:index]+"$" + name[index+1:]
    #if index == pos:
        #name = name[:index] + "@" + name[index+1:]
        #print(name)

name = name[:pos] + "@" + name[pos+1:]

print(name)
