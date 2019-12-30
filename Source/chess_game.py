from tkinter import *
from cell import Cell
from pieces import King

import typing
if typing.TYPE_CHECKING:
    from typing import Dict, Tuple


class ChessGame:
    ROWS: int = 8
    COLUMNS: int = 8
    PLAYER_W: str = 'W'
    PLAYER_B: str = 'B'
    STARTING_PLAYER: str = PLAYER_W

    def __init__(self):
        self._tk: Tk = Tk()
        self._tk.resizable(False, False)
        self._current_player = self.STARTING_PLAYER
        self._cells: Dict[Tuple[int, int], Cell] = {}
        for y in range(self.ROWS):
            for x in range(self.COLUMNS):
                self._cells[x, y] = Cell(self._tk, x, y)
        self.setup_pieces()

    def run(self):
        self._tk.mainloop()

    def setup_pieces(self):
        self._cells[0, 0].assign_piece(King(self._cells[0, 0]))

    def switch_player(self):
        if self._current_player == self.PLAYER_W:
            self._current_player = self.PLAYER_B
        else:
            self._current_player = self.PLAYER_W
