import os
import ast


base_path = "data/users/"

def create_user(email, data):
	try:	
		if(user_exist(email)):
			print("User already Exist. Please Use Another Email")
			return False
		else:
			with open(base_path+email+".txt", "w") as f:
				f.write(str(data))
				print("User Created Succesfully")
				return True
	except:
		delete_user(email)
		print("Something went wrong please try again")
		return False


def update_user(email, data):
	try:
		if(user_exist(email)):
			with open(base_path+email+".txt", "w") as f:
				f.write(str(data))
				print("User Updated Succesfully")
				return True

		else:
			print("User Not Found")
			return False
	except:
		print("something went wrong")
		return False


def delete_user(email):
	try:
		if(user_exist(email)):
			os.remove(base_path+email+".txt")
			print("User Deleted")
			return True
		else:
			print("User Not Found")
			return False
	except:
		print("Something went wrong please try again")
		return False



def read(email):
	if(user_exist(email)):
		with open(base_path+email+".txt", "r") as f:
			raw_data = f.read()
			return ast.literal_eval(raw_data)
	return False



def user_exist(email):
	return os.path.exists(base_path + email + ".txt")


def login(email, password):
	try:
		if(user_exist(email)):
			user = read(email)
			if user['password'] == password:
				return user
		return False
	except:
		print("Something went wrong please try again")
		return False




dummy_data = {
		"first_name": 'first_name',
		"last_name": 'last_name',
		"password": 'password',
		"account_number": 1234567890,
		"email": 'a@a.com',
		"balance": 0
	}

data_2 = {
	"first_name": 'first',
	"last_name": 'last',
	"password": 'pass',
	"account_number": 1234567890,
	"email": 'a@a.com',
	"balance": 0
}

# data = read("e@a.com")
# create_user("e@a.com", dummy_data)
delete_user("e@a.com")
# update_user("e@a.com", data_2)
# details = login("e@a.com", 'pass')

# print(details)




