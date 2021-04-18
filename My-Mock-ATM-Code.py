# Function to initialize app
def init():
	print("Welcome to YourBank.")
	entry = int(input("\nDo you already have an account with us? \n(1) Yes\n(2) No\n"))
	if (entry == 1):
		login()
	elif (entry == 2):
		register()
	else:
		print("You have entered an invalid input\n")
		init()

# Creating a dictionary to store user data and a function to generate account number for user
dict = {}
def GenerateAccNum():
	import random
	return random.randrange(1111111111, 9999999999)
AccNum= GenerateAccNum()

# Creating a login function
def login():
	LogIn= True
	while LogIn== True:
		AccNumUser = int(input ('Please enter your account number: \n'))
		password = input ('Please enter your password: \n')
		for AccNum,UserDetails in dict.items():
			if (AccNum == AccNumUser):
				if (UserDetails[2] == password):
					bankOperations()
			LogIn= False
		print("You have entered an invalid account number or password. Please try again.")
		init()

# Creating a register function
def register():
		firstName= input("Please enter your first name:\n")
		lastName= input("Please enter your last name:\n")
		Password = input("Please enter your preferred password:\n")
	
		dict [AccNum] = [firstName, lastName, Password]
		
		print("An account has now been created for you.")
		print("Your Account Number is: ", AccNum)
		print("Your preferred password is: ", Password)
		print("Keep your credentials safe. You may now proceed to login.")
		
		print("**** **** **** ****")
		login()

# Creating a logout function
def logout():
	print("You have been logged out.\n")
	logging()

# Creating a function that prompts the user to login again or not
def logging():
	Retry = int(input("Do you want to login again? \n(1) Yes\n(2) No\n"))
	if (Retry == 1):
		login()
			
	elif (Retry == 2):
		exit()
			
	else:
		print("You have entered an invalid input")
		logging()								

# Creating a function that presents the user with options of the bank operations
def Options():

	print('\nThese are the available options:\n')

	print('1. Cash Withdrawal')
	print('2. Cash Deposit')
	print('3. Complaints')
	print('4. Logout')
	print('5. Exit')

	selectedOption= int(input('\nPlease select an option: '))

	if (selectedOption== 1):
		withdrawal()

	elif (selectedOption== 2):
		deposit()

	elif (selectedOption== 3):
		complaints()

	elif (selectedOption== 4):
		logout()

	elif (selectedOption== 5):
		exit()

	else:
		print('\nInvalid option selected. Please try again.')
		Options()

# Creating a function that prompts the user whether to perform the bank operations again or not
def Prompt():
		Response= int(input('\nWant to perform another operation?\n(1) Yes\n(2) No\n'))
		if (Response == 1):
			Options()
		elif (Response == 2):
			logout()
		else:
			print("You have entered an invalid input. Please try again.")
			Prompt()

# Creating a function for the bank withdrawal operation
def withdrawal():
	withdrawAmount= input('\nHow much would you like to withdraw? ')
	print('\nTake your cash')		
	Prompt()

# Creating a function for the bank deposit operation
def deposit():
	depositAmount= input('\nHow much would you like to deposit? ')
	print('\nYour current balance is %s' %(depositAmount))
	Prompt()

# Creating a function for the bank complaints operation
def complaints():
	complaintEntry= input('\nWhat issue will you like to report? ')
	print('\nThank you for contacting us.')
	Prompt()

# Creating a function that initializes the bank operations
def bankOperations():
	import datetime
	now= datetime.datetime.now()
	for AccNum,UserDetails in dict.items():
	
		print ('\nWelcome, %s %s.  You have been logged in at time' %(UserDetails[0], UserDetails[1]), 
			now.strftime("%H:%M:%S"), ', on this day:', now.strftime("%d-%m-%Y "))
	Options()

init()
		
	

	
