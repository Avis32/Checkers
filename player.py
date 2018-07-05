
import pawn
import chessboard

class Player:
    """ color can be 'w' or 'b' """
    def __init__(self, choosen_color, chessboard):
        self.color = choosen_color
        self.chessboard = chessboard

    def player_turn(self):
        if self.color == 'w':
            print('White Player Turn')
        if self.color == 'b':
            print('Black Player Turn')
        #checking if input is numbers and if it has correct size
        while True:
            selected_coords = input("select_pawn")
            if selected_coords.isdigit():
                if len(selected_coords) == 2:
                    x, y=[int(selected_coords[0]), int(selected_coords[1])]
                    break
            else: # else nie potrzbeny
                print("invalid input:{}".format(selected_coords))
                self.player_turn()

        while True:
            # checking if selected input have Pawn in it
            if self.chessboard.is_pawn(coord_x=x, coord_y=y):
                #checking if color is same as a Player
                if self.chessboard.get_object_by_position(pos_x=x, pos_y=y).color == self.color:
                    if self.chessboard.is_move_possible(x, y):
                        self.chessboard.move_pawn(x, y)
                        break
                    else:
                        print('no possible movement')
                        self.player_turn()
                else:
                    self.player_turn()
            else:  # nie potrzebny
                print("invalid input")
                self.player_turn()
            break

