number1 =int(input("Please enter a number "))
number2 =int(input("Please enter another number "))

def square(number):
    sq = number**2
    return sq

print(square(number1))

def rev_number(number):
    r_number = 0
    while number>0:
        r = number%10
        r_number = r_number*10+r
        number = number//10
    if r_number == number2:
        print("%d and %d are palindrome numbers" %(number1,number2))
    else:
        print("%d and %d are not palindrome numbers" %(number1,number2))
    return r_number

print(rev_number(number1))
