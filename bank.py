# Python Code: Bank Class with Class Variable and Class Method
class Bank:
    # Class variable shared by all instances
    bank_name = "National Bank of Pakistan"
    branches = {"Main Branch" : "Karachi"}

    def __init__(self, account_holder, branch):
        self.account_holder = account_holder  # Instance variable
        self.branch = branch
        self.balance = 0  # Instance variable for account balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.account_holder} deposited {amount}. New balance: {self.balance}")

    def display(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank:{Bank.bank_name}")
        print(f"Branch:{self.branch}")
        print(f"Balance: {self.balance}")

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name
        print(f"Bank name changed to {cls.bank_name}")
    
    @classmethod
    def add_branch(cls,branch_name, location):
        cls.branches[branch_name] = location
        print(f"Branch ' {branch_name}' added at location: {location}")
    
    @classmethod
    def show_branches(cls):
        print("\n --- Bank Branches ---")
        for branch, location in cls.branches.items():
            print(f"{branch} - {location}")

# Add new branches
Bank.add_branch("Lahore", "DHA Lahore")
Bank.add_branch("Islamabad", "DHA Islamabad")

# Display all branches
Bank.show_branches()

# Create two Bank accounts
acc1 = Bank("Ali Zafar", "Main Branch")
acc2 = Bank("Sara Khan", "Lahore")

# Deposit money into accounts
acc1.deposit(1000)
acc2.deposit(10000)

# Display initial bank names
acc1.display()
acc2.display()


# Change the bank name using the class method
Bank.change_bank_name("Bank Alfalah limited")

# Display updated bank names
acc1.display()
print()
acc2.display()




