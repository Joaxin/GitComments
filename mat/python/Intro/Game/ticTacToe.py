"""
井字棋游戏
[井字棋](https://zh.wikipedia.org/wiki/%E4%BA%95%E5%AD%97%E6%A3%8B)
"""


import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['LL'] + '|' + board['LM'] + '|' + board['LR'])

def main():
    theBoard = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'LL': ' ', 'LM': ' ', 'LR': ' '
    }

    key_map = {
        '1':'TL', '2':'TM', '3':'TR',
        '4':'ML', '5':'MM', '6':'MR',
        '7':'LL', '8':'LM', '9':'LR'
    }

    begin = True
    while begin:
        board = theBoard.copy()
        begin = False
        turn = 'X'
        counter = 1
        os.system('clear')

        print_board(board)
        while counter <= 9:
            move = input('Turn %d for %s . Move on which space?\n' % (counter,turn)).strip().upper()
            if move in theBoard or move in key_map:
                if move in theBoard and board[move] == ' ':
                    board[move] = turn
                elif move in key_map and board[key_map[move]] == ' ':
                    board[key_map[move]] = turn
                else:
                    print('This space has been taken, plz try another space.')
                    continue
                bd = list(board.values())
                # print(bd)
                check_lines = [bd[:3],bd[3:6],bd[6:],bd[::3],bd[1::3],bd[2::3],bd[0::4],bd[2:8:2]]
                if ['X']*3 in check_lines :
                     print_board(board)
                     print('Turn %d : Player X WIN!!!'% counter)
                     break
                elif ['O']*3 in check_lines:
                    print_board(board)
                    print('Turn %d : Player O WIN!!!'% counter)
                    break
                elif counter == 9:
                    print_board(board)
                    print('Turn %d : WIN WIN!!!'% counter)
                    break
                else:
                    counter += 1
                    if turn == 'X':
                        turn = 'O'
                    else:
                        turn = 'X'   
            else:
                print('Invaild input.')
                continue
            os.system('clear')
            print_board(board)
        choice = input('Play Again?(Y|N)\n')
        begin = choice == 'Y'


if __name__ == '__main__':
    main()
