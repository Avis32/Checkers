
import player
import chessboard


class Game_Manager:
    def __init__(self):

        self.chessboard = chessboard.Chessboard(8, 8)
        self.white_player = player.Player('w', self.chessboard)
        self.black_player = player.Player('b', self.chessboard)
        self.chessboard.set_pawns()

    def play(self):
        while True:
            self.chessboard.show_board()
            self.white_player.player_turn()
            if self.chessboard.is_white_player_won():
                print('White Player won')
                break
            self.chessboard.show_board()
            self.black_player.player_turn()
            if self.chessboard.is_black_player_won():
                print('Black Player won')
                break


c = Game_Manager()
c.play()
