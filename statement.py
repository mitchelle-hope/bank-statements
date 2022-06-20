from datetime import datetime
class Account:
    def __init__(self,name,idnumber):
        self.name=name
        self.balance=0
        self.transaction_cost = 100
        self.idnumber=idnumber
        self.deposits = []
        self.withdraws = []
        self.loan_balance=0

    def deposit(self,amount):
        if amount < 0:
            return f"Deposit must be greater than zero"
        else:
            self.balance+=amount
            date=datetime.now()
            depo={"date": date.strftime('%x'),"amount": amount, "narration":f"you deposited{amount} on {date.strftime('%x %X')}"}
            self.deposits.append(depo)
            return f"Hello your have deposited Ksh {amount} and your new balance is {self.balance} on {date.strftime('%x')}"  
    
    def withdraw(self,amount):
        withdrawable_amount=self.balance-self.transaction_cost
        if amount>withdrawable_amount:
          return f"You have insufficient balance" 
        elif amount <=0:
            return f"Your amount should be greater zero" 
        else:
            self.balance-=amount+self.transaction_cost
            date=datetime.now()
            withd={"date": date.strftime('%x'),"amount": amount, "narration":f"you withdrew {amount} on {date.strftime('%x %X')}"}
            self.withdraws.append(withd)
            return f"Hello {self.name} you have withdrawn {amount} your new balance is {self.balance}"  

    def deposits_statement(self):
        for statements in self.deposits:
            print(statements)
    def withdraws_statement(self):
        for statements in self.withdraws:
            print(statements)
    def current_balance(self):
        balance=self.balance
        print(balance)
    def full_statement(self):
        states=self.deposits+self.withdraws
        for a in states:
            if a in self.deposits:
                print(f"{a['date']}...Deposit...{a['amount']}")
            elif a in self.withdraws:
                 print(f"{a['date']}...Withdrawal...{a['amount']}")

    def borrow (self,amount):
        total_deposit=0
        for a in self.deposits:
            total_deposit+=a["amount"]
        if amount<=0:
            return "invalid amount"
        elif len(self.deposits)<10:
            return f"you can't borrow money, make {10-len(self.deposits)} more deposits to qualify"
        elif amount<100:
            return "you can only borrow at least 100"
        elif self.balance !=0:
            return f"you have{self.balance}in your account.you are not eligible to borrow money." 
        elif amount>total_deposit/3:
            return f"you are not qualified to borrow{total_deposit/3}"  
        if self.loan_balance!=0:
            return f"you have unapaid  loan of {self.loan_balance},first clear the loan you have to be eligible"
        else:
            interest=(3/100)*amount
            self.loan_balance+=amount+interest
            return f"you have borrowed {amount} and your loan balance to be paid is {self.loan_balance}"

    def loan_repayment(self,amount):
        if amount<=0:
            return "invalid amount"
        if amount>self.loan_balance:
            remainder=amount-self.loan_balance
            self.loan_balance=0
            return f"Your loan balance is {self.loan_balance} { self.deposit(remainder)}"
        else:
            self.loan_balance-=amount
            return f"You have paid a loan of {amount} and your current loan balance is {self.loan_balance} "        

    def transfer(self,amount,instance_name):
        if amount<=0:
            return "invalid amount"
        elif amount>=self.balance:
            return "insufficient amount"
        else:
            self.balance-=amount
            instance_name.balance+=amount
            return f"You have transfered {amount} to account with the name of {instance_name.name}. Your new balance is {self.balance}"

