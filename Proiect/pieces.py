import tkinter as tk
import pydoc

def is_in_table(i, j):
    if i < 0:
        return False
    if i > 7:
        return False
    if j < 0:
        return False
    if j > 7:
        return False
    return True


class Piece:
    def __init__(self, position):
        self.name = "empty"
        self.position = position
        self.selected = False
        self.highlighted = False

    def get_moves(self):
        """
            method to get possible moves of this type of piece
            (possible, but not necessarily correct because the table is unknown here)
        """
        pass


class Pawn(Piece):
    def __init__(self, piece_c, position):
        super().__init__(position)
        self.name = 'pawn'
        self.piece_color = piece_c
        self.image = tk.PhotoImage(file=f"pieces/{self.name}{self.piece_color}.png")

    def get_moves(self):
        x = self.position[0]
        y = self.position[1]
        moves = []

        if self.piece_color == "black":
            if x + 1 <= 7:
                moves.append((x + 1, y))

            # if the pawn is in the initial position
            if x == 1:
                moves.append((x + 2, y))
        else:
            if x - 1 >= 0:
                moves.append((x - 1, y))

            # if the pawn is in the initial position
            if x == 6:
                moves.append((x - 2, y))

        return [moves]


class Bishop(Piece):
    def __init__(self, piece_c, position):
        super().__init__(position)
        self.name = 'bishop'
        self.piece_color = piece_c
        self.image = tk.PhotoImage(file=f"pieces/{self.name}{self.piece_color}.png")

    def get_moves(self):
        moves = []
        directions = [(-1, +1), (+1, +1), (+1, -1), (-1, -1)]

        for k in range(len(directions)):
            x = self.position[0] + directions[k][0]
            y = self.position[1] + directions[k][1]
            liniar_moves = []

            while is_in_table(x, y):
                liniar_moves.append((x, y))
                x += directions[k][0]
                y += directions[k][1]

            if len(liniar_moves) > 0:
                moves.append(liniar_moves)
        return moves


class Rock(Piece):
    def __init__(self, piece_c, position):
        super().__init__(position)
        self.name = 'rock'
        self.piece_color = piece_c
        self.image = tk.PhotoImage(file=f"pieces/{self.name}{self.piece_color}.png")
        self.initial_position = True

    def get_moves(self):
        moves = []
        directions = [(-1, 0), (0, +1), (+1, 0), (0, -1)]

        for k in range(len(directions)):
            x = self.position[0] + directions[k][0]
            y = self.position[1] + directions[k][1]
            liniar_moves = []

            while is_in_table(x, y):
                liniar_moves.append((x, y))
                x += directions[k][0]
                y += directions[k][1]

            if len(liniar_moves) > 0:
                moves.append(liniar_moves)
        return moves


class Queen(Piece):
    def __init__(self, piece_c, position):
        super().__init__(position)
        self.name = 'queen'
        self.piece_color = piece_c
        self.image = tk.PhotoImage(file=f"pieces/{self.name}{self.piece_color}.png")

    def get_moves(self):
        moves = []
        directions = [(-1, +1), (+1, +1), (+1, -1), (-1, -1), (-1, 0), (0, +1), (+1, 0), (0, -1)]

        for k in range(len(directions)):
            x = self.position[0] + directions[k][0]
            y = self.position[1] + directions[k][1]
            liniar_moves = []

            while is_in_table(x, y):
                liniar_moves.append((x, y))
                x += directions[k][0]
                y += directions[k][1]

            if len(liniar_moves) > 0:
                moves.append(liniar_moves)
        return moves


class Knight(Piece):
    def __init__(self, piece_c, position):
        super().__init__(position)
        self.name = 'knight'
        self.piece_color = piece_c
        self.image = tk.PhotoImage(file=f"pieces/{self.name}{self.piece_color}.png")

    def get_moves(self):
        directions = [(-2, +1), (-1, +2), (+1, +2), (+2, +1), (+2, -1), (+1, -2), (-1, -2), (-2, -1)]
        moves = []

        for k in range(len(directions)):
            x = self.position[0] + directions[k][0]
            y = self.position[1] + directions[k][1]
            if is_in_table(x, y):
                moves.append((x, y))

        return moves


class King(Piece):
    def __init__(self, piece_c, position):
        super().__init__(position)
        self.name = 'king'
        self.piece_color = piece_c
        self.image = tk.PhotoImage(file=f"pieces/{self.name}{self.piece_color}.png")
        self.initial_position = True

    def get_moves(self):
        directions = [(-1, +1), (+1, +1), (+1, -1), (-1, -1), (-1, 0), (0, +1), (+1, 0), (0, -1)]
        moves = []

        for k in range(len(directions)):
            x = self.position[0] + directions[k][0]
            y = self.position[1] + directions[k][1]
            if is_in_table(x, y):
                moves.append((x, y))

        return moves


# pydoc.writedoc('pieces')
