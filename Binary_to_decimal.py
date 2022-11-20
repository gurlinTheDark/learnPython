#11 = 1* 2^1 + 1 * 2^0
number = int(input("Enter a number "))
modified_number = 0
loop_count = 0
while number>0:
    remainder = number%10
    remainder = remainder * (2) ** loop_count
    modified_number = modified_number + remainder
    number = number //10
    loop_count+=1
print(modified_number)
