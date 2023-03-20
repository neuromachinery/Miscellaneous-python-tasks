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

#def Task1(A=None,B=None): 
#	ParameterCheck((A,B),("A","B")) 
def Task1():
	List = []
	for number in [1, 4, 9, 16]:
		List.append(number)
	#List = [1, 4, 9, 16] # Just in case this line was required
	List.pop()
	print(List)
	List[0] = -1
	List.remove(4)
	print(List)
def Task2():
	List = []
	print("Input N...")
	N = int(input())
	for i in range(N):
		print("Input number...")
		List.append(input())  #It is not clear when the conversion happens.
		#List.append(int(input()))  #This way is better,
	for index in range(len(List)): # But I guess Task requires this strict order of operations.
		List[index] = int(List[index])
	print(List) # Once again, output was not required
def Task3():
	List = []
	print("Input N...")
	N = int(input())
	for i in range(N):
		print("Input number...")
		List.append(input()) 
		#List.append(int(input())) # Almost identical implementation
	result = int(List[0])
	for index in range(len(List)): 
		List[index] = int(List[index])
		if(int(List[index])>result):
			result = int(List[index])
	print(result) 
def Task4():
	List = []
	print("Input N...")
	N = int(input())
	for i in range(N):
		print("Input number...")
		List.append(input()) 
		#List.append(int(input())) # Almost identical implementation
	result = []
	for index in range(len(List)): 
		List[index] = int(List[index])
		if(int(List[index])<10):
			result.append(int(List[index]))
	print(result)
def Task5(Size=None): # Size of list was not specified.
	ParameterCheck((Size),("size of list")) 
	List = []
	from random import randint
	for i in range(Size):
		n = randint(0, 10)  # Preserved original Task implementation
		List.append(n)
	print(List)
	result = 0
	for number in List:
		result = result + number
	print(result/len(List))
def Task6():
	List = []
	print("Input N...")
	N = int(input())
	for i in range(N):
		print("Input string...")
		List.append(input()) 
	result = ""
	for string in List: 
		if(len(string)>len(result)):
			result = string
	print(result)
def Task7():
	List = []
	print("Input N...")
	N = int(input())
	for i in range(N):
		print("Input string...")
		List.append(input()) 
	result = 0
	for string in List: 
		if(string.find("o")!=-1 or string.find("о")!=-1): # unfortunatly, latin o and russian о are identical. Of course Im doing both
			result = result + 1
	print(result)
def Task8():
	List = []
	print("Input N...")
	N = int(input())
	for i in range(N):
		print("Input number...")
		List.append(input())  
		#List.append(int(input()))  
	for index in range(len(List)): 
		List[index] = int(List[index])
	result = List[0]
	Largest = 0
	for number in List:
		if(List.count(number)>Largest):
			Largest = List.count(number)
			result = number
	print(result)
def Task9():
	List = []
	print("Input N...")
	N = int(input())
	for i in range(N):
		print("Input number...")
		List.append(input())  
		#List.append(int(input()))  
	UniqueList = [] # It is not clear what "unique" means. I assume it's a list of elements from previous list without repetitive values
	for index in range(len(List)): 
		List[index] = int(List[index])
		if(List[index] not in UniqueList):
			UniqueList.append(List[index])
	print(List,"\n",UniqueList)
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
	except KeyboardInterrupt:
		print("Exiting...")
		quit()
	except Exception as E: # catch generic exceptions
		print("Something went wrong. Here's exception ->", E) # and print them out
	print("\n")