numbers = [3,6,2,7,3,6,9,23,57]
result = []
length = len(numbers)
for i in range(length):
    if numbers[i] not in result:
        result.append(numbers[i])
        
print(result)
