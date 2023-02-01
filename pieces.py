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
    def __init__(self, color: Color, type: Type) -> None:
        self.color = color
        self.type = type
        
    def __str__(self) -> str:
        str = ''

        if self.color == Color.White:
            str = 'W'
        else:
            str = 'B'

        if self.type == Type.Pawn:
            str += 'P'
        elif self.type == Type.Knight:
            str += 'N'
        elif self.type == Type.Bishop:
            str += 'B'
        elif self.type == Type.Rook:
            str += 'R'
        elif self.type == Type.Queen:
            str += 'Q'
        elif self.type == Type.King:
            str += 'K'

        return str

    @staticmethod
    def get_piece(symbol: str):
        if(symbol == 'p'):
            return Pawn(Color.Black)
        elif(symbol == 'r'):
            return Rook(Color.Black)
        elif(symbol == 'n'):
            return Knight(Color.Black)
        elif(symbol == 'b'):
            return Bishop(Color.Black)
        elif(symbol == 'q'):
            return Queen(Color.Black)
        elif(symbol == 'k'):
            return King(Color.Black)
        elif(symbol == 'P'):
            return Pawn(Color.White)
        elif(symbol == 'R'):
            return Rook(Color.White)
        elif(symbol == 'N'):
            return Knight(Color.White)
        elif(symbol == 'B'):
            return Bishop(Color.White)
        elif(symbol == 'Q'):
            return Queen(Color.White)
        elif(symbol == 'K'):
            return King(Color.White)

    def get_move_list(self) -> list:
        raise NotImplementedError('Subclass should implement this method')

class Pawn(Piece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, Type.Pawn)
        self.can_double_move = True

    def has_moved(self) -> None:
        self.can_double_move = False

    def get_move_list(self) -> list:
        return ([(0, 1), (0, 2)] if self.color == Color.White else [(0, -1), (0, -2)]) if self.can_double_move else ([(0, 1)] if self.color == Color.White else [(0, -1)])

class Knight(Piece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, Type.Knight)

    def get_move_list(self) -> list:
        return [(1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

class Bishop(Piece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, Type.Bishop)

    def get_move_list(self) -> list:
        return [val for sublist in [[(i, i) for i in range(1, 8)], [(-i, -i) for i in range(1, 8)], [(i, -i) for i in range(1, 8)], [(-i, i) for i in range(1, 8)]] for val in sublist]

class Rook(Piece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, Type.Rook)

    def get_move_list(self) -> list:
        return [val for sublist in [[(i, 0) for i in range(-7, 8)], [(0, i) for i in range(-7, 8)]] for val in sublist]

class Queen(Piece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, Type.Queen)

    def get_move_list(self) -> list:
        return [val for sublist in [[(i, i) for i in range(1, 8)], [(-i, -i) for i in range(1, 8)], [(i, -i) for i in range(1, 8)], [(-i, i) for i in range(1, 8)], [(i, 0) for i in range(-7, 8)], [(0, i) for i in range(-7, 8)]] for val in sublist]

class King(Piece):
    def __init__(self, color: Color) -> None:
        super().__init__(color, Type.King)

    def get_move_list(self) -> list:
        return [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]