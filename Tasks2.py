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


# Нумерация заданий совпадает с заданиями для учеников в файле
def Task2(A:int=None):
	ParameterCheck((A),("natural number A")) # Here and below this line checks if user defined parameter.
	print("Statement is", A%2!=0) # A lot of tasks did not requested output, but I feel that it's supposed to give an output.
def Task3(A:int=None,B:int=None):
	ParameterCheck((A,B),("natural number A","natural number B"))
	print("Statement is", A%2==B%2)
def Task4(A:int=None,B:int=None,C:int=None):
	ParameterCheck((A,B,C),("integer A","integer B", "integer C"))
	List = [A,B,C]
	for number in List:
		if(number>0):
			print("Statement is true")
			return None
	print("Statement is false")
def Task5(A=None):
	ParameterCheck((A),("natural number"))
	print(str(A)[-1]) # This line turns integer to text and then takes last letter (in this case number) and prints it
def Task7(A:float=None):
	ParameterCheck((A),("floating point number"))
	try:
		Answer = str(A)[str(A).find(".")+1] # this line converts int to string, then finds index of decimal point and looks for the letter after it.
	except IndexError: # If user passed a string with decimal dot at the end the algorithm will throw this exception.
		print("This number has nothing after decimal point. That's not how float works.")
		return None
	if(Answer == str(A)[0]): # since .find() outputs -1 in case of absence, the next to this would be 0
		print("Unable to find decimal point.")
	else:
		print(Answer)
def Task9(N:int=None, ISO8601=True):
	# This problem has two solutions, 12-hour clock and international standart clock. To get solution for the former - set the ISO8601 tag to False
	ParameterCheck((N),("number of seconds"))
	n = n % (24*3600)
	if(n//3600<12 or ISO8601):
		print(n//3600,"hours", (n%3600)//60, "minutes", (n%3600)%60, "seconds")
	else:
		print((n//3600)-12,"hours", (n%3600)//60, "minutes", (n%3600)%60, "seconds")
def Task10(a=None,b=None,n=None):
	ParameterCheck((a,b,n),("price in roubles","price in kopecks","number of pies"))
	b = (b*n) % 100
	a = (a*n) + (b*n) // 100
	print("{a} roubles, {b} kopecks".format(a=a,b=b))
def Task11(Number=None):
	ParameterCheck((Number),("natural number"))
	#i = 0
	#while(Number>9):
	#	i = i +1
	#	Number = Number - 10
	print("%s tens"%Number//10)
def Task12(Number=None):
	ParameterCheck((Number),("two digit number"))
	print(int(str(Number)[0])+int(str(Number)[1])) # firstly this line converts number to string, then takes both letters, converts them again, and then adds them up
def Task14(Number=None):
	ParameterCheck((Number),("natural number"))
	List = []
	for digit in str(Number):
		if(digit not in List):
			List.append(digit)
		else:
			print("Statement is false")
			return None
	print("Statement is true")
def Task15(Number=None):
	ParameterCheck((Number),("natural number"))
	ascendSeq = True
	descendSeq = True
	# This two cycles are iterating over numbers.
	for digitIndex in range(1,len(str(Number))):  #First one checks for ascending sequence...
		if(str(Number)[digitIndex-1]>str(Number)[digitIndex]): 
			ascendSeq = False 
			break
	for digitIndex in range(1,len(str(Number))): # ...the other one for descending.
		if(str(Number)[digitIndex-1]<str(Number)[digitIndex]): # If it finds out that there is a wrong pair
			descendSeq = False # it sets according tag to False
			break	
	print("Statement is",(ascendSeq or descendSeq))


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
		print("Something went wrong. Here's exception ->", type(E), E) # and print them out
	print("\n")