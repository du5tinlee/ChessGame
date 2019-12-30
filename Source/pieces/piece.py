import typing
from tkinter import *
from typing import Generator, Tuple

if typing.TYPE_CHECKING:
    from cell import Cell


class Piece:
    IMAGE = 'images/w_pawn.png'

    def __init__(self, cell: 'Cell'):
        self._image = PhotoImage(file=self.IMAGE)
        self.cell = cell

    @property
    def image(self):
        return self._image

    @property
    def possible_moves(self) -> Generator[Tuple[int, int], None, None]:
        raise NotImplementedError

    def move_consequence(self, move):
        pass
