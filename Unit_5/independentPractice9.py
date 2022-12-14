# Zachary hoover || independent practice 9
# 10-6-22
import os
from inspect import getmembers, isfunction

# repeating code
################

global clear
clear = lambda: os.system("clear" if os.name == "posix" else "cls")

def printHeader():
    clear()
    print("\n     Independent Practice 9   ")
    print(" --------------+--------------\n")
    return

def returnMain():
    print("\n Press Enter to continue")
    input()
    autoMenu()

################################################
# start functions here

def cityCountry(city, country):
	return f"{city.title()}, {country}"

def city_country():
	printHeader()

	"""
	This function calls the cityCountry() function 10 times using different cities and countries, and prints the result.
	"""

	name = cityCountry("Concord", "United States of America")
	print("", name)
	name = cityCountry("Mexico City", "Mexico")
	print("", name)
	name = cityCountry("Berlin", "Germany")
	print("", name)
	name = cityCountry("Barcelona", "Spain")
	print("", name)
	name = cityCountry("Madrid", "Spain")
	print("", name)
	name = cityCountry("London", "England")
	print("", name)
	name = cityCountry("Sydney", "Australia")
	print("", name)
	name = cityCountry("Boston", "United States of America")
	print("", name)
	name = cityCountry("New York", "United States of America")
	print("", name)
	name = cityCountry("Paris", "France")
	print("", name)

	returnMain()

################################################

# auto Menu starts
# made this function to automate the menus I use in my assignments, it can also do a bit more.

menuMode = 0
currentBench = 0

def autoMenu():	
	global menuMode
	global currentBench
	global usable

	if menuMode == 1:
		if currentBench > len(usable):
			menuMode = 0
			currentBench = 0
			autoMenu()
		else:
			currentBench += 1
			usable[currentBench-1][1]()

	if menuMode == 2:
		if currentBench > len(usable):
			menuMode = 0
			currentBench = 0
			autoMenu()
		else:
			currentBench += 1
			usable[currentBench-1][1]()
	
	else:
		printHeader()

		# change were it says 'baseTemplate' to module name.
		import independentPractice9 as foo
		
		list = getmembers(foo, isfunction)
	
		i = 0
		x = 0
		exceptions = [
			 "autoMenu", "printHeader", "getmembers", "clear", "time", "isfunction",
			 "returnMain", "cls", "cityCountry"
			]
		
		usable = []
		
		print(">> ----+ Functions +---- <<")
		while i < len(list):		
			if list[i][0] not in exceptions:
				x += 1
				print(f"  {x}. {list[i][0]}")
				usable.append(list[i]) 
			i += 1

		print("\n>> ----+ Utilities +---- <<")
		print(f"  {x+1}. Exit program")
		print(f"  {x+2}. Benchmark (run all)")
		print(f"  {x+3}. Debug (to be added later)")
		
		try:
			usrin = int(input("\n Enter number of the item: "))
			if usrin == len(usable) + 1:
				SystemExit()
			elif usrin == len(usable) + 2:
				menuMode = 1
				print("Bench")
				autoMenu()
			elif usrin == len(usable) + 3:
				menuMode = 2
				print("Debug")
				autoMenu()
			else:
				usable[usrin-1][1]()
		
		except:
			autoMenu()
			
# auto menu ends
if __name__ == "__main__": autoMenu();