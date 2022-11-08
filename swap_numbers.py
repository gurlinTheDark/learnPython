numbers = [13,25,4,7,11,4]
no_to_be_found = int(input("Please enter a number "))
length = len(numbers)
for (key,value) in enumerate(numbers):
    if value == no_to_be_found:
        numbers[key] = numbers[0]
        numbers[0] = no_to_be_found
print(numbers)
