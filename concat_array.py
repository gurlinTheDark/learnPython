a = [31,13,4,148,700,1000]
b = [24,27,64,243,300]
i = 0
j = 0
a.sort()
b.sort()

while i < len(a) and j < len(b):
    if a[i] > b[j]:
        a.insert(i,b[j])
        j = j+1
    i = i+1
while i == len(a) and j < len(b):
    a.append(b[j])
    j = j + 1

print(a)
