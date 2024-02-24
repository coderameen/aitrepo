class BankManagementSystem:
    #constractor
    def __init__(self):
        self.acc_no = None
        self.acc_holder = None
        self.balance = 0

    #creating user in bank
    def new_user(self,acc_no,acc_holder,amount):
        self.acc_no = acc_no
        self.acc_holder = acc_holder
        self.balance = amount
        print(f"{self.acc_holder} has been created successfully!!")

    def display_balance(self):
        print(f"The Account No: {self.acc_no} | Account Holder: {self.acc_holder} | Available Balance: {self.balance}")

    def withdraw_amount(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} has been withdraw succesfully!!")
        else:
            print("Insuffient balace!!")

    def credit_amount(self,acc_holder,amount):
        if acc_holder == self.acc_holder:
            self.balance += amount
            print(f"{amount} has been credited!!")
        else:
            print("Invalid user!!")
    def update_acc_holder(self,new_holder):
        self.acc_holder = new_holder
        print(f"{new_holder} has been updated !!")

c1 = BankManagementSystem()
c1.new_user('101','alen',1000)
c1.display_balance()
c1.withdraw_amount(700)
c1.display_balance()
c1.credit_amount('alen',2000)
c1.display_balance()
c1.update_acc_holder('alen walker')
c1.display_balance()
