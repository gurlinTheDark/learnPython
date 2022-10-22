list_a = [3, 2, 1]  

def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        print("i = %d, arr[%d] = %d" % (i,i, arr[i]))
        for j in range(0,i):
            print("j = %d, arr[%d] = %d"% (j,j, arr[j]))
            if arr[i]<arr[j]:
                print("swapped i and j because %d < %d" % (arr[i], arr[j]))
                arr[j],arr[i] = arr[i],arr[j]
                
    return(arr)
print(bubble_sort(list_a))
