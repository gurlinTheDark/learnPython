account_holders = {"Ashwin":2000, "Archana":3000, "Asha":3420, "Rajkumar":4284, "Naveen":4358}
bal = 0.0
trans_Amt = 0.0
name = input("Enter your name")
if name in account_holders:
    bal = account_holders[name]
    while(1):
        a = int(input("Enter an option 1. debit 2. credit 3. check balance 4. exit"))
        if a == 1:
            trans_Amt = float(input("Enter the transaction amount"))
            bal = bal - trans_Amt
            account_holders[name] = bal
            print("Your current balance is Rs %.2f" % bal)
        elif a == 2:
            trans_Amt = float(input("Enter the amount to be credited"))
            bal = bal + trans_Amt
            account_holders[name] = bal
            print("Your current balance is Rs %.2f" % bal)
        elif a == 3:
            print("Your current balance is Rs %.2f" % bal)
        else:
            print("Thank you and visit again")
            break
else:
    print("You don't have an account with out bank")
