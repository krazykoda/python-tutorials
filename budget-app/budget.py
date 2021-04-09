
#budget class app

class Budget:
	def __init__(self, name, bal):
		self.name = name
		self.balance = bal

	def deposit(self, amt):
		try:
			self.balance += amt
			print(f"{amt} deposited to {self.name} successfully")
			self.check_balance()
		except TypeError:
			print("Amount should be an integer")
		except:
			print("something went wrong")



	def withdraw(self, amt):
		try:
			self.balance -= amt
			print(f"Made a withdrawal of {amt} from {self.name}")
			self.check_balance()
		except TypeError:
			print("Amount should be an integer")
		except:
			print("something went wrong")



	def check_balance(self):
		try:
			print(f"Current balance for {self.name} is: {self.balance}")
			return self.balance
		except TypeError:
			print("Amount should be an integer")
		except:
			print("something went wrong")



	def transfer(self, budget, amt):
		try:
			if(self.balance > amt):
				budget.deposit(amt)
				self.balance -= amt
				print(f"{amt} transfered to {budget.name} from {self.name} successfully")
				self.check_balance()
			else:
				print('Not enough balance to make transfer')
		except TypeError:
			print("Amount should be an integer")
		except:
			print("something went wrong")


food = Budget("food", 1000)
clothes = Budget('clothes', 500)

clothes.check_balance()
clothes.deposit(1000)
clothes.withdraw(400)
clothes.transfer(food, 100)
food.check_balance()

#test exception
print("="*10, " test error ", '='*10)
food.withdraw('100')


# print('budget1', food.balance)
# print('budget2', clothes.balance)

