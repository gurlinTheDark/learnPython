a = int(input("Enter the number of integers"))
set_a = set({})
for i in range(1,a+1):
    b = int(input("Enter the %d number" % i))
    set_a.add(b)
print(set_a)
set_b = set({20,15,12,2})

set_a.update(set_b)
set_a.remove(2)
set_a.discard(2)
print(set_a.clear())
del set_a
print(set_a)
