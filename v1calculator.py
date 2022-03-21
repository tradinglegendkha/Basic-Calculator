#calculator

#name of the user
print("Enter your name")
name = input()
print("Hello " + name, "this is a calculator")

#numbers the user wants to calculate 
print("\nPlease pick two numbers")
n1 = int(input("First number "))
n2 = int(input("Second number "))

#calculations
print("\nNow what do you wanna calculate? Add, Minus, Times, Divide")
sym = input()
if sym == "add": 
	add = n1+n2
	print("Answer:", n1, "+", n2, "=", add)

elif sym == "minus":
	minus = n1-n2
	print("Answer:", n1, "-", n2, "=", minus)

elif sym == "times":
	times = n1*n2
	print("Answer:", n1, "*", n2, "=", times)

elif sym == "divide":
	divide = n1/n2
	print("Answer:", n1, "/", n2, "=", divide)

else: 
	print("Please pick a symbol and try again " + name)


