arr = [12,15,15,14,45,34,22,12,35,45]

result = []
i = 0
j = len(arr)

while i<j:
    z = i+1
    while z<len(arr):
        if arr[i] == arr[z]:
            result.append(arr[i])
        z+=1
    i+=1
print(result)
