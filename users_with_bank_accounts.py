# Users with Bank Accounts Assignment - Gregg Bowen

# Create a User class with an __init__ method (Done)

# Add a make_deposit method to the User class that calls on it's bank account's instance methods. (Done)

# Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.

# Add a display_user_balance method to the User class that displays user's account balance

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.


class User: 
    all_users = []
    
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(first_name=first_name, last_name=last_name, email=email, age=age)
        User.all_users.append(self)

    def display_info(self):
        print("First Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Rewards Member:", self.is_rewards_member)
        print("Gold Card Points:", self.gold_card_points)
        print("Bank Account:", self.account.display_account_info())

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
            return True
        else:
            print("User already a member")
            return False

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points -= amount
            return self.gold_card_points
        else:
            print("Insufficient points.")

    def make_deposit(self,amount):
        self.account.balance += amount
        return self

    def make_withdraw(self,amount):
        self.account.balance -= amount
        return self
    
    def display_user_balance(self):
        print("User Balance:", self.account.balance)
        return self
    
    def transfer_to_friend(self, user, amount):
        self.account.balance -= amount
        user.account.balance += amount
        return self


class BankAccount:
    bank_name = "Big Money Bank"
    all_accounts = []
    
    def __init__(self, first_name, last_name, age, email): 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.int_rate = 0.01
        self.balance = 100
        BankAccount.all_accounts.append(self)

#The below deposit and withdraw methods are redundant because I have already created similar functions from the User class method
#that calls upon an instance with the Bank account to make the withdraw or deposit.

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self):
        self.balance -= amount
        return self

    def display_account_info(self):
        print("-------------------")
        print("Bank:", self.bank_name)
        print("Name:", self.first_name, self.last_name)
        print("Age:", self.age)
        print("Account Balance:", round(self.balance, 2))
        print("Account Interest Rate:", self.int_rate)
        print("-------------------")
        return self

    def yield_interest(self):
        self.balance = (1 + self.int_rate) * self.balance
        return self

#Below are the users for my User class, which is also used in creating a bank account by inserting the info into the 
#bank account instance in my User init method.

user1 = User("Tom", "Merrilin", "wheeloftime@legend.com", 55)
user2 = User("Rand", "Althor", "dragonmount@legend.com", 20)
user3 = User("Mat", "Cauthon", "wolfnecklace@legend.com", 21)

# Assignment Action:
user1.make_deposit(120).display_info()
user1.make_withdraw(15).display_info()
user1.display_user_balance()

#SENSEI BONUS:
user1.transfer_to_friend(user2,40)
user1.display_info()
user2.display_info()
