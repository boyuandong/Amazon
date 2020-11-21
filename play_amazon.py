"""This is a player for Game of Amazons"""

WHITE = 0
BLACK = 1
EMPTY = 2
ARROW = 3
N =10   #This is the size of the board, must be even numbers, here we use 10
    
class Amazon:

    
    def __init__(self):
        self.BLACK_STONES = [] #Store all positions of 4 black stones
        self.WHITE_STONES = [] #Store all positions of 4 white stones
        self.a = [] #Store the board
        self.game_end = False
        self.winner = None
        
    def coord_to_move(self, coord):
        '''convert alpha coord to move'''
        alpha = coord[0].lower()
        row = int(coord[1])
        col = ord(alpha) - 97
        return row * N + col
        
    def move_to_coord(self, move):
        '''convert move to alpha coord'''
        col = move % N
        row = move // N
        alpha = 'abcdefghij'[col]
        return alpha + str(row)
        
    def get_color(self, color_str):
        '''get the color of the player'''
        if color_str == 'o':
            return WHITE
        elif color_str == 'x':
            return BLACK
        
        
    def show(self):
        '''show the board a'''
        print('   a b c d e f g h i j')
        for i in range(N):
            print(str(i)+' '+''.join(self.a[i*N:N*(i+1)]))

        
    def set_board(self):
        '''set the board at the begining'''
        for i in range(N*N):
            self.a.append(' .')
        self.a[(N//2 - 2)] = ' x'
        self.a[(N//2+1)] = ' x'
        self.a[(N//2 - 2) * N] = ' x'
        self.a[(N//2 - 2) * N + (N - 1)] = ' x'
        self.a[(N//2+1) * N] = ' o'
        self.a[(N//2+1) * N + (N - 1)] = ' o'
        self.a[(N-1)*N + (N//2 - 2)] = ' o'
        self.a[(N-1)*N + (N//2+1)] = ' o'
#        self.BLACK_STONES = [3, 6, 30, 39]
#        self.WHITE_STONES = [60, 69, 93, 96]
        self.BLACK_STONES = [(N//2 - 2), (N//2+1), (N//2 - 2) * N, (N//2 - 2) * N + (N - 1)]
        self.WHITE_STONES = [((N//2+1) * N), (N//2+1) * N + (N - 1), (N-1)*N + (N//2 - 2), (N-1)*N + (N//2+1)]

    def menu(self):
        print('exit/q/quit        stop the game')
        print(' o d9 to e8        move o (white) d9 to e8')
        print(' x d0 to d1        move x (black) d0 to d1')
       
        
    def legal_moves(self, move):
        '''get all legal queenlike moves for a stone at move position'''
        legal_moves = set()
        now = move
    #   right move while not at the right col
        while (move + 1)% N != 0:
            if self.a[move + 1] == ' .':
                legal_moves.add(move + 1)
            else:
                break
            move = move + 1
            
    #   left move while not at the left col
        move = now
        while (move % N != 0):
            if self.a[move - 1] == ' .':
                legal_moves.add(move - 1)
            else:
                break
            move = move - 1
            
    #   down move while not at the bottom row
        move = now
        while move < (N-1)*N:
            if self.a[move + N] == ' .':
                legal_moves.add(move + N)
            else:
                break
            move = move + N
            
    #   up move while not at the top row
        move = now
        while move >= N:
            if self.a[move - N] == ' .':
                legal_moves.add(move - N)
            else:
                break
            move = move - N
            
    #   left up move while not at left/top col/row
        move = now
        while (move%N != 0) and (move >= N):
            if self.a[move - (N+1)] == ' .':
                legal_moves.add(move - (N+1))
            else:
                break
            move = move - (N+1)
            
    #   right up move while not at right/top col/row
        move = now
        while ((move+1)%N != 0) and (move >= N):
            if self.a[move - (N-1)] == ' .':
                legal_moves.add(move - (N-1))
            else:
                break
            move = move - (N-1)
            
    #   left down move while not at left/bottom col/row
        move = now
        while (move%N != 0) and (move < (N-1)*N):
            if self.a[move + (N-1)] == ' .':
                legal_moves.add(move + (N-1))
            else:
                break
            move = move + (N-1)
            
    #   right down move while not at right/bottom col/row
        move = now
        while ((move+1)%N != 0) and (move < (N-1)*N):
            if self.a[move + (N+1)] == ' .':
                legal_moves.add(move + (N+1))
            else:
                break
            move = move + (N+1)
            
        queen_moves = list(legal_moves)
        queen_moves.sort()
        
        return queen_moves
    
    def check_coord(self, str):
        '''check if the string is a valid coord'''
        return str[0].isalpha() and ord(str[0]) >=97 and ord(str[0]) <= 106 and str[1].isdigit() and int(str[1]) >=0 and int(str[1]) <= (N-1)


    def make_arrow(self, now):
        '''place an arrow'''
        place_arrow = False
        while (not place_arrow):
            arrow_coord = input("please enter your arrow move (d1):").split()
            if not self.check_coord(arrow_coord[0]):
                print("please enter a legal move for arrow like d1")
                continue
            arrow_move= self.coord_to_move(arrow_coord[0])
            if not self.check_move_to(now, arrow_move):
                print("please enter a correct destination position")
                self.print_legal_moves(now)
                continue
            legal_arrow_moves = self.legal_moves(now)
            if arrow_move in legal_arrow_moves:
                self.a[arrow_move] = ' a'
                place_arrow = True
            else:
                print("Please choose the correct arrow move")
        

    def make_move(self, now, to, color_str):
        '''make a move'''
        self.a[now] = ' .'
        self.a[to] = ' '+ color_str
        if self.get_color(color_str) == BLACK:
            self.BLACK_STONES.remove(now)
            self.BLACK_STONES.append(to)
        elif self.get_color(color_str) == WHITE:
            self.WHITE_STONES.remove(now)
            self.WHITE_STONES.append(to)
        self.show()
        self.make_arrow(to)
        
    def check_game_over(self):
        '''check if the game is over'''
        '''if either player has 0 left moves then game over, can't be a draw game'''
        black_left_moves = 0
        white_left_moves = 0
        for move in self.BLACK_STONES:
            black_left_moves += len(self.legal_moves(move))
        for move in self.WHITE_STONES:
            white_left_moves += len(self.legal_moves(move))
        if black_left_moves == 0 and white_left_moves != 0:
            self.winner = "o (white)"
            self.game_end = True
        elif black_left_moves != 0 and white_left_moves == 0:
            self.winner = "x (black)"
            self.game_end = True
    
    def check_move_now(self, color, now):
        '''check if the move now position is legall'''
        if color == BLACK:
            return now in self.BLACK_STONES
        elif color == WHITE:
            return now in self.WHITE_STONES
            
    def check_move_to(self,now, to):
        '''check if the move to positon is legall'''
        queen_moves = self.legal_moves(now)
        return self.a[to] == ' .' and (to in queen_moves)
            
    def check_color(self, color_str):
        '''check if the color entered is valid'''
        if color_str == 'x':
            return True
        elif color_str == 'o':
            return True
        else:
            return False

            
    def print_legal_moves(self, now):
        '''print all legal moves'''
        queen_moves = self.legal_moves(now)
        print_moves = []
        for move in queen_moves:
            print_moves.append(self.move_to_coord(move))
        coord_now = self.move_to_coord(now)
        queen_moves_str = ','.join(print_moves)
        print("for",str(self.move_to_coord(now)), "it is able to move to ", queen_moves_str)
    
    def print_stones(self, color):
        '''print 8 stones, 4 for white stones, 4 for black stones'''
        print_moves = []
        color_str = None
        if color == BLACK:
            color_str = "black (x)"
            for move in self.BLACK_STONES:
                print_moves.append(self.move_to_coord(move))
        elif color == WHITE:
            color_str = "white (o)"
            for move in self.WHITE_STONES:
                print_moves.append(self.move_to_coord(move))
        print("As", color_str,"you are able to play", ','.join(print_moves), "stones")

    def play(self):
        '''play the game'''
        self.set_board()
        self.show()
        self.menu()
        while not self.game_end:
            coord_str = input("please enter your move (x d1 to d3 ):")
            if coord_str == 'q' or coord_str == 'quit' or coord_str == 'exit':
                break
            if len(coord_str.split()) != 4 or not self.check_coord(coord_str.split()[1]) or not self.check_coord(coord_str.split()[3]):
                self.show()
                print("please enter a correct input (o d9 to e8)")
                self.menu()
                continue
            color_str, coord_now,_, coord_to = coord_str.split()
            if not self.check_color(color_str):
                self.show()
                print("please enter a correct color x or o")
                continue
            color = self.get_color(color_str)
            move_now = self.coord_to_move(coord_now)
            if not self.check_move_now(color, move_now):
                self.show()
                print("please enter a correct stone you want to move")
                self.print_stones(color)
                continue
            move_to = self.coord_to_move(coord_to)
            if not self.check_move_to(move_now, move_to):
                self.show()
                print("please enter a correct destination position")
                self.print_legal_moves(move_now)
                continue
            queen_moves = self.legal_moves(move_now)
#           make moves
            self.make_move(move_now, move_to, color_str)
#           show the board
            self.show()
            self.check_game_over()
        print(self.winner, "is the winner")
    
    

a = Amazon()
a.play()

