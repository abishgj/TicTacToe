import os
import re
import Draw
import Winner
import sys

def update_display(matrix,x,y,char):
	os.system('clear')
	Draw.update_mat(matrix,x,y,char)
	Draw.update_board(matrix)

def tf_validate(str):
	str.strip()
	if(re.match(r'[1-3],[1-3]',str)):
		return str 
	else:
		print "Please specify the move in the format described.\n"
		return None

def over_validate(x,y):
	if ( matrix[x][y] == ' ' ):
		return True
	else:
		print "Don't try to overwrite the box"
		return False

def interact(uname):
	print "Player %s's turn:\n"%(uname)
	while True:
		inp = raw_input("Enter your move\t")
		move = tf_validate(inp)
		if( move == None ):
			continue
		else:
			(x,y) = tuple(move.split(','))
			x = int(x);y=int(y)
			x -= 1;y -= 1
			if ( over_validate(x,y) == False ):
				continue
			break
	return (x,y)

def game_proc(user1,user2,n):
	choice = { user1:'X',user2:'O' }
	run = n ** 2
	for i in range(run):
		if ( i % 2 == 0 ):
			(x,y) = interact(user1)
			char = choice.get(user1)
			x = int(x)
			y = int(y)
			update_display(matrix,x,y,char)
			
		else:
			(x,y) = interact(user2)
			char = choice.get(user2)
			update_display(matrix,x,y,char)
	return True

def init_game():
	global matrix
	u1c = 'X'; u2c = 'O'
	os.system('clear')
	print "Tic Tac Toe is a two player game. A borad will be shown to you. You need to choose a box where you want to put your sign. You can choose a box as 1,1 for the first box and 1,2 for the second box in first row.\n"
        print "Program will ask for input from the user specifically.\n"
        x = raw_input("Shall we start ??")
	os.system('clear')
	user1 = raw_input("Player 1: Enter your name:\t")
	x = raw_input("REMEMBER:\tYour sign is %c\n\n"%(u1c))
	os.system('clear')
	user2 = raw_input("Player 2: Enter your name:\t")
	x = raw_input("REMEMBER:\tYour sign is %c\n\n"%(u2c))
	os.system('clear')
	x = raw_input("Good Luck %s and %s..\n"%(user1,user2))
	os.system('clear')
	n = 3
	Draw.write_board(n)
	matrix = Draw.init_mat()
	if ( game_proc(user1,user2,n) == True ):
		choice = { 1:user1, 2:user2 } 
		print "Nice moves by both %s and %s, let's see the result\n"%(user1,user2)
		x = raw_input("Shall We ??\n")
		wval = Winner.find_winner(matrix)
		if ( wval in choice ):
			print "Player %s wins!!"%(choice.get(wval))
		else:
			print "It's a TIE!!"

if ( __name__ == "__main__"):
	init_game()
