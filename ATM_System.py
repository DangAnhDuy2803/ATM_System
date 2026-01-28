class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposit: +{amount}")
            print("✅ Deposit successful!")
        else:
            print("❌ Invalid amount!")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient balance!")
        elif amount <= 0:
            print("❌ Invalid amount!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdraw: -{amount}")
            print("✅ Withdraw successful!")

    def view_balance(self):
        print(f"💰 Current balance: {self.balance}")

    def view_transactions(self):
        if not self.transactions:
            print("📭 No transactions yet.")
        else:
            print("📜 Transaction History:")
            for t in self.transactions:
                print("-", t)

class VIPAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.points = 0
        self.amount_per_transaction = []

    def deposit(self, amount):
        super().deposit(amount)
        self.points += int(amount // 100)
        self.amount_per_transaction.append(amount)

    def withdraw(self, amount):
        super().withdraw(amount)
        self.points += int(amount // 100)
        self.amount_per_transaction.append(amount)

    def receive_ads(self):
        print("📢 VIP Promotion: Get 2x points on deposits today!")

    def redeem_points(self):
        if self.points >= 10:
            self.points -= 10
            self.balance += 50
            print("🎁 Redeemed 10 points for 50 balance!")
        else:
            print("❌ Not enough points!")

    def view_transactions(self):
        print("🌟 VIP TRANSACTION HISTORY 🌟")
        super().view_transactions()
        print(f"⭐ Reward points: {self.points}")

def transaction_menu(account):
    while True:
        print("\n--- TRANSACTION MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View transaction history")

        if isinstance(account, VIPAccount):
            print("4. Redeem reward points")
            print("5. Back to main menu")
        else:
            print("4. Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter withdraw amount: "))
            account.withdraw(amount)

        elif choice == "3":
            account.view_transactions()

        elif choice == "4" and isinstance(account, VIPAccount):
            account.redeem_points()

        elif choice in ["4", "5"]:
            break
        else:
            print("❌ Invalid choice!")

def main():
    print("🏧 WELCOME TO ATM SYSTEM")

    name = input("Enter account holder's name: ")
    balance = float(input("Enter initial balance: "))

    acc_type = input("Choose account type (1. Normal / 2. VIP): ")

    if acc_type == "2":
        account = VIPAccount(name, balance)
        account.receive_ads()
    else:
        account = Account(name, balance)

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Account information")
        print("2. Transactions")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print(f"👤 Name: {account.name}")
            account.view_balance()

        elif choice == "2":
            transaction_menu(account)

        elif choice == "3":
            print("👋 Thank you for using ATM System!")
            break

        else:
            print("❌ Invalid choice!")
