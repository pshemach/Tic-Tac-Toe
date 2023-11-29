import random

board = ['-'] * 9
winner = None
current_player = 'X'
game_running = True


def print_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-----')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-----')
    print(board[6] + '|' + board[7] + '|' + board[8])


def player_input(board):
    inp = int(input('Enter a Number (1-9):'))
    if board[inp - 1] == '-':
        board[inp - 1] = current_player
    else:
        print('Oops Space is occupied..!!!')


def switch_player(c_player):
    global current_player
    if c_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'


def compute(board):
    while current_player == 'O':
        position = random.randint(0, 8)
        if board[position] == '-':
            board[position] = 'O'
            switch_player(current_player)


player_input(board)
switch_player(current_player)
compute(board)
print_board(board)
