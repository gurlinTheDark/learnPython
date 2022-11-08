numbers = [13,25,4,7,11,4]
sum = int(input("Please enter a sum you want to obtain "))
length = len(numbers)
for (key,value) in enumerate(numbers):
    digits = sum - value
    if digits in numbers[key+1:length]:
        print("The given sum is obtained by %d and %d" %(digits,value))
        break
else:
    print("The sum entered by you is not obtained by any digits from the list")
