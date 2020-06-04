import numpy as np
import re

class ChessGame():
    def __init__(self):
        self.BOARDSIZE = 8
        self.turn = 0

        # init board and initial pawn places
        self.board = np.full((self.BOARDSIZE, self.BOARDSIZE), '00', dtype='|S2')
        self.board[0] = ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']
        self.board[7] = ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
        self.board[1] = ['BP'] * self.BOARDSIZE
        self.board[6] = ['WP'] * self.BOARDSIZE

    def playerMove(self, color, initSq, destSq):
        if self.turn != color:
            raise GameError("Not this player's turn")

        initSq = initSq.lower()
        destSq = destSq.lower()

        if (not re.match('[a-h][1-8]$', initSq)
            or not re.match('[a-h][1-8]$', destSq)):
            raise GameError('Bad coordinates')
        
        initSq = (self.BOARDSIZE-int(initSq[1]), ord(initSq[0])-ord('a'))
        destSq = (self.BOARDSIZE-int(destSq[1]), ord(destSq[0])-ord('a'))

        if initSq == destSq:
            raise GameError('You need to move the pawn')
        
        if not chr(self.board[initSq][0]) == ('W', 'B')[self.turn]:
            raise GameError('No pawn or pawn of the adversary at initSq')

        if chr(self.board[destSq][0]) == ('W', 'B')[self.turn]:
            raise GameError('There is already one of your pawn at destSq')

        if self.fordiddenMoves(self.board[initSq], initSq, destSq):
            raise GameError('Forbidden move for this type of pawn')

        self.board[destSq] = self.board[initSq]
        self.board[initSq] = '00'

        self.turn = (self.turn + 1) % 2

    def pawnLogic(self, dx, dy, pawn, initSq, destSq, side):
        if dx == 1 and dy == side and self.board[destSq] != b'00':
            return False
        elif dx != 0 or self.board[destSq] != b'00':
            return True
        elif dy == side*2 and initSq[0] == int(-2.5*side + 3.5):
            return False
        elif dy == side:
            return False
        return True

    def fordiddenMoves(self, pawn, initSq, destSq):
        dy = destSq[0]-initSq[0]
        dx = abs(destSq[1]-initSq[1])
        print(pawn, dx, dy)

        if pawn == b'WP':
            return self.pawnLogic(dx, dy, pawn, initSq, destSq, -1)
            
        elif pawn == b'BP':
            return self.pawnLogic(dx, dy, pawn, initSq, destSq, 1)
        
        pawn = chr(pawn[1])
        dy = abs(dy)

        if pawn == 'R':
            if dx != 0 and dy != 0:
                return True
        elif pawn == 'N':
            if not((dx==1 and dy==2) or (dx==2 and dy==1)):
                return True
        elif pawn == 'B':
            if dx != dy:
                return True
        elif pawn == 'Q':
            if np.arctan(dy/dx) % (np.pi/4) != 0.0:
                return True
        elif pawn == 'K':
            if not(dx < 2 and dy < 2):
                return True
        else:
            raise GameError('Unknown pawn')

        return False

    @property
    def emojiBoard(self):
        board = self.board.tolist()

        for x in range(self.BOARDSIZE):
            for y in range(self.BOARDSIZE):
                if board[x][y] == b'00':
                    board[x][y] = ('⬛', '⬜')[(x + y) % 2]
                    continue
                
                board[x][y] = board[x][y].decode("utf-8")

                # board[x][y] = (board[x][y]
                #     .replace('BB', '<:BB:717894296396890154>')
                #     .replace('BK', '<:BK:717894296459542587>')
                #     .replace('BN', '<:BN:717894296329781250>')
                #     .replace('BP', '<:BP:717894296572788787>')
                #     .replace('BQ', '<:BQ:717894296409473047>')
                #     .replace('BR', '<:BR:717894296870584320>')
                #     .replace('WB', '<:WB:717894297109659748>')
                #     .replace('WK', '<:WK:717894296673452041>')
                #     .replace('WN', '<:WN:717894296698617877>')
                #     .replace('WP', '<:WP:717894296992219176>')
                #     .replace('WQ', '<:WQ:717894296967315517>')
                #     .replace('WR', '<:WR:717894296807931984>'))

        return '\n'.join(''.join(row) for row in board)

class GameError(Exception):
    pass

if __name__ == "__main__":
    game = ChessGame()
    print(game.emojiBoard)
    
    while 1:
        print('White turn!')
        game.playerMove(0, input('initSq: '), input('destSq: '))
        print(game.emojiBoard)

        print('Black turn!')
        game.playerMove(1, input('initSq: '), input('destSq: '))
        print(game.emojiBoard)
    