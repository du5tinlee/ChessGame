from .piece import Piece
from typing import Generator, Tuple


class Queen(Piece):
    IMAGE = 'images/w_queen.png'

    @property
    def possible_moves(self) -> Generator[Tuple[int, int], None, None]:
        yield (self.cell.X + 1, self.cell.Y)
