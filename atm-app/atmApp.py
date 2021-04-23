from datetime import datetime
import random
import db

current_user = None

def init():
	print("Welcome To My ATM")
	print("1. Login \n2. Register \n3. Cancel")
	print()

	selection = int(input("Select option: "))

	if(selection == 1):
		login()
	elif(selection == 2):
		register()
	elif(selection == 3):
		print("See you soon, bye!")
	else:
		init()



def login():
	global current_user
	try:
		email = input("Enter email: ")
		password = input("Enter password: ")

		user = db.login(email, password)

		if(user):
			current_user = user
			print(f"Welcome {current_user['first_name']}")
			print(f"Current time is {datetime.now().strftime('%c')}")
			operations()
		else:
			print("Invalid email or password")
			print()
			init()
	except:
		print("something went wrong")


# update the state of the current user after a change is made
def update_user(email):
	global current_user
	try:
		user = db.read(email)
		if user:
			current_user = user
	except:
		print("something went wrong")


def logout():
	current_user = None
	init()



def register():
	global current_user
	try:
		email = input("Enter your email: ")
		first_name = input("Enter your first name: ")
		last_name = input("Enter your last name: ")
		password = input("Enter your password: ")
		acc_num = account_number()

		new_user = {
			"first_name": first_name,
			"last_name": last_name,
			"password": password,
			"account_number": acc_num,
			"email": email,
			"balance": 0
		}

		created = db.create_user(email, new_user)

		if(created):
			current_user = new_user
			print(f"Welcome {current_user['first_name']}")
			print(f"Current time is {datetime.now().strftime('%c')}")
			operations()
		else:
			init()
	except:
		print("something went wrong")


def account_number():
	actNum = random.randrange(1111111111,9999999999)
	return actNum


def withdraw():
	try:
		amount = int(input("How much will you like to withdraw? "))
		if(current_user['balance'] > amount):
			current_user['balance'] -= amount 
			updated = db.update_user(current_user['email'], current_user)
			if updated:
				update_user(current_user["email"])
				print("Here is your cash")
				print("current balance is %d" % current_user['balance'])
			operations()
		else:
			print("Not enough balance")
			operations()
	except:
		print("something went wrong")


def deposit():
	try:
		amount = int(input("How much will you like to deposit? "))
		current_user['balance'] += amount 
		updated = db.update_user(current_user['email'], current_user)
		if updated:
			update_user(current_user['email'])
			print("current balance is %d" % current_user['balance'])
		operations()
	except:
		print("something went wrong")


def complaint():
	try:
		complaint = input("What issue do you want to report? ")
		print("Thanks for contacting us")
		operations()
	except:
		print("something went wrong")


def checkBalance():
	try:
		print("current balance is %d" % current_user['balance'])
		operations()
	except:
		print("something went wrong")


def delete_account():
	try:
		print()
		print("Are you sure u want to delete your account?")
		print("1. Yes \n2. No ")
		print()

		selection = int(input("Select an option: "))

		if(selection == 1):
			deleted = db.delete_user(current_user["email"])
			if deleted:
				print("Hope to see you again soon")
		else:
			operations()
	except:
		print("Something went wrong")



def operations():
	if(current_user):
		print()
		print("ATM operations")
		print()
		print("1. Withdraw")
		print("2. Deposit")
		print("3. Complaint")
		print("4. Check Balance")
		print("5. Logout")
		print("6. Delete Account")
		print()

		selection = int(input("What do you want to do? "))

		if(selection == 1):
			withdraw()
		elif(selection == 2):
			deposit()
		elif(selection == 3):
			complaint()
		elif(selection == 4):
			checkBalance()
		elif(selection == 5):
			logout()
		elif(selection == 6):
			delete_account()
		else:
			operations()
	else:
		init()



# start App
init()