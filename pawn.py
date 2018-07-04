

class Pawn:

    """ color can be 'w' or 'b' """
    def __init__(self, color, id_number):
        self.color = color
        self.id_nmb=id_number
        if self.color=='w':
            self.move_offset =[[1, 1], [-1, 1]]
        else:
            self.move_offset = [[1, -1], [-1, -1]]
        self.attack_offset=[[1, 1], [-1, 1], [1, -1], [-1, -1]]

    # w obecnym zalozeniu, to chessboard powinnien to ogarniac.

    # w obecnym zalozeniu, to chessboard powinnien to ogarniac.
