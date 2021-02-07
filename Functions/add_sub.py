#Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call
def calculation(num_1,num_2):
	add = num_1 + num_2
	sub = num_1 - num_2
	return f"the sum of {num_1} and {num_2} is {add} and subtraction is {sub}"
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print(calculation(num_1,num_2))