import tkinter as tk
import table
import random
import pieces as p
import pydoc

from tkinter import messagebox


class ChessBoardUI:
    def __init__(self, frame, mode, game):
        self.dimx = 60
        self.dimy = 60
        self.width = 8 * self.dimx
        self.height = 8 * self.dimy
        self.canvas = tk.Canvas(frame, width=self.width, height=self.height)
        self.cb = table.Table()
        self.chessboard = self.cb.table
        self.selectedPiece = None
        self.selectedMoves = None
        self.mode = mode
        self.winner = None
        self.promv = False
        self.promv_position = None
        self.promv_color = None
        self.root = frame
        self.gameRoot = game

        print(mode)

        for col in range(8):
            self.canvas.grid_columnconfigure(col)
            self.canvas.columnconfigure(col, weight=1)

        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self.on_resize)
        self.canvas.tag_bind("square", "<Button-1>", self.click_event)

    def draw_chess_board(self):
        """function that creates UI for the chess board"""
        # colors = ["#00CED1", "#E6E6FA", "#8A2BE2"]
        # colors = ["#F8DFD4", "#C69774", "#94D1BE"]
        colors = ["#ECECF0", "#9B85AB", "#FFD000", "#F7EFA0"]

        for i in range(8):
            for j in range(8):
                color_index = (i + j) % 2
                color = colors[color_index]
                x1 = j * self.dimx
                y1 = i * self.dimy
                x2 = x1 + self.dimx
                y2 = y1 + self.dimy

                if self.chessboard[i][j].highlighted:
                    color = colors[3]

                if self.chessboard[i][j].name == "empty":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags=((i, j), "square"))
                else:
                    if self.chessboard[i][j].selected:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=colors[2], tags=((i, j), "square"))
                    else:
                        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="square")
                    self.canvas.create_image(x1 + self.dimx / 2, y1 + self.dimy / 2, image=self.chessboard[i][j].image,
                                             tags=((i, j), "piece", self.chessboard[i][j].piece_color, "square"),
                                             anchor="c")

    def set_highlighted(self, value, piece=None):
        """
            function that changes the space color if the selected piece can move there
            or sets the space color to it's initial color if it's not highlighted anymore
        """
        if value:
            self.selectedMoves = self.cb.get_possible_moves_for_piece(piece)

        if self.selectedMoves is not None:
            for move in self.selectedMoves:
                self.chessboard[move[0]][move[1]].highlighted = value

        if not value:
            self.selectedMoves = None

    def on_resize(self, event):
        """
            function that changes the dimensions of the UI chess board depending on the window's sizes
        """
        self.canvas.delete("square")
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.dimx = self.width / 8
        self.dimy = self.height / 8
        self.draw_chess_board()

    def promote_pawn(self):
        """
            function that creates a window for choosing with
            which piece do you want to promote the pawn
        """
        promote_window = tk.Toplevel(self.root)
        promote_window.title("Promote the Pawn")

        def on_promotion_select(piece):
            promote_window.destroy()
            if piece == "Queen":
                self.chessboard[self.promv_position[0]][self.promv_position[1]] = p.Queen(self.promv_color, self.promv_position)
            elif piece == "Knight":
                self.chessboard[self.promv_position[0]][self.promv_position[1]] = p.Knight(self.promv_color, self.promv_position)
            elif piece == "Rock":
                self.chessboard[self.promv_position[0]][self.promv_position[1]] = p.Rock(self.promv_color, self.promv_position)
            elif piece == "Bishop":
                self.chessboard[self.promv_position[0]][self.promv_position[1]] = p.Bishop(self.promv_color, self.promv_position)
            self.promv = False
            self.promv_position = None
            self.promv_color = None
            self.canvas.delete("square")
            self.draw_chess_board()

        queen_button = tk.Button(promote_window, text="Queen", command=lambda: on_promotion_select("Queen"))
        queen_button.pack()

        rook_button = tk.Button(promote_window, text="Rock", command=lambda: on_promotion_select("Rock"))
        rook_button.pack()

        bishop_button = tk.Button(promote_window, text="Bishop", command=lambda: on_promotion_select("Bishop"))
        bishop_button.pack()

        knight_button = tk.Button(promote_window, text="Knight", command=lambda: on_promotion_select("Knight"))
        knight_button.pack()

        promote_window.wait_window()

    def click_event(self, event):
        """
            function that supervises if you clicked on a piece
            or if you clicked on a space where you can move the already selected piece
        """

        i = int(self.canvas.gettags(tk.CURRENT)[0][0])
        j = int(self.canvas.gettags(tk.CURRENT)[0][2])

        if self.promv:
            # do nothing
            print("aici")

        elif self.selectedPiece is None:
            if "piece" in self.canvas.gettags(tk.CURRENT) and self.cb.turn in self.canvas.gettags(tk.CURRENT):
                self.chessboard[i][j].selected = True
                self.selectedPiece = (i, j)
                self.set_highlighted(True, self.chessboard[i][j])
                self.canvas.delete("square")
                self.draw_chess_board()

        elif self.selectedPiece == (i, j):
            self.chessboard[self.selectedPiece[0]][self.selectedPiece[1]].selected = False
            self.selectedPiece = None
            self.set_highlighted(False)
            self.canvas.delete("square")
            self.draw_chess_board()

        elif self.selectedMoves is not None:
            if (i, j) in self.selectedMoves:
                self.chessboard[self.selectedPiece[0]][self.selectedPiece[1]].selected = False
                self.cb.move_the_piece(self.chessboard[self.selectedPiece[0]][self.selectedPiece[1]], (i, j))

                # the pawn at the end
                if self.chessboard[i][j].name == 'pawn':
                    if i == 0 or i == 7:
                        self.promv = True
                        self.promv_position = (i, j)
                        self.promv_color = self.cb.turn
                        self.promote_pawn()

                self.selectedPiece = None
                self.set_highlighted(False)

                adv = self.cb.turn
                if self.cb.turn == "white":
                    self.cb.turn = "black"
                else:
                    self.cb.turn = "white"

                self.canvas.delete("square")
                self.draw_chess_board()

                self.cb.get_all_possible_moves_for(self.cb.turn)
                if not self.cb.list_moves:
                    if self.cb.is_my_king_attacked(self.cb.turn):
                        messagebox.showinfo("Checkmate!", f"The {adv} player has won.")
                        self.root.destroy()
                        self.gameRoot.deiconify()

                    else:
                        messagebox.showinfo("Stalemate!", f"The match has ended.")
                        self.root.destroy()
                        self.gameRoot.deiconify()

                # if it's vs PC
                if self.mode == 2 and self.cb.turn == "black":
                    self.cb.get_all_possible_moves_for(self.cb.turn)
                    mvs = self.cb.list_moves
                    if mvs:
                        ran_pos = random.choice(list(mvs.keys()))
                        ran_move = random.randint(0, len(mvs[ran_pos]) - 1)
                        self.cb.move_the_piece(self.chessboard[ran_pos[0]][ran_pos[1]], mvs[ran_pos][ran_move])

                        # the pawn at the end
                        pawn_pos = mvs[ran_pos][ran_move]
                        if self.chessboard[pawn_pos[0]][pawn_pos[1]].name == 'pawn':
                            if pawn_pos[0] == 0 or pawn_pos[0] == 7:
                                self.promv = True
                                self.promv_position = pawn_pos
                                self.promv_color = self.cb.turn
                                nr = random.randint(1, 4)

                                if nr == 1:
                                    self.chessboard[self.promv_position[0]][self.promv_position[1]] = p.Queen(
                                        self.promv_color, self.promv_position)
                                elif nr == 2:
                                    self.chessboard[self.promv_position[0]][self.promv_position[1]] = p.Knight(
                                        self.promv_color, self.promv_position)
                                elif nr == 3:
                                    self.chessboard[self.promv_position[0]][self.promv_position[1]] = p.Rock(
                                        self.promv_color, self.promv_position)
                                elif nr == 4:
                                    self.chessboard[self.promv_position[0]][self.promv_position[1]] = p.Bishop(
                                        self.promv_color, self.promv_position)

                                self.promv = False
                                self.promv_position = None
                                self.promv_color = None

                        self.canvas.delete("square")
                        self.draw_chess_board()
                    else:
                        if self.cb.is_my_king_attacked(self.cb.turn):
                            messagebox.showinfo("Checkmate!", f"The {adv} player has won.")
                            self.root.destroy()
                            self.gameRoot.deiconify()

                        else:
                            messagebox.showinfo("Stalemate!", f"The match has ended.")
                            self.root.destroy()
                            self.gameRoot.deiconify()
                    self.cb.turn = "white"


def start_game(ui):
    ui.draw_chess_board()


def play():
    def on_start_button_click():
        selected_mode = var.get()
        if selected_mode == 0:
            messagebox.showwarning("Warning!", "Select a game mode!")
        else:
            gameRoot.withdraw()
            ui = ChessBoardUI(tk.Toplevel(gameRoot), selected_mode, gameRoot)
            start_game(ui)

    gameRoot = tk.Tk()
    gameRoot.title("Menu - Chess")

    var = tk.IntVar()

    pvp_button = tk.Radiobutton(gameRoot, text="Player vs Player", variable=var, value=1, font=("Helvetica", 40),
                                indicatoron=False, activebackground="#9B85AB", selectcolor="#9B85AB")
    pvp_button.pack()

    pvc_button = tk.Radiobutton(gameRoot, text="  Player vs PC   ", variable=var, value=2, font=("Helvetica", 40),
                                indicatoron=False, activebackground="#9B85AB", selectcolor="#9B85AB")
    pvc_button.pack()

    start_button = tk.Button(gameRoot, text=" > Start game ", command=on_start_button_click, font=("Helvetica", 40))
    start_button.pack()

    gameRoot.mainloop()


# pydoc.writedoc('ChessBoardUI')


