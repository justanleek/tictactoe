import random
import time
import os

tictactoe = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
win_setups = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
xvars = 8
yvars = 3
vars = []
x = {}
o = {}

game = 0


def print_tictac_matrix():
    print('+-----+-----+-----+')
    print('| ', tictactoe[0], ' | ', tictactoe[1], ' | ', tictactoe[2], ' |')
    print('+-----+-----+-----+')
    print('| ', tictactoe[3], ' | ', tictactoe[4], ' | ', tictactoe[5], ' |')
    print('+-----+-----+-----+')
    print('| ', tictactoe[6], ' | ', tictactoe[7], ' | ', tictactoe[8], ' |')
    print('+-----+-----+-----+')


def checkpos(x):
    if tictactoe[x] != 'X' and tictactoe[x] != 'O':
        return True
    else:
        return False


def checkboard():
    countx = 0
    counto = 0
    global vars
    global game
    vars = []
    v = 24
    for i in range(xvars):
        for j in range(yvars):
            if tictactoe[win_setups[i][j]] == 'X':
                countx += 1
                v -= 1
            elif tictactoe[win_setups[i][j]] == 'O':
                counto += 1
                v -= 1
            else:
                vars.append(win_setups[i][j])
        if countx < 2 and counto < 2:
            countx = 0
            counto = 0
        elif (countx == 2 and counto == 0) or (counto == 2 and countx == 0):
            vars = [vars[-1]]
            countx = 0
            counto = 0
            break
        elif ((countx == 2 and counto == 1) or (counto == 2 and countx == 1)) and v > 0:
            countx = 0
            counto = 0
        elif v == 0:
            game = 404
            print('Ничья')
        elif countx == 3:
            game = 1
            os.system('clear')
            print()
            print()
            time.sleep(.8)
            print('Поздравляю, ты победил!')
        elif counto == 3:
            game = 1
            os.system('clear')
            print()
            print()
            time.sleep(.8)
            print('Ты проиграл!')


while game == 0:
    os.system('clear')
    print()
    time.sleep(.4)
    print_tictac_matrix()
    print()
    choice = int(input("Введите номер ячейки с Х: ")) - 1
    if checkpos(choice):
        tictactoe[choice] = 'X'
        checkboard()
        if game != 404:
            tictactoe[int(random.choice(vars))] = 'O'
        else:
            os.system('clear')
            print()
            print()
            time.sleep(.8)
            print('Не осталось ходов, ничья')