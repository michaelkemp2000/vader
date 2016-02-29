# Battleships Game

from random import randint

# Create battlefield

class board(object):

	board = []
	ships = []

	def reset_boards(num):
	
		for i in range(num):
			board.append(num*["O"])

		for i in range(num):
			ships.append(num*["O"])

# print play areas

def print_board(board, ships):

	for row in board:
		print ""
		print "".join(row)
	for row in ships:
		print ""
		print "".join(row)

# Obtain ship location

def random_row(ships):

	return randint(0, len(board) -1)

# Obtain ship location

def random_col(ships):

	return randint(0, len(board) -1)

# Create Ships

def ships(snum):

	for n in snum:
		ship_row = random_row(ships)
		ship_col = random_col(ships)
		ships.append[ship_row][ship_col] = "S"
		print_board(board, ships)

		if ships[ship_row][ship_col] == "S":
			increase_ship(ship_row, ship_col)

def increase_ship(ship_row, ship_col):

		print "Increasing Ship Size."
		if ship_row not in range(9) or \
			ship_col not in range(9):
			ships.append[ship_row - 1][ship_col] = "S"
		else:
			ships.append[ship_row + 1][ship_col] = "S"

#for turn in range(4):
#
#	print turn +1
#	guess_row = int(raw_input("Guess Row: "))
#	guess_col = int(raw_input("Guess Column: "))
#	print ship_row
#	print ship_col
#
#	if guess_row == ship_row and guess_col == ship_col:
#		print "Congratulations! You sank my battleship!"
#		break
#
#	elif guess_row not in range(5) or \
#			guess_col not in range(5):
#		print "Oops, that's not even in the ocean."
#
#		if turn == 3:
#			print "Game Over"
#		
#	elif board[guess_row][guess_col] == "X":
#		print "You guessed that one already."
#
#		if turn == 3:
#			print "Game Over"
#
#	else:
#		print "You missed my battleship!"
#		board[guess_col][guess_row] = "X"
#		print_board(board)
#
#		if turn == 3:
#			print "Game Over"

# Main

game1 = board.reset_boards(10)
print game1
print_board(board, ships)
ships(4)




