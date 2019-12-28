# https://www.codewars.com/kata/52fcc820f7214727bc0004b7

from itertools import product
from copy import deepcopy


class Piece:
    def __init__(self, piece):
        self.piece = piece["piece"]
        self.x = piece["x"]
        self.y = piece["y"]
        self.owner = piece["owner"]
        self.is_last = "prevX" in piece
        if self.is_last:
            self.prevX = piece["prevX"]
            self.prevY = piece["prevY"]

    @property
    def dictionary(self):
        dictionary = {
            "piece": self.piece,
            "x": self.x,
            "y": self.y,
            "owner": self.owner,
        }
        if self.is_last:
            dictionary["prevX"] = self.prevX
            dictionary["prevY"] = self.prevY
        return dictionary

    def _get_next_boards_from_directions(self, board, directions, multiple=True, capture_only=False):
        next_boards = []
        for x_direction, y_direction in directions:
            move_range = range(1, 8) if multiple else [1]
            for i in move_range:
                next_x, next_y = self.x+i*x_direction, self.y+i*y_direction
                if not Board.is_in_board(next_x, next_y): break
                piece = board[next_x][next_y]
                next_board = board.copy()
                if piece:
                    if piece.owner != self.owner:
                        next_board.remove(piece)
                        if next_board.move(self, next_x, next_y):
                            next_boards.append(next_board)
                    break
                if next_board.move(self, next_x, next_y) and not capture_only:
                    next_boards.append(next_board)
        return next_boards

    def __eq__(self, other):
        if type(self) == type(other):
            if self.is_last != other.is_last: return False
            if self.is_last:
                return self.x == other.x and self.y == other.y and self.owner == other.owner and self.prevX == other.prevX and self.prevY == other.prevY
            else:
                return self.x == other.x and self.y == other.y and self.owner == other.owner

    def __hash__(self):
        if self.is_last:
            return hash(self.x) + hash(self.y) + hash(self.prevX) + hash(self.prevY) + hash(self.owner) + hash(self.piece)
        else:
            return hash(self.x) + hash(self.y) + hash(self.owner) + hash(self.piece)

    def __str__(self):
        last = "*" if self.is_last else ""
        owner = "B" if self.owner else "W"
        return "%s%s %s(%s, %s)" % (last, owner, self.piece, self.x, self.y)

    def __repr__(self):
        return self.__str__()

class Knight(Piece):
    def get_next_boards(self, board):
        directions = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]
        return self._get_next_boards_from_directions(board, directions, False)

class Rook(Piece):
    def get_next_boards(self, board):
        return self._get_next_boards_from_directions(board, [(-1, 0), (1, 0), (0, -1), (0, 1)])

class Bishop(Piece):
    def get_next_boards(self, board):
        return self._get_next_boards_from_directions(board, product([-1, 1], [-1, 1]))

class Queen(Piece):
    def get_next_boards(self, board):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] + list(product([-1, 1], [-1, 1]))
        return self._get_next_boards_from_directions(board, directions)

class King(Piece):
    def get_next_boards(self, board):
        directions = list(product([-1, 0, 1], [-1, 0, 1]))
        directions.remove((0, 0))
        return self._get_next_boards_from_directions(board, directions, False)

class Pawn(Piece):
    @property
    def front_direction(self):
        return 1 if self.owner else -1

    @property
    def first_rank(self):
        return 1 if self.owner else 6

    @property
    def is_first(self):
        return self.y == self.first_rank

    @property
    def is_at_en_passant_rank(self):
        return self.y == 4 if self.owner else self.y == 3

    @property
    def did_move_two_forward(self):
        return self.is_last and abs(self.y - self.first_rank) == 2

    def get_next_boards(self, board):
        next_boards = []
        # can move forward if the front square is empty
        if Board.is_in_board(self.x, self.y+self.front_direction) and not board[self.x][self.y+self.front_direction]:
            next_boards += self._get_next_boards_from_directions(board, [(0, self.front_direction)], False)
        # can move forward two squares if it is the first move and the two front squares are empty
        if Board.is_in_board(self.x, self.y+2*self.front_direction) and not board[self.x][self.y+self.front_direction] and not board[self.x][self.y+2*self.front_direction] and self.is_first:
            next_boards += self._get_next_boards_from_directions(board, [(0, 2*self.front_direction)], False)
        # can move diagonally front square if there is an opponent's piece
        next_boards += self._get_next_boards_from_directions(board, [(-1, self.front_direction), (1, self.front_direction)], False, True)
        # en passant
        if self.is_at_en_passant_rank:
            x_neighbors = filter(lambda p: Board.is_in_board(*p), [(self.x-1, self.y), (self.x+1, self.y)])
            for x, y in x_neighbors:
                piece = board[x][y]
                if not piece: continue
                if type(piece) == self.__class__ and piece.owner != self.owner and piece.did_move_two_forward:
                    next_board = board.copy()
                    next_board.move(self, piece.x, self.y+self.front_direction)
                    next_board.remove(piece)
                    next_boards.append(next_board)
        return next_boards

piece_classes = {
    "pawn": Pawn,
    "knight": Knight,
    "rook": Rook,
    "bishop": Bishop,
    "queen": Queen,
    "king": King
}

class Board:
    @classmethod
    def is_in_board(cls, x, y):
        return x in range(0, 8) and y in range(0, 8)

    def __init__(self, pieces):
        self._board = [[None for _ in range(0, 8)] for _ in range(0, 8)]
        for piece in pieces:
            piece_object = piece_classes[piece["piece"]](piece)
            self[piece["x"]][piece["y"]] = piece_object

    @property
    def pieces(self):
        return [piece for column in self for piece in column if piece]

    def move(self, piece, next_x, next_y):
        if not (next_x in range(0, 8) and next_y in range(0, 8)):
            return False
        piece_in_board = self[piece.x][piece.y]
        self.remove(piece)
        piece_in_board.is_last, piece_in_board.prevX, piece_in_board.prevY = True, piece.x, piece.y
        piece_in_board.x, piece_in_board.y = next_x, next_y
        self[next_x][next_y] = piece_in_board
        return True

    def remove(self, piece):
        self[piece.x][piece.y] = None

    def copy(self):
        return deepcopy(self)

    def get_king(self, player):
        king = list(filter(lambda piece: type(piece) == King and piece.owner == player, self.pieces))
        return king[0] if king else None

    def get_next_boards(self, player):
        players_pieces = list(filter(lambda piece: piece.owner == player, self.pieces))
        return {piece: piece.get_next_boards(self) for piece in players_pieces}

    def is_check(self, player):
        opponent = 0 if player else 1
        all_next_boards = self.get_next_boards(opponent)
        pieces = []
        for piece, next_boards in all_next_boards.items():
            if list(filter(lambda board: board.get_king(player) is None, next_boards)):
                pieces.append(piece.dictionary)
        return pieces

    def is_mate(self, player):
        next_boards = sum([boards for _, boards in self.get_next_boards(player).items()], [])
        return not list(filter(lambda board: not board.is_check(player), next_boards))

    def __getitem__(self, x):
        return self._board[x]

def isCheck(pieces, player):
    board = Board(pieces)
    return board.is_check(player)

def isMate(pieces, player):
    board = Board(pieces)
    return board.is_mate(player)
