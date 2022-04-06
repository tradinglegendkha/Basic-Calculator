#calculator v1.2

#name of the user
name = input("Enter your name: ")
print("Hello "+name+ " this is a calculator")

def TwoNum():
	global n1, n2
	print("\nPlease pick two numbers")
	n1 = int(input("First number: "))
	n2 = int(input("Second number: "))

#numbers the user wants to calculate 
def fourSymbols():
	#calculations
	print("\nWhat do you wanna calculate? Add, Minus, Times, Divide")
	sym = input()

	if sym == "add" or sym == "Add": 
		TwoNum()
		add = n1+n2
		print("Answer:", n1, "+", n2, "=", add)
	elif sym == "minus" or sym == "Minus":
		TwoNum()
		minus = n1-n2
		print("Answer:", n1, "-", n2, "=", minus)
	elif sym == "times" or sym == "Times":
		TwoNum()
		times = n1*n2
		print("Answer:", n1, "*", n2, "=", times)
	elif sym == "divide" or sym == "Divide":
		TwoNum()
		divide = n1/n2
		print("Answer:", n1, "/", n2, "=", divide)
	else: 
		print("Please pick a symbol and try again " + name)

fourSymbols()

while True:
	#used a while loop to ask the the person
	YorN = input("Do you want to continue? ")
	if YorN == "yes":
		fourSymbols()
	else:
		print("Thank you {}, bye".format(name))
		break 
#remove do you want to continue, should be seamesly



