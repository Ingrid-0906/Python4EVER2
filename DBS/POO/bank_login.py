""" Parent class: User
	holds deatils about an user
	has a function to show user details

	Child class: Bank
	stores detials about the account balance, amount deposits withdraw and view_balance
"""

# Class Parent: User. Login and Details about user
class login(object):
	"""docstring for login"""
	def __init__(self, user, password):
		self.user = user
		self.password = password
		if self.user == '123' and self.password == '123':
			print('Logged Successfully!')
			self.personal_details()
		else:
			print('Logged Out.')
			self.delete()


	def personal_details(self):
		# i needed to a database...

		self.name = 'Ingrid Cards'
		self.age = '27 Years Old'
		self.gender = 'Female'
		settings = input('Hello! {}. Confirm these info? {} and {}? Press 1 - Yes and 2 - No '.format(self.name, self.age, self.gender))

		if settings == '1':
			print('Confirmed.')
		else:
			print('Logged Out.')
			self.delete()


	def delete(self):
		def __del__(self):
			print('Failed Try.')

class Bank(object):
	"""docstring for Bank"""
	def __init__(self):
		option = input('1- balance / 2- withdraw ')
		if option == '1':
			self.balance()
		else:
			self.withdraw()
		
	def balance(self):
		print('balance')

	def withdraw(self):
		print('withdraw')


# Log in system
User = input('User: ')
Pass = input('Password: ')

# pass to classes
you = login(User, Pass)

# enter in the bank system
banks = Bank()
