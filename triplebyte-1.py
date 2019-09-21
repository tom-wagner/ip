ai_token = '0'
player_token = 'X'


class Board:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]

    # def __repr__(self):
    #     return '\n'.join(['|'.join(row) for row in self.board])

    def print_board(self):
        print('\n'.join(['|'.join(row) for row in self.board]))

    def add_token(self, token: str, r: int, c: int):
        self.board[r][c] = token

    def get_all_pieces(self):
        return [p for row in self.board for p in row]

    def is_board_full(self):
        pieces = self.get_all_pieces()
        for char in pieces:
            if char != 'X' and char != '0':
                return False
        return True

    def ai_move(self):
        for r, row in enumerate(self.board):
            for c, square in enumerate(row):
                if square == '-':
                    self.add_token(ai_token, r, c)
                    return
        # raise Exception('No valid moves')


class Game:
    def __init__(self):
        self.board = Board()
        self.player_up = 'HUMAN'

    def play_game(self):
        while True:
            if self.board.is_board_full():
                print('exiting, board full')
                break
            if self.player_up == 'HUMAN':
                row = int(input('what row do you want to play in?'))
                col = int(input('what column do you want to play in?'))
                self.board.add_token('X', row, col)
            if self.player_up == 'AI':
                self.board.ai_move()
            self.board.print_board()
            self.toggle_turn()

    def toggle_turn(self):
        self.player_up = 'HUMAN' if self.player_up == 'AI' else 'AI'


g = Game()

g.play_game()

# b = Board()
#
# for num in range(9):
#     print(num)
#     b.is_board_full()
#     b.ai_move()
#     b.print_board()

# b = Board()
#
# b.print_board()
#
# b.add_token('X', 0, 1)
#
# b.print_board()
#
# b.print_board()




