arr = [15,13,34,64,23,68,63]
largest = 0
i = 0
j = len(arr)-1
while i<j:
    if arr[i] > largest:
        largest = arr[i]
    if arr[j] > largest:
        largest = arr[j]
    i = i+1
    j = j-1
print(largest)
