number_list = []

while (1):
    opn = int(input("Enter the operation to perform 1) Addition 2) Subtraction 3) Multiplication 4) Division 5) Square 6) Square root 7) Cube 8) Cube root 9) x^y 10) factorial "))
    if opn == 1 or opn == 2 or opn == 3 or opn == 4:
        number = int(input("Enter the count of numbers "))
        for i in range(0,number):
            num = int(input("Enter the number "))
            number_list.append(num)
    if opn == 1:
        sum = sum(number_list)
        print("The sum of the numbers is", sum)
    if opn == 2:
        difference = number_list[0]
        for i in range(1,len(number_list)):
            difference = difference - number_list[i]
        print("The difference of the numbers is", difference)
    if opn == 3:
        multiplication = 1
        for i in number_list:
            multiplication = multiplication * i
        print("The multiplication of the numbers is", multiplication)
    if opn == 4:
        division = number_list[0]
        for i in range(1,len(number_list)):
            division = division/number_list[i]
        print("The division of the numbers is", division)
    if opn == 5 or opn == 6 or opn == 7 or opn == 8 or opn == 9 or opn == 10:
        num = int(input("Enter a number "))
    if opn == 5:
        square  = num**2
        print("The square of %d is" %num,square)
    if opn == 6:
        sqrt = num**(1/2)
        print("The square root of %d is" %num,sqrt)
    if opn == 7:
        cube = num**3
        print("The cube of %d is" %num,cube)
    if opn == 8:
        cube_root = num**(1/3)
        print("The cube root of %d is" %num,cube_root)
    if opn == 9:
        power = int(input("Enter the power to be raised to the number "))
        ans = num**power
        print("%d to the power raised to %d is" %(num,power),ans)
    if opn == 10:
        factorial = num
        for i in range(num-1,1,-1):
            factorial = factorial * i
        print("%d factorial is" % num, factorial)
