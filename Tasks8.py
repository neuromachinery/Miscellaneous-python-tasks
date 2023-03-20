# Those solutions are my homework for college. 
# I could've added the tasks statements for these solutions,
# but I won't, because I'm lazy and it isn't that important.
# Sorry if you need 'em ¯\_(ツ)_/¯

def ParameterCheck(Params, ParamsNames): # This function checks every parameter for being None. This is needed for Execution system.
	if(Params==None): # special case of single user defined parameter
		print("Enter {} parameter.".format(ParamsNames)) # This message will tell user to enter them correctly
		raise KeyError # Raises exception to be catched later.
	elif(type(Params)==tuple or type(Params)==list):
		for Param in Params:
			if(Param == None): # If any of parameters are None...
				print("Enter {} parameters.".format(" and ".join(ParamsNames))) # This message will tell user to enter them correctly
				raise KeyError # Raises exception to be catched later.
	return True # If all parameters have values then return true

def Task1(): # Im assuming that numbers for function are user defined
	def comparison(A,B):
		if(A>B):
			return A
		else:
			return B
	print("Input A and B for comparison")
	print("Biggest number turned out to be = ", comparison(int(input()),int(input())))
def Task2():
	def square(A):
		return A**2
	print("Input A for multiplying it by itself")
	print("Result = ",square(int(input())))
def Task3():
	def area(A,B,C):
		p = (A+B+C)/2
		return (p*(p-A)*(p-B)*(p-C))**0.5
	print("Input sides of a triangle. One at the time")
	print("Area = ", area(int(input()),int(input()),int(input())))
def Task4():
	def area(r):
		return 3.14*r*r
	print("Input radius of a circle")
	print("Area = ", area(int(input())))
def Task5():
	def parity(number):
		if(number%2==0):
			return True
		else:
			return False
	print("Input number")
	print("Is it even? ",parity(int(input())))
def Task6():
	def listSum(List):
		result = 0
		for number in List:
			result = result + number
		return result
	List = []
	print("Input amount of numbers in a list")
	n = int(input())
	for i in range(0,n):
		print("Input number for first list")
		List.append(int(input()))
	print("Sum: ", listSum(List))
def Task7():
	def listParityCount(List):
		result = 0
		for number in List:
			if(number%2==0):
				result = result + 1
		return result
	List = []
	print("Input amount of numbers in a list")
	n = int(input())
	for i in range(0,n):
		print("Input number for first list")
		List.append(int(input()))
	print("Even count: ", listParityCount(List))
def Task8():
	def stringLadder(string):
		i = 1
		for letter in string:
			print(letter*i)
			i = i + 1
	print("Input string.")
	stringLadder(input())
def Task9():
	def factorial(number):
		result = 1
		for i in range(1,number+1):
			result = result * i
		return result
	print("Input number.")
	print("factorial = ", factorial(int(input())))
def Task10():
	def uniqueMembers(List):
		result = []
		for member in List:
			if(member not in result):
				result.append(member)
		return result
	List = []
	print("Input amount of numbers in a list")
	n = int(input())
	for i in range(0,n):
		print("Input number for first list")
		List.append(int(input()))
	print("Amount of unique numbers: ", uniqueMembers(List))
def Task11():
	def uniqueMembers(List):
		result = []
		for member in List:
			if(member not in result):
				result.append(member)
		return result
	def similarityCheck(List1,List2):
		result = 0
		for member in uniqueMembers(List1): # Im assuming that repetition doesn't count
			if(member in uniqueMembers(List2)):
				result = result + 1
		return result
	List1 = []
	List2 = []
	print("Input amount of numbers in the lists")
	n = int(input())
	for i in range(0,n):
		print("Input number for first list")
		List1.append(int(input()))
	for i in range(0,n):
		print("Input number for second list")
		List2.append(int(input()))
	print("Amount of similar elements: ", similarityCheck(List1,List2))
def Task12():
	def memberWiseSum(List1,List2):
		if(len(List1)!=len(List2)):
			return -1
		result = []
		for index in range(0,len(List1)):
			result.append(List1[index] + List2[index])
		return result
	List1 = []
	List2 = []
	print("Input amount of numbers in the lists")
	n = int(input())
	for i in range(0,n):
		print("Input number for first list")
		List1.append(int(input()))
	for i in range(0,n):
		print("Input number for second list")
		List2.append(int(input()))
	print("Sum: ", memberWiseSum(List1,List2))
###### Execution and task check ######
# How to use:
# 1) Write Task number
# 2) Task may require some params. Enter them next if necessary. 
# 3) If you don't know what requested parameters mean, look them up in corresponding function

def ParamDefinition(): # This function used for defining user defined parameters inside functions. Comes with fool-proof protection!
	try:
		print("Type in the parameters for the task. Separate them with a ',' and put quotes around string parameters")
		try:Params = input()
		except KeyboardInterrupt: # Check for KeyboardInterrupt to exit without exceptions
			print("Exiting...")
			quit()
		exec("Task{}({})".format(Task, Params))
		return False
	except NameError:
		print("Please don't forget quotes around string parameters.")
		return True
	except ValueError:
		print("Enter valid type. (int/str/bool/float/etc...)")
		return True
	except KeyError:
		print("Please type the correct parameters.")
		return True
	except Exception as E: # catch generic exceptions
		print("Something went wrong. Here's exception -> ", E) # and print them out
		return False
	
while(True):
	print("which Task to execute?..")
	try:
		Task = int(input())
	except KeyboardInterrupt: # Check for KeyboardInterrupt.
		print("Exiting...")
		quit()
	except ValueError: # Check for number in input
		print("Please enter valid task numbers. Try again...\n")
		continue
	try:
		print("Executing Task{}".format(Task))
		exec("Task{}()".format(Task)) # Execution of required task
	except KeyError: # For cases when function has parameters
		while(ParamDefinition()):pass # this line executes code that asks user for parameters. If user enters them the wrong way, it asks again.
	except ValueError:
		print("Maybe function had default type and it didn't work. Enter correct type")
		while(ParamDefinition()):pass # Again, but checks for valid type
	except NameError:
		print("This function does not exist. Try again...")
	except Exception as E: # catch generic exceptions
		print("Something went wrong. Here's exception ->", E) # and print them out
	print("\n")