# Program to perform arithematic operators

continu = 'y'
while continu == 'y':
	number_1  = int(input("Enter a number: "))
	number_2  = int(input("Enter another number: "))
	operation = input("Enter the operation to perform 1) Addition(+) , 2) Subtraction, 3) Multiplication, 4) Division: ")
	if operation == '+' or '1':
		sum = number_1 + number_2
		print(f"The Addition of {number_1} and {number_2} is {sum}")
	elif operation == '-' or '2':
		difference = number_1 - number_2
		print(f"The Subtraction of {number_1} and {number_2} is {difference}")
	elif operation == '*' or '3':
		mul = number_1*number_2
		print(f"The Multiplication of {number_1} and {number_2} is {mul}")
	else:
		div = number_1 / number_2
		print(f"The Division of {number_1} and {number_2} is {div}")
	continu = input("Do you want to continue [y/n]")
