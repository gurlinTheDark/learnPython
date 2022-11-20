numbers = [23, 25, 74, 53, 62, 18]
sum = 0
even = []
for i in range(len(numbers)):
    if i%2 == 0:
        print("The values of even indices " ,numbers[i])
        sum = sum + numbers[i]
    if numbers[i]%2 == 0:
        even.append(numbers[i])
print("The even numbers are ", even)
print("The sum of even numbers is ",sum)
print("The list ", numbers)
