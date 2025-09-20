from atm import ATM

def main():
    atm = ATM()
    atm.create_account("1234", "1111", 1000)

    acc_num = input("Enter account number: ")
    pin = input("Enter PIN: ")
    account = atm.authenticate(acc_num, pin)

    if account:
        print("Login successful!")
        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Choose option: ")

            if choice == "1":
                print("Balance:", account.check_balance())
            elif choice == "2":
                amount = float(input("Enter amount: "))
                print("New Balance:", account.deposit(amount))
            elif choice == "3":
                amount = float(input("Enter amount: "))
                result = account.withdraw(amount)
                if result is not None:
                    print("New Balance:", result)
                else:
                    print("Insufficient funds")
            elif choice == "4":
                break
            else:
                print("Invalid choice")
    else:
        print("Authentication failed!")

if __name__ == "__main__":
    main()
