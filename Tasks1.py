# Those solutions are my homework for college. 
# I could've added the tasks statements for these solutions,
# but I won't, because I'm lazy and it isn't that important.
# Sorry if you need 'em ¯\_(ツ)_/¯

def ParameterCheck(Params, ParamsNames): # This function checks every parameter for being None. This is needed for Execution system.
	for Param in Params:
		if(Param == None): # If any of parameters are None...
			print("Enter {} parameters.".format(" and ".join(ParamsNames))) # This message will tell user to enter them correctly
			raise KeyError # Raises exception to be catched later.
	return True # If all parameters have values then return true

# 1. 
# I don't understand what "Experiment" means, but I'll try anyway
def Task1():
	print("Enter something to convert it...")
	Input = input()
	def Convert(Type, Value): # This function returns converted value and it's type after conversion bundled in a tuple 
		try: return(Type(Value), type(Type(Value)))
		except:
			return "Conversion throws exception. ¯\_(ツ)_/¯"
	def IterativeConversion(ListOfTypes,Value): # This function just...
		for Type in ListOfTypes: #... iterates over given list of types...
			print("... to '{}' -> {}".format(Type.__name__, Convert(Type,Value))) #... and tries to convert given value to iterated type. 
	print("The type of our input -> ", type(Input))
	print("Let's try converting it...")
	IterativeConversion((int,str,list,float,bool),Input) # Iterate over some basic types.

# 2. 
def Task2():
	print("Enter your credentials. First of all, your name...")
	Name = input()
	print("... and now your last name...")
	LastName = input()
	print("Hello, {} {}! Hopefully I'll remember you...".format(Name, LastName))

# 3.
# There is two possible ways of entering 3 numbers. Separatly, and with a single entry. I'll do both cases
def Task3(Version=None, Separator=None): # Both cases can be executed using 'Version' parameter. 'Separator' used in second case.
	ParameterCheck((Version,Separator),("Version","Separator"))
	if(Version==1): # Case for entering 3 numbers separatly
		Sum = int()
		for i in range(0,3): 
			print("Input number to sum...")
			Sum = Sum + int(input())
		print(Sum) # Task did not requested output, but I think it's supposed to output result.
	elif(Version==2): # Case for a line of numbers, separated by common separator
		Sum = int()
		print("Input numbers to sum. Separate them with '{}'".format(Separator))
		Input = input()
		Numbers = Input.split(Separator) # this line splits Input line in a list of numbers using common separator between them
		#if(len(Numbers)>3):
		#	while(len(Numbers>3)):
		#		Numbers.pop(-1)
		# Uncomment previous 3 lines if it is necessary to only sum 3 numbers and no more.
		for Number in Numbers:
			Sum = Sum + int(Number) 
		print(Sum) # Again, task did not requested output.

# 4.
# Since Task 3 and Task 4 are ultimatly the same, I'll just adapt the code to accept any type requested.
def Task4(Version=None, Separator=None, Type:type=int): # Type parameter used for converting input. Defaults to integer
	ParameterCheck((Version, Separator),("Version","Separator"))
	if(Version==1): # Case for entering 3 numbers separatly
		Sum = Type() # Variable 'Sum' initialization uses requested Type.
		for i in range(0,3): 
			print("Input number to sum...")
			Sum = Sum + Type(input()) # Type() tries to convert input to requested type and then adding it to the sum 
		print("Sum equals ", Sum) # Task did not requested output, but I think it's supposed to output result.
	elif(Version==2): # Case for a line of numbers, separated by common separator
		Sum = Type() # Variable 'Sum' initialization uses requested Type.
		print("Input numbers to sum. Separate them with '{}'".format(Separator))
		Input = input()
		Numbers = Input.split(Separator) # this splits Input line in a list of numbers using common separator between them
		#if(len(Numbers)>3):
		#	while(len(Numbers>3)):
		#		Numbers.pop(-1)
		# Uncomment previous 3 lines if it is necessary to only sum 3 numbers and no more.
		for Number in Numbers:
			Sum = Sum + Type(Number) # Conversion to type and addition
		print("Sum equals ", Sum) # Again, task did not requested output.

# 5.
def Task5(Variant=1, Number=10): # I don't sure which implementation is requested, so I did both. Accessed through 'Variant' parameter
	# Initial nuber is a parameter, so it can be changed later.
	if(Variant==1):
		print("Number before {} is {}".format(Number, Number-1))
		print("Number after {} is {}".format(Number, Number+1))
		print("###### Translation bridge / Мост перевода ######")
		print("Число предшествующее числу {} равно {}".format(Number, Number-1))
		print("Число следующее за числом {} равно {}".format(Number, Number+1))
	elif(Variant==2):
		print("Number before ", Number, "is ",Number-1)
		print("Number after ", Number, "is ",Number+1)
		print("###### Translation bridge / Мост перевода ######") # Output contains both languages, if either of them required
		print("Число предшествующее числу ", Number, "равно ",Number-1)
		print("Число следующее за числом ", Number, "равно ",Number-1)

# 6.
def Task6():
	print("Enter your name...")
	Name = input()
	print("... and your age...")
	Age = input()
	print("Hello, {}! Your age is {}!".format(Name,Age))
	print("###### Translation bridge / Мост перевода ######") # Output contains both languages, if either of them required
	print("Привет, {}! Ваш возраст равен {}!".format(Name,Age))

# 7.
def Task7(Type:type=int): # I added support for non-integer X
	def MathematicalTask(x):
		result = x*x - 10*x + 15 # this equation can be changed if needed
		return result
	print("x*x - 10*x + 15. Input x...")
	Input = input()
	print("The result = ",MathematicalTask(Type(Input)))

# 8.
def Task8(A=None,B=None): # A and B are parameters, so they are user defined.
	ParameterCheck((A, B),("A","B"))
	from math import sqrt
	print("cathets A and B are {} and {}, respectively...".format(A,B))
	print("Then the hypotenuse must be {} and the perimeter must be {}.".format(sqrt(A**2 + B**2), (sqrt(A**2 + B**2) + A + B)))

# 9.
def Task9(A:int=None,B:int=None): # values of both variables are user defined.
	ParameterCheck((A, B),("A","B"))
	print("Values of A and B are ",A,B, ", respectively")
	TemporaryVariable = B
	B = A
	A = TemporaryVariable
	print("Values of A and B are ",A,B, ", respectively")

# 10.
def Task10(X=None,Y=None,A=None): # Again, all values are user defined.
	ParameterCheck((X, Y, A),("X","Y", "A"))
	Price = A/X
	Cost = Price*Y
	print("price of 1kg of candies = {}. \n Total cost of {}kg of candies = {}.".format(Price,Y,Cost))

# 11.
def Task11(A=None,B=None,C=None):
	ParameterCheck((A, B, C),("A","B", "C"))
	if(not A<C or not C<B):
		print("Initial conditions differ from the task.")
	AC = abs(C-A)
	BC = abs(B-C)
	print("AC = {}.\n BC = {}.\n AC*BC = {}".format(AC,BC,AC*BC))

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