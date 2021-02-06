#Count of letters in string
string = input("Enter the String: ")
letter = input("Enter the letter to find frequency: ")
count = 0
for i in range(len(string)):
	if string[i] == letter:
		count += 1
print(count)