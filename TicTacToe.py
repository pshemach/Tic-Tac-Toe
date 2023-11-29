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


def check_column(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != '-':
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '-':
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '-':
        winner = board[6]
        return True


def check_raw(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '-':
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '-':
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '-':
        winner = board[2]
        return True


def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '-':
        winner = board[0]
        return True
    elif board[2] == board[4] == board[7] and board[6] != '-':
        winner = board[2]
        return True


def check_win(board):
    global game_running
    if check_column(board):
        print_board(board)
        print(f'The Winner: {winner}')
        game_running = False
    elif check_raw(board):
        print_board(board)
        print(f'The Winner: {winner}')
        game_running = False
    elif check_diagonal(board):
        print_board(board)
        print(f'The Winner: {winner}')
        game_running = False


def check_tie(board):
    global game_running
    if '-' not in board:
        print_board(board)
        print("It's Tie")
        game_running = False


while game_running:
    print_board(board)
    player_input(board)
    check_win(board)
    if not game_running:
        break
    check_tie(board)
    if not game_running:
        break
    switch_player(current_player)
    compute(board)
    check_win(board)
    if not game_running:
        break
    check_tie(board)
