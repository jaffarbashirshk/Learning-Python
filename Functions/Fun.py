#Create a function that can accept two arguments name and age and print its value
def func(name,age):
    return ("Name entered is: " + name + " and age entered is: " + str(age))
name = input("Enter name: ")
age = int(input("Enter age: "))
print(func(name,age))
