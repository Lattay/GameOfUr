from random import random

from board import Board, Moves
from players import NaivePlayer, OtherNaivePlayer, HumanPlayer


def roll_dices():
    return sum(random() > 0.5 for i in range(4))


def bot_vs_bot_loop():
    b = Board()
    p1 = OtherNaivePlayer(0, b)
    p2 = NaivePlayer(1, b)

    end = False
    lock = 0
    c = 0

    b.draw_board()
    while not end:
        c += 1
        print('\n========== Turn', c)
        print('\n########## Player 1 turn')
        replay = True
        while replay:
            replay = False
            dices = roll_dices()
            print('Here is a', dices, '!')
            if dices > 0:
                pawn = p1.play(dices)
                if pawn != -1:
                    lock = 0
                    res = b.play(p1.me, pawn, dices)
                    if res == Moves.WIN:
                        print('Player 1 Won')
                        end = True
                    elif res == Moves.REPLAY:
                        replay = True
                    b.draw_board()
                else:
                    lock += 1
                    print('Player 1 cannot play.')
            else:
                print('Player 1 do nothing.')

        if not end:
            print('\n########## Player 2 turn')
            replay = True
            while replay:
                replay = False
                dices = roll_dices()
                print('Here is a', dices, '!')
                if dices > 0:
                    pawn = p2.play(dices)
                    if pawn != -1:
                        lock = 0
                        res = b.play(p2.me, pawn, dices)
                        if res == Moves.WIN:
                            print('Player 2 Won')
                            end = True
                        elif res == Moves.REPLAY:
                            replay = True
                        b.draw_board()
                    else:
                        lock += 1
                        print('Player 2 cannot play.')
                else:
                    print('Player 2 do nothing.')
        if lock >= 10:
            end = True
            print('This was a deadlock !')


def bot_vs_human_loop():
    b = Board()
    p1 = OtherNaivePlayer(0, b)
    p2 = HumanPlayer(1, b)

    end = False
    lock = 0
    c = 0

    b.draw_board()
    while not end:
        c += 1
        print('\n========== Turn', c)
        print('\n########## Player 1 turn')
        replay = True
        while replay:
            replay = False
            dices = roll_dices()
            print('Here is a', dices, '!')
            if dices > 0:
                pawn = p1.play(dices)
                if pawn != -1:
                    lock = 0
                    res = b.play(p1.me, pawn, dices)
                    if res == Moves.WIN:
                        print('Player 1 Won')
                        end = True
                    elif res == Moves.REPLAY:
                        replay = True
                    b.draw_board()
                else:
                    lock += 1
                    print('Player 1 cannot play.')
            else:
                print('Player 1 do nothing.')

        if not end:
            print('\n########## Player 2 turn')
            replay = True
            while replay:
                replay = False
                dices = roll_dices()
                print('Here is a', dices, '!')
                if dices > 0:
                    pawn = p2.play(dices)
                    if pawn != -1:
                        lock = 0
                        res = b.play(p2.me, pawn, dices)
                        if res == Moves.WIN:
                            print('Player 2 Won')
                            end = True
                        elif res == Moves.REPLAY:
                            replay = True
                        b.draw_board()
                    else:
                        lock += 1
                        print('You cannot do anything.')
                else:
                    print('You do nothin.')
        if lock >= 10:
            end = True
            print('This was a deadlock !')


if __name__ == '__main__':
    bot_vs_human_loop()
