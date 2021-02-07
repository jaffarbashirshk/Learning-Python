#Create a function showEmployee() in such a way that it should accept employee name, and it’s salary and display both, and if the salary is missing in function call it should show it as 9000
def showEmployee(name,salery):
	return f"{name} has salery {salery} rupees"
name = input("Enter the name of Employee: ")
salery = input("Enter the salery: ")
print(showEmployee(name,salery = 9000))