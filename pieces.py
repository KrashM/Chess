from enum import Enum

class Type(Enum):
    Pawn = 1
    Knight = 2
    Bishop = 3
    Rook = 4
    Queen = 5
    King = 6
    
class Color(Enum):
    White = 1
    Black = 2

class Piece:
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def get_move_list(self):
        raise NotImplementedError('Subclass should implement this method')

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, Type.Pawn)
        self.can_double_move = True

    def has_moved(self):
        self.can_double_move = False

    def get_move_list(self):
        return ([(0, 1), (0, 2)] if self.color == Color.White else [(0, -1), (0, -2)]) if self.can_double_move else ([(0, 1)] if self.color == Color.White else [(0, -1)])

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, Type.Knight)

    def get_move_list(self):
        return [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color, Type.Bishop)

    def get_move_list(self):
        return [val for sublist in [[(i, i) for i in range(1, 8)], [(-i, -i) for i in range(1, 8)], [(i, -i) for i in range(1, 8)], [(-i, i) for i in range(1, 8)]] for val in sublist]

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, Type.Rook)

    def get_move_list(self):
        return [val for sublist in [[(i, 0) for i in range(-7, 8)], [(0, i) for i in range(-7, 8)]] for val in sublist]

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color, Type.Queen)

    def get_move_list(self):
        return [val for sublist in [[(i, i) for i in range(1, 8)], [(-i, -i) for i in range(1, 8)], [(i, -i) for i in range(1, 8)], [(-i, i) for i in range(1, 8)], [(i, 0) for i in range(-7, 8)], [(0, i) for i in range(-7, 8)]] for val in sublist]

class King(Piece):
    def __init__(self, color):
        super().__init__(color, Type.King)

    def get_move_list(self):
        return [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]