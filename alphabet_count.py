list = ["ashwin", "archana", "asha"]
letter = input("Enter the letter to be counted from the string ")
count = 0

def count_letters(string,letter):
    count = 0
    for i in string:
        if i.lower() == letter.lower():
            count+=1
    return count

for i in list:
    count = count + count_letters(i,letter)  
    
print("The number of %s in list is %d" %(letter,count))
