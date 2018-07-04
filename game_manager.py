
import player
import chessboard


class Game_Manager:
    def __init__(self):

        self.chessboard=chessboard.Chessboard(8, 8)
        self.white_player = player.Player('w', self.chessboard)
        self.black_player = player.Player('b', self.chessboard)
        self.chessboard.set_pawns()

    def play(self):
        # gra raczej powinna trwac do czasu wygranej a nie w nieskonczonosc
        while True:
            self.chessboard.show_board()
            self.white_player.player_turn()
            self.chessboard.show_board()
            self.black_player.player_turn()

# zrob plik main, ktory bedzie mial ifa z mainem11
#https://docs.python.org/3/library/__main__.html11

c = Game_Manager()
c.play()
