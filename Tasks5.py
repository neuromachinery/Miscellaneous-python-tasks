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

def Task1(N=None): # Task did not specify the domain of the number, but because of floating point numbers the task becomes impossible, I assume N being integer
	ParameterCheck((N),("integer")) 
	for number in range(0,N):
		if(number%3==0):print(number)
def Task2(N=None): # Similarly to Task 1, floating point is impossible.
	ParameterCheck((N),("integer"))
	for number in range(0,N):
		if(number%3==0 or number%7==0):print(number)
def Task3(N=None): # Similar problem to previous tasks
	ParameterCheck((N),("integer"))
	result = int()
	for number in range(1,N):
		if(number%2==0):
			result = result + number
	print(result)
def Task4(N=None): # Similar problem to previous tasks
	ParameterCheck((N),("integer"))
	result = 1
	for number in range(1,N):
		result = result + 1/number
	print(result)
def Task5(N=None): # Similar problem to previous tasks
	ParameterCheck((N),("integer"))
	result = 1
	for number in range(1,N):
		result = result + 2**number
def Task6(N=None): # I found another way of implementing this problem, so I did both 
	ParameterCheck((N),("integer"))
	result = int()
	for number in range(1,N):
		result = result + float("1.%s"%number)
	result = int()
	for number in range(1,N):
		result = result + (1+0.1*number)
	print(result)
def Task7(N=None):
	ParameterCheck((N),("integer"))
	result = int()
	for number in range(1,N):
		if(number%2==0):
			result = result - float("1.%s"%number)
		else:
			result = result + float("1.%s"%number)
	print(result)
def Task8(N=None):
	ParameterCheck((N),("integer"))
	result = int()
	for number in range(1,N):
		result = result * number
	print(result)
def Task9(N=None):
	ParameterCheck((N),("integer"))
	result = str(1)
	print(result)
	for number in range(2,N+1):
		result = result + str(number)
		print(result)
def Task10(N=None):
	ParameterCheck((N),("integer"))
	for number in range(1,N+1):
		print(str(number)*number)
def Task11(N=None, K=None):
	ParameterCheck((N, K),("integer", "integer"))
	result = int()
	for number in range(N,K):
		result = result + number
	print(result//len(range(N,K)))
def Task12(N=None, K=None, Mode=1):
	ParameterCheck((N, K),("integer", "integer"))
	if(Mode==1):# There is more concise way of doing it, but the task required importing math.sqrt. So I did both through modes. Mode 1 is the one with import
		from math import sqrt
		print(sqrt(K*N))
	else:
		print((K*N)**0.5) 
def Task13(N=1, K=None):
	ParameterCheck((N, K),("integer", "integer"))
	spaceDict = {}
	for i in range(1,len(str(K*K))+1): # This dictionary generator makes dictionary that tells how much spaces needed for a given lenght of largest element
		spaceDict[i] = range(1,len(str(K*K))+1)[-i]
	for row in range(N,K+1):
		for column in range(N,K+1):
			print(column*row, end=" "*spaceDict[len(str(column*row))]) # This line prints results with regard to spacing between numbers
		print()
def Task19(N=1, K=None):
	ParameterCheck((N, K),("integer", "integer"))
	for row in range(N,K+1):
		for column in range(N,K+1):
			Result = column%row - row%column
			print(Result, end=" "*((len(str(K*K))+1)-len(str(Result)))) # This line prints results with regard to spacing between numbers
		print()
def Task20():
	n,k=1,13
	for i in range(n,k+1):
		for j in range(n,k+1):
			print(i*j, end=" ")
		print()
def Task14(N=1, K=None):
	ParameterCheck((N, K),("integer", "integer"))
	spaceDict = {}
	for i in range(1,len(str(K*K))+1): # It's exactly the same generator
		spaceDict[i] = range(1,len(str(K*K))+1)[-i]
	for row in range(N,K+1):
		for column in range(N,K+1):
			print("{result}{space1}= {row}{space2}* {column}\n".format(
				result=row*column,
				space1=" "*spaceDict[len(str(column*row))],
				space2=" "*spaceDict[len(str(row))],
				row=row,
				column=column,
				))
		print("\n")
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