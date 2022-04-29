board = ['1','2','3','4','5','6','7','8','9']
turns = 0

def pick_marker():
    valid_marker = False 
    while valid_marker == False:
        player_1 = input('Player 1, do you want X or O: ').upper()
        if player_1 not in ['X', 'O']:
            print('Not valid - please choose X or O')
            continue
        else:
            valid_marker = True
            if player_1 == 'X':
                player_2 = 'O'
                print("PLAYER 1:", player_1, "PLAYER 2:", player_2)
            else:
                player_2 = 'X'
                print("PLAYER 1:", player_1, "PLAYER 2:", player_2)
            take_turn(board,turns,player_1,player_2)

def show_board(board):
    print(board[0] + '|' +board[1]+'|'+board[2])
    print('-|-|-')
    print(board[3] + '|' +board[4]+'|'+board[5])
    print('-|-|-')
    print(board[6] + '|' +board[7]+'|'+board[8])
    
def take_turn(board,turns,player_1,player_2):
    show_board(board)
    valid_turn = False
    while valid_turn == False:
        user_choice = input('Pick a number between 1 and 9: ')
        if user_choice.isdigit() and int(user_choice) in range(1,10):
            valid_turn = True
            turns = turns + 1
            change_board(board, user_choice, turns,player_1,player_2)
        else:
            continue

def change_board(board,user_choice, turns,player_1,player_2):
    for idx in range(len(board)):
        if user_choice == board[idx]:
            if turns % 2 == 0:
                board[idx] = player_2
            else:
                board[idx] = player_1
    take_turn(board,turns,player_1,player_2)
            
pick_marker()
show_board(board)