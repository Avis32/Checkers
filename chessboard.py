import pawn


class Chessboard:
    """"chessboard_positions is 2 dimensional dictionary, first index is x and the second is y
    [x,y]"""

    def __init__(self, size_x, size_y): #spacje wszedzie
        self.size_x=size_x
        self.size_y = size_y
        # self.bottom_coords = ''
        self.bottom_coords = str()
        self._chessboard={}
        for x_coord in range(size_x):
            for y_coord in range(size_y):
                self._chessboard[(x_coord + 1, y_coord + 1)]=None

        # zamiast printow mozesz podepnac sobie biblioteke logger
        print("map has been created")
        print(self._chessboard)

#get i bez dict
# lepiej, poczytaj o getterach i setterach
    def get_chessboard_positions(self):
        return self._chessboard

    def set_pawns(self):
        id_numb = 0
        # odstepy pomeidzy zmiennymi PEP-8/ pobaw sie pylint'em
        for x, y in self._chessboard:
            id_numb += 1
            """ Im mniej zagniezdzen tym kod bardziej czytelny
            Nie wiem po co ten warunek jest. Upewnij sie czy nie rpzekombinowales
            if (x+y)%2!=0:
                continue
            if y<self.size_y/2:
                self._chessboard_positions[x, y]= Pawn.Pawn('w') # Pawn.Pawn(color='w')
            if y>self.size_y/2+1:
                self._chessboard_positions[x, y] = Pawn.Pawn('b')
            """
            if (x+y) % 2 == 0:
                if y < self.size_y / 2:
                    # Jesli pionek ma wlasciwosc kolor, zadeklaruj jakies zmienne w pliku z pionkami ktory bedzie trzymal ten kolor tj:
                    # WHITE = 'w'
                    # BLACK = 'b'
                    # jako ze to sa jedyne kolory jakie moga byc, mozesz te zmienne zadeklarowac jako zmienne klasy
                    self._chessboard[x, y] = pawn.Pawn(color = 'w', id_number = id_numb)
                if y > self.size_y/2+1:
                    self._chessboard[x, y] = pawn.Pawn(color = 'b', id_number = id_numb)

    def show_board(self):
        for y in range(1, self.size_y+1):
            print("\n")
            print(y, sep=" ", end="::", flush=False)
            for x in range(1, self.size_x+1):
                if not self._chessboard[x, y]: # Jesli checcboard nie bedzie mial 0, mozesz uzyc if not
                    print("x", sep=" ", end=" ", flush=False)
                else:
                    print(self._chessboard[x, y].color, sep=' ', end=' ', flush=False)

        # Zamiast robic jakas magie z printami, plus flush, mozesz zrobic zwyczajnie zmienna ktora Ci to przechowa
        # for y in range(1, self.size_y+1):
        #     row = ''
        #     for x in range(1, self.size_x+1):
        #         field = self._chessboard_positions[x, y]
        #         row += ' '.join('x' if not field else field.color)
        #     print(row)
        # To jest pseudo kod, nie testowalem

    def get_position_by_id_number(self, id_number):
        # get position of pawn by id number
        pass

    def get_object_by_position(self, pos_x, pos_y):
        return self._chessboard[pos_x, pos_y]

    def is_pawn(self, coord_x, coord_y):
        if self._chessboard[coord_x, coord_y] is not None:
            return True
        else:
            return False

    def is_input_valid(self, x, y):
        if x <= 0 or y <= 0:
            return False
        if x > self.size_x or y > self.size_y:
            return False
        return True

    def get_possible_attacks(self, sel_x, sel_y):
        possible_attacks = []
        for attack_x, attack_y in self._chessboard[sel_x, sel_y].attack_offset:
            if self.is_input_valid(sel_x+attack_x,sel_y+attack_y):
                if self._chessboard[sel_x + attack_x, sel_y + attack_y] is not None:
                    if self._chessboard[sel_x + attack_x, sel_y + attack_y].color != self._chessboard[sel_x, sel_y].color:
                        if self.is_input_valid(sel_x + attack_x, sel_y + attack_y):
                            if self._chessboard[sel_x + attack_x+(attack_x/abs(attack_x)), sel_y + attack_y+(attack_y/abs(attack_y))] is None:
                                possible_attacks.append([sel_x + attack_x + (attack_x/abs(attack_x)), sel_y + attack_y + (attack_y / abs(attack_y))])
        return possible_attacks

    def get_possible_moves(self,sel_x, sel_y):
        possible_moves = []
        for move_x, move_y in self._chessboard[sel_x, sel_y].move_offset:
            if self.is_input_valid(sel_x+move_x, sel_y+move_y):
                if self._chessboard[sel_x+move_x, sel_y+move_y] is None:
                    possible_moves.append([sel_x + move_x, sel_y + move_y])
        return possible_moves

    def is_move_possible(self, sel_x, sel_y):
        #I could call get_possible_moves and get possible attack and check if they are empty but this seems more resource friendly
        for move_x, move_y in self._chessboard[sel_x, sel_y].move_offset:
            if self.is_input_valid(sel_x+move_x, sel_y+move_y):
                if self._chessboard[sel_x+move_x, sel_y+move_y] is None:
                    return True
        for attack_x, attack_y in self._chessboard[sel_x, sel_y].attack_offset:
            if self.is_input_valid(sel_x+attack_x,sel_y+attack_y):
                if self._chessboard[sel_x + attack_x, sel_y + attack_y] is not None:
                    if self._chessboard[sel_x + attack_x, sel_y + attack_y].color != self._chessboard[sel_x, sel_y].color:
                        if self.is_input_valid(sel_x + attack_x, sel_y + attack_y):
                            if self._chessboard[sel_x + attack_x+(attack_x/abs(attack_x)), sel_y + attack_y+(attack_y/abs(attack_y))] is None:
                                return True
        return False

    def move_pawn(self, sel_x, sel_y):
        possible_moves = self.get_possible_moves(sel_x, sel_y)
        possible_attacks = self.get_possible_attacks(sel_x, sel_y)
        print(possible_moves)
        print(possible_attacks)
        destination = input('where?: ')
        dest_x, dest_y = [int(destination[0]), int(destination[1])]
        if [dest_x, dest_y] in possible_moves:
            self._chessboard[dest_x, dest_y] = self._chessboard[sel_x, sel_y]
            self._chessboard[sel_x, sel_y] = None
        if [dest_x, dest_y] in possible_attacks:
            self._chessboard[dest_x, dest_y] = self._chessboard[sel_x, sel_y]
            self._chessboard[sel_x, sel_y] = None
