#Into to programing
#Author: Daniel Gisolfi
#Date: 11/4/16
#tictactoe.py


board =[[0,0,0],
	[0,0,0],
	[0,0,0]]

symbols = [" ", "x", "o"]



def play(board,row,column,player):
	if board[row][column] == 0:
		if player == 1:
			board[row],[column] = [player]
		elif player == 2:
			board[row],[column] = [player]
		return True
	elif board[row][column] != 0:
		return False




def displayBoard():
	print('   |   |')
	print(' ' + board[0,0] + ' | ' + board[0,1] + ' | ' + board[0,2])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1,0] + ' | ' + board[1,1] + ' | ' + board[1,2])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[2,0] + ' | ' + board[2,1] + ' | ' + board[2,2])
	print('   |   |')


