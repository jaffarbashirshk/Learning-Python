#Calculate Frequency of Characters
string = input("Enter the string: ")
frequency = {}
for word in string:
	if word in frequency:
		frequency[word] +=1
	else:
		frequency[word] = 1
print(f"The frequencies of word in {string} is {frequency}")
