from abc import ABC, abstractmethod
from enum import Enum
import numpy as np
import re

class GameError(Exception):
    pass

class Piece(ABC):
    def __init__(self, color):
        self.COLOR = color

    def __repr__(self):
        return self.COLOR + type(self).__name__[0]
        # return ('W', 'B')[self.COLOR.value] + type(self).__name__[0]
        # return '\n<{} at {}>'.format(type(self).__name__, self.position)

    @abstractmethod
    def checkIfValid(self, initSq, destSq, color):
        print('Piece.checkIfValid', initSq, destSq)
        if initSq == destSq:
            raise GameError('You need to move the piece')

        if self.COLOR != color:
            # We already checked for empty square in board.py
            raise GameError('Piece of the adversary at initSq')


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.hasMoved = False

    def checkIfValid(self, initSq, destSq, color):
        super().checkIfValid(initSq, destSq, color)

        # check for pawn specific move and return the squares that need to be empty to be a valid move

        dx = destSq[1] - initSq[1]
        dy = destSq[0] - initSq[0]

        if abs(dx) < 2 and abs(dy) < 2:
            return

        return ((initSq[0]+(destSq[0]-initSq[0])//2, initSq[1]),)