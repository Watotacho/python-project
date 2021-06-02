balance=1000
print("""
Welcome to ATM Machine
choose Transaction

1) BALANCE
2) WITHDRAW
3) DEPOSIT
4) EXIT

""")
while True:

    option = int(input("Enter Transaction: "))
    if(option == 1):
        print("Your Balance is: ",balance)
        anothertrans = input("Do you want to make another transaction")
        if(anothertrans == "YES"):
            continue
        else:
            break
    elif(option == 2):
        withdraw = float(input("Enter amount to withdraw:"))
        if(balance>withdraw):
            total = balance - withdraw
            print("Success")
            print("Your new balance is: ",total)
        else:
            print("insufficient balance")
    elif(option == 3):
        deposit = float(input("Enter amount to deposit:"))
        totalbalance = balance + deposit
        print("success")
        print("total balance now is: ",totalbalance)
    elif(option == 4):
             print("closing the program...")
             exit()
    else:
        print("no selected transaction")
