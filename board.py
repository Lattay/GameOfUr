class Moves:
    NOP = 1  # nothing special, the turn is over
    REPLAY = 2  # play again
    OUT = 3  # you got one of the foo stone out
    IN = 4  # you got one of your pawn home
    WIN = 5  # all of your pawns are home


class Board:

    def __init__(self):
        self.pawns = ([], [])
        self.pawn_left = [7, 7]

    def create_copy(self):
        copy = Board()
        copy.pawns[0] = self.pawns[0].copy()
        copy.pawns[1] = self.pawns[1].copy()
        copy.pawn_left = self.pawn_left.copy()
        return copy

    def abort_if_not_meaningful(self, player, pawn, move):
        tested = "Player {}, pawn {}, move {}".format(player+1, pawn, move)
        assert player == 0 or player == 1, "No such player " + tested
        assert 0 <= pawn < len(self.pawns[player]) or \
            pawn == 7, "No such pawn " + tested
        # assert 0 not in self.pawns[player][:pawn], (
        #         "No yet playable pawn " +
        #         tested)
        assert move > 0, "Negative move " + tested

    def is_valid(self, player, pawn, move):
        self.abort_if_not_meaningful(player, pawn, move)

        if pawn < 7:
            newpos = self.pawns[player][pawn]+move
        else:
            newpos = move
        return newpos <= 15 and (
                                 all(pos2 != newpos
                                     or pos2 != 8
                                     for pos2 in self.pawns[1-player])
                                 and all(pos2 != newpos
                                         for pos2 in self.pawns[player]))

    def sim_move(self, player, pawn, move):
        assert self.is_valid(player, pawn, move), "Forbiden move"

        if pawn < 7:
            newpos = self.pawns[player][pawn]+move
        else:
            newpos = move
        if newpos == 15:
            return (
                    (Moves.WIN, 0) if sum(self.pawns[player]) == 90
                    else (Moves.IN, 0)
            )
        else:
            if newpos == 4 or newpos == 8 or newpos == 14:
                return (Moves.REPLAY, newpos)
            elif 5 <= newpos <= 12:
                for pos in self.pawns[1-player]:
                    if pos == newpos:
                        return (Moves.OUT, newpos)
            return (Moves.NOP, newpos)

    def play(self, player, pawn, move):
        assert self.is_valid(player, pawn, move), "Forbiden move"

        if pawn == 7:
            pawn = len(self.pawns[player])
            self.pawn_left[player] -= 1
            self.pawns[player].append(move)
        else:
            self.pawns[player][pawn] += move

        newpos = self.pawns[player][pawn]
        if newpos == 15:
            self.pawns[player].pop(pawn)
            return (
                    Moves.WIN if (self.pawn_left[player] +
                                  len(self.pawns[player])) == 0
                    else Moves.IN
            )
        else:
            if newpos == 4 or newpos == 8 or newpos == 14:
                return Moves.REPLAY
            elif 5 <= newpos <= 12:
                for p, pos in enumerate(self.pawns[1-player]):
                    if pos == newpos:
                        self.pawns[1-player].pop(p)
                        self.pawn_left[1-player] += 1
                        return Moves.OUT
            return Moves.NOP

    def get_pawns(self, player):
        pawns = list(enumerate(self.pawns[player]))
        pawns.sort(key=lambda t: -t[1])
        if self.pawn_left[player] > 0:
            pawns.append((7, 0))
        return pawns

    def draw_board(self):

        # top border
        print("\n/-------\\   /---\\")

        # top line, player 1 home
        for i in (4, 3, 2, 1, 14, 13):
            print('|', end='')
            if i in self.pawns[0]:
                print('1', end='')
            elif i == 4 or i == 14:
                print('*', end='')
            else:
                print(' ', end='')
            if i == 1:
                print('|   ', end='')
        print('|')

        # first middle border
        print("|---------------|")

        # middle line
        for i in range(5, 13):
            print('|', end='')
            if i in self.pawns[0]:
                print('1', end='')
            elif i in self.pawns[1]:
                print('2', end='')
            elif i == 8:
                print('*', end='')
            else:
                print(' ', end='')
        print('|')

        # second middle border
        print("|---------------|")

        # bottom line, player 2 home
        for i in (4, 3, 2, 1, 14, 13):
            print('|', end='')
            if i in self.pawns[1]:
                print('2', end='')
            elif i == 4 or i == 14:
                print('*', end='')
            else:
                print(' ', end='')
            if i == 1:
                print('|   ', end='')
        print('|')

        # bottom border
        print("\\-------/   \\---/")
        p1score = 7 - self.pawn_left[0] - len(self.pawns[0])
        p2score = 7 - self.pawn_left[1] - len(self.pawns[1])
        print("Player 1] {:2} - {:2} [Player 2".format(p1score, p2score))
        print(self.pawns)
