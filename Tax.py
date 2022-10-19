tax_payers = {}

def calc_tax():
    tax = 0.0
    income  = float(input("Enter your income in Rs"))
    if (income <= 250000):
        tax = 0
    if (income > 250000 and income <= 500000):
        tax = (5/100)*(income-250000)
    if (income >500000 and income <=1000000):
        tax = (10/100)*(income-500000) + (5/100)*(250000)
    if (income >1000000 and income <=1500000):
        tax = (20/100)*(income-1000000) + (10/100)*(500000) + (5/100)*(250000)
    if (income > 1500000):
        tax = (30/100)*(income-1500000) + (20/100)*(1000000) + (10/100)*(500000) + (5/100)*(250000)

    return tax

def calc_cum_tax():
    cum_tax = 0.0
    for name,tax in tax_payers.items():
        cum_tax = cum_tax + tax
    print("The tax collect by GOI is Rs %.2f" % cum_tax)
while True:
    opt = int(input("Choose an option 1) Caculate tax for a new person 2) Calculate cumulative tax collected by GOI"))
    if opt==1:
        name = input("Enter your name")
        tax_payers[name] = calc_tax()
        print("Hi %s youe income tax is %d" %(name,tax_payers[name]))
    else:
        calc_cum_tax()
