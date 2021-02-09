# Check weather a number is divisible by 2 and 3 or not
number = int(input("Enter a number: "))
if number % 2 == 0:
	#print("Number is divisible by 2 but not by 3")
	if number % 3 == 0:
		print(f"{number} is divisible by both 2 and 3")
	else:
		print(f"{number} is divisible by 2 but not 3")
else:
	if number % 3 == 0:
		print(f"{number} is divisible by 3 but not 2")
	else:
		print(f"{number} is neither divisible by 2 nor by 3")
