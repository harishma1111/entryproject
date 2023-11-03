bank_data = {
    "1357": {
        "pin": "1234",
        "balance": 1000
    },
    "2468": {
        "pin": "4321",
        "balance": 500
    }
}

def login():
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    if account_number in bank_data and pin == bank_data[account_number]["pin"]:
        print("Login successful!")
        return account_number
    else:
        print("Invalid account number or PIN.")
        return None


def deposit(account_number):
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        bank_data[account_number]["balance"] += amount
        print(f"Deposit of {amount} successful.")
        print(f"Updated balance: {bank_data[account_number]['balance']}")
    else:
        print("Invalid amount. Deposit amount should be greater than zero.")


def withdraw(account_number):
    amount = float(input("Enter the amount to withdraw: "))
    if 0 < amount <= bank_data[account_number]["balance"]:
        bank_data[account_number]["balance"] -= amount
        print(f"Withdrawal of {amount} successful.")
        print(f"Updated balance: {bank_data[account_number]['balance']}")
    else:
        print("Invalid amount. Withdrawal amount should be greater than zero and less than or equal to account balance.")


def print_banking_system():
    print("Welcome to the Banking System!")
    while True:
        account_number = login()
        if account_number:
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Logout")
                choice = input("Enter your choice : ")
                if choice == "1":
                    deposit(account_number)
                elif choice == "2":
                    withdraw(account_number)
                elif choice == "3":
                    print(f"Your current balance: {bank_data[account_number]['balance']}")
                elif choice == "4":
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid choice. Please choose again.")
        else:
            break

if __name__ == "__main__":
    print_banking_system()