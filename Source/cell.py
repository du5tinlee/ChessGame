from tkinter import *
from pieces.piece import Piece
from typing import Optional


class Cell:
    FONT: str = 'Calibri 10 bold'
    SIZE: int = 64
    IMAGE: str = 'images/empty.png'

    def __init__(self, tk: Tk, x: int, y: int):
        self._tk = tk
        self.piece: Optional[Piece] = Piece(self)
        self.X = x
        self.Y = y

        self.button = Button(self._tk, font=self.FONT, height=self.SIZE, width=self.SIZE, command=self._pressed)
        self.button.grid(row=y, column=x)
        self.button.configure(image=PhotoImage(file=self.IMAGE))

    def assign_piece(self, piece: Piece):
        self.piece = piece
        self.button.configure(image=self.piece.image)

    def _pressed(self):
        pass
