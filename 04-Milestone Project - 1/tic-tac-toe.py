board = ['1','2','3','4','5','6','7','8','9']
turns = 0
valid_marker = False
user_choice = ''

def pick_marker(valid_marker):
    while valid_marker == False:
        player_1 = input('Player 1, do you want X or O: ').upper()
        if player_1 not in ['X', 'O']:
            print('Not valid - please choose X or O')
            continue
        else:
            valid_marker = True
            if player_1 == 'X':
                player_2 = 'O'
            else:
                player_2 = 'X'
    print("PLAYER 1:", player_1, "PLAYER 2:", player_2)
    take_turn(board,turns,player_1,player_2)

def check_win(player_1,player_2,turns):
    win = False
    if board[0] == board[1] == board[2]:
        win = True
        if board[0] == 'X':
            winner = 'X'
        else:
            winner = 'O'
    elif board[3] == board[4] == board[5]:
        win = True
        if board[3] == 'X':
            winner = 'X'
        else:
            winner = 'O'
    elif board[6] == board[7] == board[8]:
        win = True 
        if board[6] == 'X':
            winner = 'X'
        else:
            winner = 'O'
    elif board[0] == board[3] == board[6]:
        win = True
        if board[0] == 'X':
            winner = 'X'
        else:
            winner = 'O'
    elif board[1] == board[4] == board[7]:
        win = True
        if board[1] == 'X':
            winner = 'X'
        else:
            winner = 'O'
    elif board[2] == board[5] == board[8]:
        win = True
        if board[2] == 'X':
            winner = 'X'
        else:
            winner = 'O'
    elif board[0] == board[4] == board[8]:
        win = True 
        if board[0] == 'X':
            winner = 'X'
        else:
            winner = 'O'
    elif board[2] == board[4] == board[6]:
        win = True 
        if board[2] == 'X':
            winner = 'X'
        else:
            winner = 'O'
    if win == True:
        show_board(board)
        print('End of game.', winner, "wins")
    else: 
        take_turn(board,turns,player_1,player_2)

def show_board(board):
    print('\n'*100)
    print(board[0] + '|' +board[1]+'|'+board[2])
    print('-|-|-')
    print(board[3] + '|' +board[4]+'|'+board[5])
    print('-|-|-')
    print(board[6] + '|' +board[7]+'|'+board[8])
    
def take_turn(board,turns,player_1,player_2):
    show_board(board)
    valid_turn = False
    current_player = ''
    while valid_turn == False:
        if turns %2 == 0:
            current_player = 'Player 1'
        else:
            current_player = 'Player 2'
        user_choice = input('{}, pick a number between 1 and 9: '.format(current_player))
        if user_choice.isdigit() and int(user_choice) in range(1,10):
            valid_turn = True            
            change_board(board, user_choice, turns,player_1,player_2)
        else:
            continue

def change_board(board,user_choice, turns,player_1,player_2):
    for idx in range(len(board)):
        if user_choice == board[idx]:
            turns = turns + 1
            if turns % 2 == 0:
                board[idx] = player_2
            else:
                board[idx] = player_1
        else:
            continue
    check_win(player_1,player_2,turns)   
            
pick_marker(valid_marker)