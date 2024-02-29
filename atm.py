'''the below is simple atm project it is developed by upcoming developer C.MUTHUPANDIYAN,yeah let's go the code'''
'''HERE I ONLY USE CONDITION STATEMENTS AND OOPS CONCEPTS'''

class ATM:#class 
    def __init__(self):#initazling the instant variable"
        self.available=4000
    def display(self):#here,give the option to the customer .what kind need they want?
        print("welcome to our atm ")
        print("please enter what you want")
        print("If you want withdraw please enter no:1")
        print("If you want deposit please enter no:2")
        print("If you want see current balance please enter no:3")
        print("If you want others transaction please enter no:4")
        print("--------------------------------------------------")
        get_input=input("enter your option:")# get a input for the option
        if get_input=="1":#if the option 1 the execution go to withdraw  method
           self.withdraw()
        elif get_input=="2":
            self.deposit()
        elif get_input=="3":
            self.balance_check()
        elif get_input=="4":
            self.other_transaction()
        print("DO YOU CONTINUE YOUR TRANSACTION")
        option=input()#it is if they want more option which means continue with atm 
        if option=="yes":
            self.display()
        elif option=="no":
            print("thank you")
    def withdraw(self):
        print("Enter your withdraw amount")
        withdraw_amount=int(input())
        if withdraw_amount>=self.available:#it is gonna be check withdraw is greater than available balance
            print("SORRY,you don't enough money in your amount")
        elif withdraw_amount<self.available:
            self.available=self.available-withdraw_amount
            print("your current balance amount:",self.available)
    def deposit(self):
        print("enter your deposit amount:")
        deposit_amount=int(input())
        self.available=self.available+deposit_amount
        print("your amount is deposit successfully")
        print("your current balance",self.available)
        
    def balance_check(self):
        print("your account balance",self.available)
    def other_transaction(self):
        self.display()
bank=ATM()# create object for the class
bank.display()#it is call the function inside the class

        
            
            
