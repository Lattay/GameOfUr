from random import randint
from board import Moves

C_4_n = (1, 4, 6, 4, 1)


class Player:

    def __init__(self, num, board):
        self.board = board
        self.me = num

    def get_moves(self, dices):
        pawns = self.board.get_pawns(self.me)
        moves = []
        for num, pos in pawns:
            if self.board.is_valid(self.me, num, dices):
                moves.append(num)
        return moves


class NaivePlayer(Player):

    def score_move(self, pawn, dices):
        res, pos = self.board.sim_move(self.me, pawn, dices)
        if res == Moves.WIN:
            return 15
        elif res == Moves.IN:
            return 7 - C_4_n[dices]
        elif res == Moves.OUT:
            return pos + dices
        elif res == Moves.REPLAY:
            return dices + 4
        else:
            return dices

    def play(self, dices):
        moves = self.get_moves(dices)
        best_moves = []
        best_score = -1
        for pawn in moves:
            score = self.score_move(pawn, dices)
            if score > best_score:
                best_score = score
                best_moves = [pawn]
            elif score == best_score:
                best_moves.append(pawn)

        print("Moves", moves)
        if best_moves:
            return best_moves[randint(0, len(best_moves)-1)]
        else:
            return -1


class OtherNaivePlayer(NaivePlayer):

    def score_move(self, pawn, dices):
        res, pos = self.board.sim_move(self.me, pawn, dices)
        if res == Moves.WIN:
            return 30
        elif res == Moves.IN:
            return 26
        elif res == Moves.OUT:
            return pos + dices + 7
        elif res == Moves.REPLAY:
            return dices + 4
        else:
            return dices - (pawn == 7)


def is_valid_index(s, l):
    if s == '':
        return False
    elif not s.isdigit():
        return False
    elif int(s) >= l:
        return False
    else:
        return True


class HumanPlayer(Player):

    def get_moves(self, dices):
        pawns = self.board.get_pawns(self.me)
        moves = []
        for num, pos in pawns:
            if self.board.is_valid(self.me, num, dices):
                moves.append((num, pos))
        return moves

    def play(self, dices):
        moves = self.get_moves(dices)
        if len(moves) == 0:
            return -1
        print('Which pawn would you like to move ?')
        for i, (num, pos) in enumerate(moves):
            if num == 7:
                print('- Add a new pawn on the board ? Hit {}.'.format(i))
            else:
                print('- Pawn {} at position {} ? Hit {}.'.format(num, pos, i))
        rep = ''
        while not is_valid_index(rep, len(moves)):
            rep = input('> ')
        return moves[int(rep)][0]
