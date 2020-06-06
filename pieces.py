from abc import ABC, abstractmethod
from enum import Enum
import numpy as np
import re

class Color(Enum):
    WHITE = 0
    BLACK = 1

class GameError(Exception):
    pass

class Piece(ABC):
    def __init__(self, color):
        self.COLOR = color

    def __repr__(self):
        return ('W', 'B')[self.COLOR.value] + type(self).__name__[0]
        # return '\n<{} at {}>'.format(type(self).__name__, self.position)

    @abstractmethod
    def checkIfValid(self, initSq, destSq, color):
        if initSq == destSq:
            raise GameError('You need to move the pawn')

        color = str(initSq)

        if self.COLOR != color:
            raise GameError('No pawn or pawn of the adversary at initSq')

        if chr(self.board[destSq][0]) == ('W', 'B')[turn]:
            raise GameError('There is already one of your pawn at destSq')


class Pawn(Piece):
    def __init__(self, position, color):
        super().__init__(position, type(self).__name__, color)
        self.hasMoved = False

    def checkIfValid(self, initSq, destSq, color):
        super().checkIfValid(initSq, destSq, color)

        # check for pawn specific move and return the squares that need to be empty to be a valid move

