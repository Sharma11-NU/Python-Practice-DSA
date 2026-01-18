"""
1. Student Class (Basic OOP Example)
2. BankAccount Class (Instance Variables)
3. Encapsulation (Private Variables)
4. Advanced BankAccount + Transactions + Multiple Users

"""
#------ STUDENT CLASS-----------
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old"

# Create objects
s1 = Student("abc", 20)
s2 = Student("qwe", 32)

# call the methods
print(s1.introduce())
print(s2.introduce())

#------ BANK ACCOUNT CLASS--------
# ---- Instance Variable ----###
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount("jay", 1000)
account.deposit(500)
account.withdraw(200)

print(account.balance)

# --------- Encapsulation --------------
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, input_password):   # <-- requires 1 argument
        return self.__password == input_password
user = User("divya123", "secret")
print(user.check_password("secret"))  # True
print(user.check_password("wrong"))   # False

# ---------- ADVANCED BANK ACCOUNT -----------------

from datetime import datetime

class BankAccount:
    def __init__(self,user, balance,):
        self.user = user
        self.balance = balance
        self.transactions = []

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            now = datetime.now()
            self.transactions.append(["deposit", amount, self.balance, now.strftime("%Y-%m-%d %H:%M:%S")])

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            now = datetime.now()
            self.transactions.append(["withdraw", amount, self.balance, now.strftime("%Y-%m-%d %H:%M:%S")])
        else:
            print(" not enough to withdraw")

    def get_balance(self):
        return self.balance

class User:
   def __init__(self,name):
       self.name = name
       self.accounts = []

# account → points to BankAccount object

user = User("Abs")
account = BankAccount(user, 100)
user.accounts.append(account)

user1= User(" xyz")
account1 = BankAccount(user1, 100)
user1.accounts.append(account1)

# 5. Print all users and their account balances
users = [user, user1]  # list of all users

acc_num = 0
for u in users:
    print("User:", u.name)
    for acc in u.accounts:
        print(" Account", acc_num, "Balance:", acc.balance)
        acc_num += 1


account.deposit(50)
account.withdraw(80)
account1.withdraw(40)
print(account.balance , account1.balance)        # 150
print(f" {account.transactions}, {account1.transactions}")   # [["deposit", 50, 150]]
