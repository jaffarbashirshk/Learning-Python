#Program to print birthday message
def birthday(sender,reciever):
	message  = f'Hello {reciever}, {sender} Here!. I wish you many many happy returns of the day ):'
	return message

sender = input('Enter the name of sender: ')
reciever = input("Enter the name of reciever: ")
print(birthday(sender,reciever))