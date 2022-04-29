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



pick_marker()