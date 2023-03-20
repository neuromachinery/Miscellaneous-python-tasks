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

def Task1(Day:int=None, ISO8601=True): # There are international date standard as tag, if your week starts from sunday - set it to false
	ParameterCheck((Day),("number between 1 and 7")) 
	if(ISO8601):
		weekDict = {
			1:"monday",
			2:"tuesday",
			3:"wednesday",
			4:"thursday",
			5:"friday",
			6:"saturday",
			7:"sunday"
		}
	else:
		weekDict = { # for Americans and others
			1:"sunday",
			2:"monday",
			3:"tuesday",
			4:"wednesday",
			5:"thursday",
			6:"friday",
			7:"saturday"
		}
	print(weekDict[Day])
def Task2(Month:int=None):
	ParameterCheck((Month),("number between 1 and 12")) 
	seasonDict = {
		1:"winter",
		2:"winter",
		3:"spring",
		4:"spring",
		5:"spring",
		6:"summer",
		7:"summer",
		8:"summer",
		9:"autumn/fall",
		10:"autumn/fall",
		11:"autumn/fall",
		12:"winter"
	}
	if(1>Month or Month>12):
		print("Non-existant month.")
		return None
	print(seasonDict[Month])
def Task3(Column=None, Row=None):
	ParameterCheck((Row,Column),("Row position", "Column position"))
	if(Column>8 or Column<0 or Row>8 or Row<0):print("Not a real chess board, but if it was, then")
	chessDict = {
		True:"black",
		False:"white"
	}
	print("The position at ({},{}) is {}".format(Column,Row,chessDict[(Column+Row)%2==0]))
def Task4(x1=None,y1=None,x2=None,y2=None):
	ParameterCheck((x1,y1,x2,y2),("x1","y1","x2","y2"))
	chessDict = {
		True:"black",
		False:"white"
	}
	if(chessDict[(x1+y1)%2==0]==chessDict[(x2+y2)%2==0]):
		print("YES")
	else:
		print("NO")
def Task5(x1=None,y1=None,x2=None,y2=None):
	ParameterCheck((x1,y1,x2,y2),("x1 for king piece","y1 for king piece","x2 for movement tile","y2 for movement tile"))
	def hypot(x,y): # this calculates hypotenuse
		return (x*x + y*y)**0.5 
	if(hypot(x1-x2,y1-y2)<1.5): # this calculates range between points. Maximum reach of a king is square root of 2 ~= 1.4
		print("YES")
	else:
		print("NO")
def Task6(a=None,b=None,c=None):
	ParameterCheck((a,b,c),("natural number 'a'","natural number 'b'","natural number 'c'"))
	result = a
	for number in [a,b,c]:
		if(number>result):
			result = number
	print("largest number is %s"%result)
def Task7(a=None,b=None,c=None):
	ParameterCheck((a,b,c),("natural number 'a'","natural number 'b'","natural number 'c'"))
	result = a
	for number in [a,b,c]:
		if(number<result):
			result = number
	print("smallest number is %s"%result)
def Task8(a=None,b=None,c=None):
	ParameterCheck((a,b,c),("natural number 'a'","natural number 'b'","natural number 'c'"))
	smallest = a
	largest = a
	for number in [a,b,c]:
		if(number<smallest):
			smallest = number
		if(number>largest):
			largest = number
	for number in [a,b,c]:
		if(number not in [largest,smallest]):
			print(number)
			return None
	print("There are duplicates in numbers")
def Task9(Year:int=None):
	ParameterCheck((Year),("Year"))
	if(Year%4==0 and not (Year%100==0 and not Year%400==0)):
		print("YES")
	else:
		print("NO")
def Task10(a=None,b=None,c=None):
	ParameterCheck((a,b,c),("natural number 'a'","natural number 'b'","natural number 'c'"))
	if((a+b)>c and (a+c)>b and (b+c)>a):
		print("YES")
	else:
		print("NO")

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