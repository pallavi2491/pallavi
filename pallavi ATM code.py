# Initial Setup Variables
stored_username = "student"
stored_password = "password123"
correct_pin = "1234"
balance = 10000.0

# 1. Login Phase
username_input = input("Enter Username: ")
password_input = input("Enter Password: ")

if username_input != stored_username:
    # If username is wrong, display the joint error message
    print("Incorrect Username and Password")
elif password_input != stored_password:
    # If username is right but password is wrong
    print("Incorrect Password")
else:
    # 2. Successful Login Phase
    print("\n--- Login Successful! Welcome to the ATM System ---")
    
    # Main ATM Menu Loop
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        # If the user wants to exit, we handle it immediately without asking for a PIN
        if choice == "5":
            print("Thank You")
            break
            
        # Ensure the user entered a valid menu option before asking for PIN
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            # Ask for PIN before any banking operation
            entered_pin = input("Enter your 4-digit PIN: ")
            
            if entered_pin != correct_pin:
                print("Incorrect PIN")
            else:
                # Option 1: Check Balance
                if choice == "1":
                    print("Current Balance: $", balance, sep="")
                
                # Option 2: Deposit
                elif choice == "2":
                    deposit_amount = float(input("Enter deposit amount: $"))
                    balance = balance + deposit_amount
                    print("Successfully Deposited! New Balance: $", balance, sep="")
                
                # Option 3: Withdraw
                elif choice == "3":
                    withdraw_amount = float(input("Enter withdrawal amount: $"))
                    if withdraw_amount <= balance:
                        balance = balance - withdraw_amount
                        print("Successfully Withdrawn! Remaining Balance: $", balance, sep="")
                    else:
                        print("Insufficient Balance")
                
                # Option 4: Transfer
                elif choice == "4":
                    receiver_acc = input("Enter receiver account number: ")
                    transfer_amount = float(input("Enter transfer amount: $"))
                    if transfer_amount <= balance:
                        balance = balance - transfer_amount
                        print("Successfully Transferred $", transfer_amount, " to Account ", receiver_acc, ".", sep="")
                        print("Remaining Balance: $", balance, sep="")
                    else:
                        print("Insufficient Balance")
        else:
            print("Invalid Choice! Please enter a number between 1 and 5.")