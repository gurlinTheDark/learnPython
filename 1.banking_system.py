bal = 0.0
trans_Amt = 0.0
while(1):
    a = int(input("Enter an option 1. debit 2. credit 3. check balance 4. exit"))
    
    if a == 1:
        trans_Amt = float(input("Enter the transaction amount"))
        bal = bal - trans_Amt
        print("Your current balance is Rs %.2f" % bal)
    elif a == 2:
        trans_Amt = float(input("Enter the amount to be credited"))
        bal = bal + trans_Amt
        print("Your current balance is Rs %.2f" % bal)
    elif a == 3:
        print("Your current balance is Rs %.2f" % bal)
    else:
        print("Thank you and visit again")
