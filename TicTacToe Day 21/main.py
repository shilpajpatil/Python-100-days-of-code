import random


gameboard= {"1":' ', "2":' ', "3":' ',
            "4":' ', "5":' ',"6":' ',
            "7":' ', "8":' ', "9":' '}

# Accessing the dictionary content use
print(gameboard)


def theboard(board):
    print(board['1'] +'|'+board['2']+'|'+ board['3'])
    print('-+-+-')
    print(board['4'] +'|'+board['5']+'|'+ board['6'])
    print('-+-+-')
    print(board['7'] +'|'+board['8']+'|'+board['9'])

# function call with sending gamelogic to that function
theboard(gameboard)


def isWinner(board,turn):
    if not board['1']==' ' and board['1']==board['2'] and not board['2']==' ' and board['2']==board['3']:
        print(board['3']+ " Is the Winner")
        return True
    elif not board['4']==' ' and board['4']==board['5'] and not board['5']==' ' and board['5']==board['6']:
        print(board['6']+ " Is the Winner")
        return True

    elif not board['7'] == ' ' and board['7']==board['8'] and not board['8'] == ' ' and board['8']==board['9']:
        print(board['9']+ " Is the Winner")
        return True
    elif not board['1']==' ' and board['1']==board['4'] and not board['4']==' ' and board['4']==board['7']:
        print(board['1']+ " Is the Winner")
        return True
    elif not board['2']==' ' and board['2']==board['5'] and not board['5']==' ' and board['5']==board['8']:
        print(board['2']+ " Is the Winner")
        return True

    elif not board['3']==' ' and board['3']==board['6'] and not board['6']==' ' and board['6']==board['9']:
        print(board['3']+ " Is the Winner")
        return True

    #     Digonals check
    elif not board['1']==' ' and board['1']==board['5'] and not board['5']==' ' and board['5']==board['9']:
        print(board['1']+ " Is the Winner")
        return True

    elif not board['3']==' ' and board['3']==board['5'] and not board['5']==' ' and board['5']==board['7']:
        print(board['3']+ " Is the Winner")
        return True

def resetBoard(board):
    for k in board.keys():
        board[k]=' '
resetBoard(gameboard)
players = ['x','o']
turn = random.choice(players)

#here we are traversing a gameboard from each colume
for i in range(9):
    print("whos trun :" + turn + ",plays")   # for getting whose turn is this
    print("your choice: ")      # where i have to mark

    #travers to  your board
    for k in gameboard.keys():
        #print(k)
        if gameboard[k] == ' ':
            print(k, end = " ")

    #here getting the input
    move = input()

    if move not in gameboard.keys():
        print("Incorrect Move")

    gameboard[move] = turn
    print(theboard(gameboard))

    iswon = isWinner(gameboard,turn)

    if  iswon:
        print("congrats!!")
        print(turn ," win")
        resetBoard(gameboard)
        break;
    if turn == 'x':
        turn = 'o'
    else:
        turn='x'

    if i == 8:
        print("Match drew")








