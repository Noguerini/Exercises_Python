def showBalance():
    print("Your balance is " + str(balance))

def deposit():
    global balance
    increasedDeposit = int(input("How much would you like to deposit?: "))
    balance += increasedDeposit
    print("Deposit successful!")

def withdraw():
    global balance
    decreasedDeposit = int(input("How much would you like to withdraw?: "))
    if decreasedDeposit <= balance:
        balance -= decreasedDeposit
        print("Withdrawal successful!")
    else:
        print("Insufficient funds!")

balance = 0
is_running = True

while is_running:
    print("\nBanking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Which operation would you like to perform?: ")
    
    if choice == "1":
        showBalance()
    elif choice == "2":
        deposit()
    elif choice == "3":
        withdraw()
    elif choice == "4": 
        is_running = False
        print("Thank you for using the Banking Program!")
    else:
        print("Invalid option. Please try again.")