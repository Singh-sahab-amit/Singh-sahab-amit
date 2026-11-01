balance = 100000
user_name = str(input("Enter your user_name :"))
pin = int(input("Enter your pin :"))
if user_name == "AMIT SINGH" and pin == 742329:
    print("🔓 ACCESS-GRANTED!")
  

    while True:
        print("----Welcome to ATM-----")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("choose your no. what you want  :"))

        if choice == 1:
            print("your balance is:", balance)

        elif choice ==2:
            amount = int(input("Enter your amount to deposit  :"))
            if amount > 0:
                balance = balance + amount
                print("your current balance is:", balance)
            else:
                print("Invalid amount")
    
        elif choice ==3:
            amount = int(input("enter your amount to withdraw  :"))
            if amount > 0 and amount <= balance:
                balance = balance - amount
                print("your new balance is:", balance)
            elif amount <= 0:
                print("Invalid balance")

            else:
                print("Insufficient-Balance")
    
        else:
            print("   🤖 Thanks for using 🤖   ") 
            break

else:
    print("❎LOGIN-FAILED!!")