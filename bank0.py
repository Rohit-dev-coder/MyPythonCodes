import sys
class Bank(object):
	def __init__(self,name,bal = 0.0):
		self.name = name
		self.balance = bal
	def showAmt(self):
		return self.balance
	def deposite(self, amount):
		self.balance += amount
		return self.balance
	def withdraw(self, amount):
		if amount > self.balance:
			print("Balance AMount is less, So no Withdrawal")
		else:
			self.balance-=amount
		return self.balance
name = input("Enter Name: ")
b = Bank(name)
while (True):
	print('\n\ns -ShowBalance, d -Deposite, w -Withdraw, e -Exit')
	choice = input('your Choice:').lower()
	if choice == 'e':
		sys.exit()
	if choice == 'd':
		amt = float(input("Enter Amount: "))
		print("Balance after Deposite: ",b.deposite(amt))
	elif choice == 'w':
		amt = float(input("Enter Amount: "))
		print("Balance after Withdrawal: ",b.withdraw(amt))
	elif choice == 's':
		print("{} your Account Balance is {}".format(name,b.showAmt()))