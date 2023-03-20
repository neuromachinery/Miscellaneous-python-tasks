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

def Task1(Amount=None): 
	ParameterCheck((Amount),("amount of numbers"))
	List = []
	for i in range(Amount):
		print("Input number...")
		List.append(input())
	print(List) # Task did not required output. Did anyway
	return List # Task 3 and 4 required output.
def Task2(Amount=None): #functionally identical.
	ParameterCheck((Amount),("amount of numbers"))
	List = []
	for i in range(Amount):
		print("Input name...")
		List.append((input()))
	print(List)
	return List
def Task3(Amount=None):
	ParameterCheck((Amount),("amount of numbers"))
	List = Task1(Amount)
	for index in range(0,len(List)):
		if(index%2!=0):
			print(List[index])
def Task4(Amount=None):
	ParameterCheck((Amount),("amount of numbers"))
	for number in Task1(Amount):
		if(int(number)%2==0):
			print(number)
def Task5(List=None):
	ParameterCheck((List),("List of numbers. For example [0,1,2]"))
	result = List[0]
	for number in List:
		if(number>result):
			result = number
	print(result)
def Task6(List=None):
	ParameterCheck((List),("List of numbers. For example [0,1,2]"))
	result = List[0]
	for number in List:
		if(number<result):
			result = number
	print(result)
def Task7(List=None):
	ParameterCheck((List),("List of numbers. For example [0,1,2]"))
	result = 0
	for number in List:
		result = result + number
	print(result)
def Task8(List=None):
	ParameterCheck((List),("List of numbers. For example [0,1,2]"))
	result = 0
	for number in List:
		result = result + number
	print(result/len(List))
def Task9(Amount=None):
	ParameterCheck((Amount),("amount of numbers"))
	result = ""
	for name in Task2(Amount):
		if(len(name)>len(result)):
			result = name
	print(result)
def Task10():
	List = []
	print("Input range lower bound...")
	a = int(input())
	print("Input range upper bound...")
	b= int(input())
	for number in range(a,b,2):
		List.append(number+1)
	print(List)
def Task11():
	List = []
	print("Input range lower bound...")
	a = int(input())
	print("Input range upper bound...")
	b= int(input())
	for number in range(a,b):
		List.append(number**2)
	print(List)
		
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