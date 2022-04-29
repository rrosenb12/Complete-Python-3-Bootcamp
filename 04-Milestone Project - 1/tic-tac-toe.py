board = ['1','2','3','4','5','6','7','8','9']

def pick_marker():
    player_1 = input('Player 1, do you want X or O: ').upper()
    if player_1 not in ['X', 'O']:
        print('Not valid - please choose X or O')
        pick_marker()
    else:
        if player_1 == 'X':
            player_2 = 'O'
            print("PLAYER 1:", player_1, "PLAYER 2:", player_2)
        else:
            player_2 = 'X'
            print("PLAYER 1:", player_1, "PLAYER 2:", player_2)
        show_board(board)

def show_board(board):
    print(board[0] + '|' +board[1]+'|'+board[2])
    print('-|-|-')
    print(board[3] + '|' +board[4]+'|'+board[5])
    print('-|-|-')
    print(board[6] + '|' +board[7]+'|'+board[8])

pick_marker()