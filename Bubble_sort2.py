a = [15,2,25,19,12,102,10,17,90]

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range (0,i):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
print(bubble_sort(a)[:3])
