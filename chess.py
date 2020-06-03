from enum import Enum
import numpy as np

class Color(Enum):
    WHITE = 0
    BLACK = 1

class ChessGame():
    def __init__(self):
        self.BOARDSIZE = 8
        self.turn = Color.WHITE

        # init board and initial pawn places
        # self.board = [[None for x in range(self.BOARDSIZE)] for y in range(self.BOARDSIZE)]
        self.board = np.full((self.BOARDSIZE, self.BOARDSIZE), '00', dtype='|S2')
        self.board[0, 4] = 'BK'
        self.board[1] = ['BP'] * self.BOARDSIZE
        self.board[6] = ['WP'] * self.BOARDSIZE

    def playerMove(self, color, initialSquare, destinationSquare):
        pass

    @property
    def emojiBoard(self):
        board = self.board.tolist()

        for x in range(self.BOARDSIZE):
            for y in range(self.BOARDSIZE):
                if board[x][y] == b'00':
                    board[x][y] = ['⬜', '⬛'][(x + y) % 2]
                    continue
                
        
        return board

def gridprint(list2d):
    print(*list2d, sep='\n')


if __name__ == "__main__":
    game = ChessGame()
    gridprint(game.emojiBoard)
