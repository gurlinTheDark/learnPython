a = [{"Name": "Ashwin", "Marks": [37,20,29]},{"Name": "Archana", "Marks": [25,34,18]},{"Name": "Asha", "Marks": [26,14,38]}]

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(0,i):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
for i in a:
    print("%s's marks in descending order is %s" %(i["Name"],bubble_sort(i["Marks"])))
