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

        print(initSq, destSq, self.board[initSq], chr(self.board[initSq][0]))
        
        if not chr(self.board[initSq][0]) == ('W', 'B')[self.turn]:
            raise GameError('No pawn or pawn of the adversary at initSq')

        if chr(self.board[destSq][0]) == ('W', 'B')[self.turn]:
            raise GameError('There is already a pawn at destSq')

        self.board[destSq] = self.board[initSq]
        self.board[initSq] = '00'

        self.turn = (self.turn + 1) % 2
        

    @property
    def emojiBoard(self):
        board = self.board.tolist()

        for x in range(self.BOARDSIZE):
            for y in range(self.BOARDSIZE):
                if board[x][y] == b'00':
                    board[x][y] = ('⬜', '⬛')[(x + y) % 2]
                    continue
                
                board[x][y] = board[x][y].decode("utf-8")


        return board

class GameError(Exception):
    pass

def gridprint(list2d):
    print(*list2d, sep='\n')


if __name__ == "__main__":
    game = ChessGame()
    gridprint(game.emojiBoard)
    
    print('White turn!')
    game.playerMove(0, input('initSq: '), input('destSq: '))

    print('Black turn!')
    game.playerMove(1, input('initSq: '), input('destSq: '))
