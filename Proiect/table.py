import pieces as p
import pydoc


class Table:
    def __init__(self):
        self.table = [
            [p.Rock("black", (0, 0)), p.Knight("black", (0, 1)), p.Bishop("black", (0, 2)), p.Queen("black", (0, 3)),
             p.King("black", (0, 4)), p.Bishop("black", (0, 5)), p.Knight("black", (0, 6)), p.Rock("black", (0, 7))],
            [p.Pawn("black", (1, i)) for i in range(8)],
            [p.Piece((2, i)) for i in range(8)],
            [p.Piece((3, i)) for i in range(8)],
            [p.Piece((4, i)) for i in range(8)],
            [p.Piece((5, i)) for i in range(8)],
            [p.Pawn("white", (6, i)) for i in range(8)],
            [p.Rock("white", (7, 0)), p.Knight("white", (7, 1)), p.Bishop("white", (7, 2)), p.Queen("white", (7, 3)),
             p.King("white", (7, 4)), p.Bishop("white", (7, 5)), p.Knight("white", (7, 6)), p.Rock("white", (7, 7))],
        ]
        self.wKingPos = (7, 4)
        self.bKingPos = (0, 4)
        self.colors = ["white", "black"]
        self.turn = "white"
        self.last_move = None
        self.list_moves = {}

    def is_my_king_attacked(self, color):
        """function to see if the king of the given color is attacked"""
        # get the position of the king of the given color
        kingPos = self.wKingPos
        if color == "black":
            kingPos = self.bKingPos

        # is my king attacked by a Knight?
        attacks = [(-2, +1), (-1, +2), (+1, +2), (+2, +1), (+2, -1), (+1, -2), (-1, -2), (-2, -1)]
        for i in range(len(attacks)):
            x = kingPos[0] + attacks[i][0]
            y = kingPos[1] + attacks[i][1]
            if p.is_in_table(x, y):
                if self.table[x][y].name == "knight":
                    if self.table[x][y].piece_color != color:
                        return True

        # is my king attacked by a bishop or the Queen?
        attacks = [(-1, +1), (+1, +1), (+1, -1), (-1, -1)]
        for i in range(len(attacks)):
            x = kingPos[0] + attacks[i][0]
            y = kingPos[1] + attacks[i][1]

            while p.is_in_table(x, y):
                if self.table[x][y].name == "empty":
                    x += attacks[i][0]
                    y += attacks[i][1]
                elif self.table[x][y].piece_color != color and (
                        self.table[x][y].name == "bishop" or self.table[x][y].name == "queen"):
                    return True
                else:
                    x = 8
                    y = 8

        # is my king attacked by a rock or the Queen?
        attacks = [(-1, 0), (0, +1), (+1, 0), (0, -1)]
        for i in range(len(attacks)):
            x = kingPos[0] + attacks[i][0]
            y = kingPos[1] + attacks[i][1]

            while p.is_in_table(x, y):
                if self.table[x][y].name == "empty":
                    x += attacks[i][0]
                    y += attacks[i][1]
                elif self.table[x][y].piece_color != color and (
                        self.table[x][y].name == "rock" or self.table[x][y].name == "queen"):
                    return True
                else:
                    x = 8
                    y = 8

        # is my king attacked by a pawn?
        if color == "white":
            attacks = [(-1, -1), (-1, +1)]
        else:
            attacks = [(+1, -1), (+1, +1)]

        for i in range(len(attacks)):
            x = kingPos[0] + attacks[i][0]
            y = kingPos[1] + attacks[i][1]

            if p.is_in_table(x, y):
                if self.table[x][y].name == "pawn":
                    if self.table[x][y].piece_color != color:
                        return True
        return False

    def are_kings_too_close(self):
        """function to see if the kings are too close to each other"""
        i = self.bKingPos[0]
        j = self.bKingPos[1]
        if self.wKingPos[0] in (i - 1, i, i + 1) and self.wKingPos[1] in (j - 1, j, j + 1):
            return True
        return False

    def move_the_piece(self, piece, where_to, test=False):
        """
            function to move the piece on the table
            if it's only a test to see if the move is possible then we undo it and give feedback
        """
        remember_pawn = None
        if piece.name == 'pawn':
            # if en_passant took place, then we need to remove the eaten pawn
            if where_to[1] != piece.position[1] and self.table[where_to[0]][where_to[1]].name == 'empty':
                remember_pawn = self.table[self.last_move[2][0]][self.last_move[2][1]]
                self.table[self.last_move[2][0]][self.last_move[2][1]] = p.Piece(self.last_move[2])

        backup_lost_piece = self.table[where_to[0]][where_to[1]]
        from_where = piece.position
        kings_ip = False

        piece.position = (where_to[0], where_to[1])
        self.table[where_to[0]][where_to[1]] = piece
        self.table[from_where[0]][from_where[1]] = p.Piece(from_where)

        if piece.name == "king":
            # if left-castling takes place
            if from_where[1] - where_to[1] == 2:
                self.move_the_piece(self.table[from_where[0]][0], (where_to[0], where_to[1] + 1))
            # if right-castling takes place
            elif from_where[1] - where_to[1] == -2:
                self.move_the_piece(self.table[from_where[0]][7], (where_to[0], where_to[1] - 1))

            kings_ip = piece.initial_position
            piece.initial_position = False

            if piece.piece_color == "white":
                self.wKingPos = where_to
            else:
                self.bKingPos = where_to

        if not test:
            self.last_move = (piece, from_where, where_to)

            if piece.name == "king" or piece.name == "rock":
                piece.initial_position = False
            return True
        else:
            kings_sbs = False
            if self.are_kings_too_close():
                kings_sbs = True
            attacked = self.is_my_king_attacked(self.turn)
            piece.position = from_where
            self.table[from_where[0]][from_where[1]] = piece
            self.table[where_to[0]][where_to[1]] = backup_lost_piece

            # undo en passant eaten piece
            if remember_pawn is not None:
                self.table[self.last_move[2][0]][self.last_move[2][1]] = remember_pawn

            if piece.name == "king":
                # if left-castling took place
                if from_where[1] - where_to[1] == 2:
                    # for the king
                    self.table[from_where[0]][from_where[1]].initial_position = True
                    # for the rock
                    self.table[where_to[0]][where_to[1] + 1].initial_position = True
                    self.table[where_to[0]][where_to[1] + 1].position = (from_where[0], 0)
                    self.table[from_where[0]][0] = self.table[where_to[0]][where_to[1] + 1]
                    self.table[where_to[0]][where_to[1] + 1] = p.Piece((where_to[0], where_to[1] + 1))

                # if right-castling took place
                elif from_where[1] - where_to[1] == -2:
                    # for the king
                    self.table[from_where[0]][from_where[1]].initial_position = True
                    # for the rock
                    self.table[where_to[0]][where_to[1] - 1].initial_position = True
                    self.table[where_to[0]][where_to[1] - 1].position = (from_where[0], 7)
                    self.table[from_where[0]][7] = self.table[where_to[0]][where_to[1] - 1]
                    self.table[where_to[0]][where_to[1] - 1] = p.Piece((where_to[0], where_to[1] - 1))

                piece.initial_position = kings_ip
                if piece.piece_color == "white":
                    self.wKingPos = from_where
                else:
                    self.bKingPos = from_where

            if attacked or kings_sbs:
                return False
        return True

    def get_possible_moves_for_piece(self, piece):
        """function to get what moves can the given piece make in that current situation"""
        possible_moves = piece.get_moves()
        filtred_moves = []

        if piece.name in ("rock", "bishop", "queen", "pawn"):
            for i in range(len(possible_moves)):
                liniar_moves = possible_moves[i]
                j = 0
                while j < len(liniar_moves):
                    x = liniar_moves[j][0]
                    y = liniar_moves[j][1]
                    if self.table[x][y].name == "empty":
                        filtred_moves.append(self.table[x][y].position)
                        j += 1
                    else:
                        if piece.name != "pawn":
                            # I can eat the piece if it's not mine and if it's not a king (for all but not the pawn)
                            if self.table[x][y].piece_color != self.turn and self.table[x][y].name != "king":
                                filtred_moves.append(self.table[x][y].position)
                        j = len(liniar_moves)
        # for knight and king
        else:
            for i in range(len(possible_moves)):
                x = possible_moves[i][0]
                y = possible_moves[i][1]

                if self.table[x][y].name == "empty":
                    filtred_moves.append(self.table[x][y].position)
                elif self.table[x][y].piece_color != self.turn and self.table[x][y].name != "king":
                    filtred_moves.append(self.table[x][y].position)

        # more moves for pawn if conditions are fulfilled
        if piece.name == 'pawn':
            if piece.piece_color == self.turn:
                i = piece.position[0]
                j = piece.position[1]

                # verify if conditions are fulfilled for the move where the pawn can eat a piece
                if piece.piece_color == "white":
                    if p.is_in_table(i - 1, j - 1):
                        if self.table[i - 1][j - 1].name != 'empty':
                            if self.table[i - 1][j - 1].piece_color != piece.piece_color:
                                filtred_moves.append(self.table[i - 1][j - 1].position)
                    if p.is_in_table(i - 1, j + 1):
                        if self.table[i - 1][j + 1].name != 'empty':
                            if self.table[i - 1][j + 1].piece_color != piece.piece_color:
                                filtred_moves.append(self.table[i - 1][j + 1].position)

                if piece.piece_color == "black":
                    if p.is_in_table(i + 1, j - 1):
                        if self.table[i + 1][j - 1].name != 'empty':
                            if self.table[i + 1][j - 1].piece_color != piece.piece_color:
                                filtred_moves.append(self.table[i + 1][j - 1].position)
                    if p.is_in_table(i + 1, j + 1):
                        if self.table[i + 1][j + 1].name != 'empty':
                            if self.table[i + 1][j + 1].piece_color != piece.piece_color:
                                filtred_moves.append(self.table[i + 1][j + 1].position)

                # en passant
                if self.last_move is not None:
                    if self.last_move[0].name == 'pawn':
                        from_here = self.last_move[1]
                        to_here = self.last_move[2]
                        if from_here[0] - to_here[0] == 2 or from_here[0] - to_here[0] == -2:
                            if to_here[0] == piece.position[0]:
                                if piece.position[1] == to_here[1] + 1 or piece.position[1] == to_here[1] - 1:
                                    filtred_moves.append((int((from_here[0] + to_here[0]) / 2), from_here[1]))

        if piece.name == 'king':
            castling = self.can_king_make_castling(piece.piece_color)
            if castling[0] == 1:
                filtred_moves.append((piece.position[0], piece.position[1] - 2))
            if castling[1] == 1:
                filtred_moves.append((piece.position[0], piece.position[1] + 2))

        final_moves = []
        for i in range(len(filtred_moves)):
            ok_to_move = self.move_the_piece(piece, filtred_moves[i], test=True)
            if ok_to_move:
                final_moves.append(filtred_moves[i])

        if len(final_moves) == 0:
            return None
        return final_moves

    def can_king_make_castling(self, color):
        # get the position of the king of the given color
        king = self.table[self.wKingPos[0]][self.wKingPos[1]]
        rockL = self.table[7][0]
        rockR = self.table[7][7]
        if color == "black":
            king = self.table[self.bKingPos[0]][self.bKingPos[1]]
            rockL = self.table[0][0]
            rockR = self.table[0][7]

        if not king.initial_position:
            return (0, 0)

        if rockL.name != 'rock' or not rockL.initial_position:
            if rockR.name != 'rock' or not rockR.initial_position:
                return (0, 0)

        okR = 0
        # try right castling
        if rockR.name == 'rock' and rockR.initial_position:
            okR = 1
            if self.table[king.position[0]][king.position[1] + 1].name != 'empty':
                okR = 0
            elif self.table[king.position[0]][king.position[1] + 2].name != 'empty':
                okR = 0
            elif self.is_my_king_attacked(color):
                okR = 0
            elif not self.move_the_piece(king, (king.position[0], king.position[1] + 1), test=True):
                okR = 0
            elif not self.move_the_piece(king, (king.position[0], king.position[1] + 2), test=True):
                okR = 0

        okL = 0
        # try left castling
        if rockL.name == 'rock' and rockL.initial_position:
            okL = 1
            if self.table[king.position[0]][king.position[1] - 1].name != 'empty':
                okL = 0
            elif self.table[king.position[0]][king.position[1] - 2].name != 'empty':
                okL = 0
            elif self.table[king.position[0]][king.position[1] - 3].name != 'empty':
                okL = 0
            elif self.is_my_king_attacked(color):
                okL = 0
            elif not self.move_the_piece(king, (king.position[0], king.position[1] - 1), test=True):
                okL = 0
            elif not self.move_the_piece(king, (king.position[0], king.position[1] - 2), test=True):
                okL = 0

        return (okL, okR)

    def get_all_possible_moves_for(self, color):
        self.list_moves = {}
        for i in range(8):
            for j in range(8):
                if self.table[i][j].name != 'empty':
                    if self.table[i][j].piece_color == color:
                        moves = self.get_possible_moves_for_piece(self.table[i][j])
                        if moves:
                            self.list_moves[self.table[i][j].position] = moves


# pydoc.writedoc('table')
