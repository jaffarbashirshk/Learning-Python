# Tic tac toe Project
import random
name = input("Enter your name: ")
game_input = ['Null','x','o','x','o','x','o','x','o','x']
def board(game_input):
	print(game_input[7]+'|'+game_input[8]+'|'+game_input[9])
	print(game_input[4]+'|'+game_input[5]+'|'+game_input[6])
	print(game_input[1]+'|'+game_input[2]+'|'+game_input[3])

#print(board(game_input))

def player_input():
	marker = input(f"Dear {name}! Choose your marker either 'x' or 'o':")
	while marker != 'x' and marker != 'o':
		marker = input("Choose your marker again: ")
	if marker == 'x':
		return ('x ','o ')
	else:
		return('o ','x ')
#Put the marker on board
def put_marker(game_input,marker,position):
	game_input[position] = marker


#Criteria to check if the player has won or not
def win(game_input,marker):
	return  ((game_input[7] == game_input[8] == game_input[9] == marker) or
			(game_input[4] == game_input[5] == game_input[6] == marker) or
    		(game_input[7] == game_input[4] == game_input[1] == marker) or
			(game_input[8] == game_input[5] == game_input[2] == marker) or
    		(game_input[9] == game_input[6] == game_input[3] == marker) or
    		(game_input[1] == game_input[5] == game_input[9] == marker) or
			(game_input[7] == game_input[5] == game_input[3] == marker))
    
#print(win(game_input,'o'))
#choose player using random function
def choose_player():
	player = random.randint(1,2)
	if player == 1:
		return 'Player_1'
	else:
		return 'Player_2'
#checking empty space
def space(game_input,position):
	return game_input[position] == ' '
#checking full board for empty space
def full_board_check(game_input):
	for i in range(1,10):
		if space(game_input,i):
			return False
		return True
#player Choice marker Placement
def player_choice(game_input):
	position = 0
	while position not in [1,2,3,4,5,6,7,8,9] or not space(game_input,position):
		position = int(input("Please choose your position (1-9) on num-pad: "))
	return position
#Would u like to play again
def play_again():
	choice = input("Would you like to play again [y/x]")
	return choice == 'y'

#Game mechanism
while True:
	the_board = [' ']*10
	player_1,player_2 = player_input()
	print(player_1 + 'is player_1 sign')
	print(player_2 + 'is player_2 sign')
	turn = choose_player()
	print(turn + "will play first")
	play_game = input("Are you ready to play[y/n]")
	if play_game == 'y':
		game_on = True
	else:
		game_on = False
	while game_on:
		if turn == 'player_1':
			board(the_board)
			position = player_choice(the_board)
			put_marker(the_board,player_1,position)
			if win(the_board,player_1):
				board(the_board)
				print("Player1 has won")
				game_on = False
			else:
				if full_board_check(the_board):
					board(the_board)
					print("Game tie")
					game_on = False
				else:
					turn = 'player_2'
		else:
			board(the_board)
			position = player_choice(the_board)
			put_marker(the_board,player_2,position)
			if win(the_board,player_2):
				board(the_board)
				print("Player2 has won")
				game_on = False
			else:
				if full_board_check(the_board):
					board(the_board)
					print("Game tie")
					game_on = False
				else:
					turn = 'player_1'

# Check weatherr the player wants to paly again or not
	if not play_again():
		break;
