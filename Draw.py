import numpy as np

def write_board(n,char=' '):
	for i in range(0,n):
		print " "+"--- "*n
		print "|"+(" "+char+" |")*n
	print " "+"--- "*n

def init_mat(n=3):
	mat = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
	return mat

def update_mat(mat,x=0,y=0,char='X'):
	mat[x][y] = char
	return mat

def update_board(mat,n=3):
	for i in range(n):
		print " "+"--- "*n
		print "|",
		for j in range(n):
			print mat[i][j]+" |",
		print ""
	print " "+"--- "*n

if ( __name__ == "__main__" ):
	num = input("Provide the number for board game")
	write_board(num)
	matrix = init_mat()
	matrix = update_mat(matrix)
	update_board(matrix)
