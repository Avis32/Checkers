
import pawn
import chessboard

class Player:
    def __init__(self, choosen_color, chessboard):
        # czemu player jest z duzej?
        # sama nazwa color wystarczy, nie musisz dodawac palyer zeby wszycy wiedzieli ze to kolor gracza
        self.color=choosen_color
        self.chessboard=chessboard

    def player_turn(self):

        
        """        
        while True:
            cords_from_input = input("select_pawn")
            if len(cords_from_input) != 2:
                print('Wrong number of cords')
                continue
            x, y = cords_from_input
            if x.isdigit() and y.isdigit:
                break
            print("invalid input")
        
        cos takiegoe
        """
        #checking if input is numbers and if it has correct size
        while True:
            selected_coords = input("select_pawn")
            if selected_coords.isdigit():
                if len(selected_coords) == 2:
                    x, y=[int(selected_coords[0]), int(selected_coords[1])]
                    print('pawn selected')
                    break
            else: # else nie potrzbeny
                print("invalid input:{}".format(selected_coords))
                continue

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
                        continue
                else:
                    self.player_turn()
            else:  # nie potrzebny
                print("invalid input")
                continue
            break

