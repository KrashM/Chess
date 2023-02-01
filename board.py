from pieces import Piece

class Board:
    def __init__(self) -> None:
        self.board = [[None for _ in range(8)] for _ in range(8)]

    def set_piece(self, symbol: str, x: int, y: int) -> None:
        self.board[y][x] = Piece.get_piece(symbol)
    
    def print_board(self) -> None:
        for i in range(8):
            print(', '.join(map(str, self.board[i])))