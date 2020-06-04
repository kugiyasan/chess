import unittest
from chess import ChessGame, GameError

class TestChessGame(unittest.TestCase):

    def test_game_start(self):
        game = ChessGame()
        self.assertEqual(game.emojiBoard, 
            'BRBNBBBQBKBBBNBR\nBPBPBPBPBPBPBPBP\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\nWPWPWPWPWPWPWPWP\nWRWNWBWQWKWBWNWR')

        with self.assertRaises(GameError):
            game.playerMove(1, 'e2', 'e4')
            game.playerMove(1, 'g7', 'g6')
            
        game.playerMove(0, 'e2', 'e4')


if __name__ == '__main__':
    unittest.main()