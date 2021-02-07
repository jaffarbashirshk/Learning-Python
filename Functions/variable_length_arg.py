#Write a function func1() such that it can accept a variable length of  argument and print all arguments value


def funct(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum
print(funct(10,20,30))
