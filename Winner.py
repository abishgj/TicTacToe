import numpy as np
import sys

wc1 = 0
wc2 = 0

def read_matrix(n):
	mat = [[] for i in range(0,n)]
	for i in range(0,n):
		mat[i] = eval(raw_input("Enter %d row"%(i)))
	return mat

def row_col(mat,n):
	global wc1, wc2
	for i in range(n):
		if ( len(set(mat[i])) == 1 ):
			if ( 'X' in mat[i] ):
				wc1 += 1
			elif ( 'O' in mat[i] ):
				wc2 += 1
	diagl = np.diag(mat)
	if ( len(set(diagl)) == 1 ):
		if ( 'X' in diagl ):
			wc1 += 1
		elif( 'O' in diagl ):
			wc2 += 1

def find_winner(matr,n=3):
	row_col(matr,n)
	matc = np.array(matr)
	row_col(np.fliplr(matc.transpose()),n)
	if ( wc1 == wc2 ):
		return 0
	elif ( wc1 > wc2 ):
		return 1
	else:
		return 2

if ( __name__ == "__main__" ):
	print "Tic Tac Toe!!"
	n = input("Provide the number of rows")
	matrix = read_matrix(n)
	find_winner(matrix,n)
