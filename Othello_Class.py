#This module implements the Classes for the Game Logic

NONE=' '
WHITE='W'
BLACK='B'

class InvalidOthelloMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass

class OthelloGameOverError(Exception):
    '''
    Raised whenever an attempt is made to make a move after the game is
    already over
    '''
    pass

class GameState:
    def __init__(self,BOARD_COLUMNS,BOARD_ROWS,first_player,top_left,winning_option):
        if first_player=='w':
            self._turn=WHITE
        else:
            self._turn=BLACK
        self._columns=BOARD_COLUMNS
        self._rows=BOARD_ROWS
        self._board=_new_game_board(BOARD_COLUMNS,BOARD_ROWS,top_left)
        self._winning_option=winning_option

    def board(self)->list:
        return self._board
    
    def turn(self)->str:
        return self._turn

    def columns(self)->int:
        return self._columns

    def rows(self)->int:
        return self._rows
    
    def drop_piece(self,row_number,column_number):
        self._board[column_number-1][row_number-1]=self.turn()
        self._turn=self.opposite_turn()

    def check_valid_moves(self)->list:
        valid_moves=[]
        for col in range(1,self.columns()+1):
            for row in range(1,self.rows()+1):
                if self.board()[col-1][row-1]==NONE:
                    valid_moves.append(self.board_check(row,col,'check'))
        return valid_moves

    def winning_player(self)->str:
        valid_moves=[]
        white_count=self.white_count()
        black_count=self.black_count()
        valid_moves=self.check_valid_moves()
        if True in valid_moves:
            return NONE
        else:
            print('Player ', self._turn ,'has no valid moves')
            self._turn=self.opposite_turn()
            valid_moves=self.check_valid_moves()
            if True in valid_moves:
                return NONE
            elif self._winning_option=='m':
                print('Player ', self._turn ,'has no valid moves')
                if black_count>white_count:
                    return BLACK
                elif white_count>black_count:
                    return WHITE
                else:
                    return 'No Winner'
            else:
                print('Player ', self._turn ,'has no valid moves')
                if black_count<white_count:
                    return BLACK
                elif white_count<black_count:
                    return WHITE
                else:
                    return 'No Winner'
                
            

    def black_count(self)->int:
        count=0
        for row in range(self.rows()):
            for col in range(self.columns()):
                if self.board()[col][row]=='B':
                    count+=1
        return count
                    
    def white_count(self)->int:
        count=0
        for row in range(self.rows()):
            for col in range(self.columns()):
                if self.board()[col][row]=='W':
                    count+=1
        return count
   
    def opposite_turn(self) -> str:
        '''Given the player whose turn it is now, returns the opposite player'''
        if self.turn() == WHITE:
            return BLACK
        else:
            return WHITE

# METHODS  FOR  FLIPPING THE BOARD

    def board_check(self,row_number,column_number,intention):
        Valid_moves=[]
        Valid_moves.append(self.lower_column_check(row_number,column_number,intention))
        Valid_moves.append(self.upper_column_check(row_number,column_number,intention))
        Valid_moves.append(self.right_row_check(row_number,column_number,intention))
        Valid_moves.append(self.left_row_check(row_number,column_number,intention))
        Valid_moves.append(self.upper_right_diagnol_check(row_number,column_number,intention))
        Valid_moves.append(self.lower_left_diagnol_check(row_number,column_number,intention))
        Valid_moves.append(self.upper_left_diagnol_check(row_number,column_number,intention))
        Valid_moves.append(self.lower_right_diagnol_check(row_number,column_number,intention))

        if True in Valid_moves:
            return True
        else:
            return False
            
    def lower_column_check(self,row_number,column_number,intention):
        p=column_number-1
        q=row_number
        flip_indices=[]
        while True:
            try:
                if p<0 or q<0:
                    return False
                if self.board()[p][q]==self.opposite_turn():
                    flip_indices.append(q)
                    q+=1
                elif self.board()[p][q]==self.turn():
                    if intention=='flip':
                        for index in flip_indices:
                            self._board[p][index]=self.turn()
                    return len(flip_indices)>0
                else:
                    return  False
            except IndexError:
                return False
              
    def upper_column_check(self,row_number,column_number,intention):
        p=column_number-1
        q=row_number-2
        flip_indices=[]
        while True:
            try:
                if p<0 or q<0:
                    return False
                if self.board()[p][q]==self.opposite_turn():
                    flip_indices.append(q)
                    q+=-1
                elif self.board()[p][q]==self.turn():
                    if intention=='flip':
                        for index in flip_indices:
                            self._board[p][index]=self.turn()
                    return len(flip_indices)>0
                else:
                    return False
            except IndexError:
                return False
            
    def right_row_check(self,row_number,column_number,intention):
        p=column_number
        q=row_number-1
        flip_indices=[]
        while True:
            try:
                if p<0 or q<0:
                    return False
                if self.board()[p][q]==self.opposite_turn():
                    flip_indices.append(p)
                    p+=1
                elif self.board()[p][q]==self.turn():
                    if intention=='flip':
                        for index in flip_indices:
                            self._board[index][q]=self.turn()
                    return len(flip_indices)>0
                else:
                        return False
            except IndexError:
                return False
                
    def left_row_check(self,row_number,column_number,intention):
        p=column_number-2
        q=row_number-1
        flip_indices=[]
        while True:
            try:
                if p<0 or q<0:
                    return False
                if self.board()[p][q]==self.opposite_turn():
                    flip_indices.append(p)
                    p+=-1
                elif self.board()[p][q]==self.turn():
                    if intention=='flip':
                        for index in flip_indices:
                            self._board[index][q]=self.turn()
                    return len(flip_indices)>0
                else:
                    return False
            except IndexError:
                return False
            
    def upper_right_diagnol_check(self,row_number,column_number,intention):
        p=column_number
        q=row_number-2
        flip_indices=[]
        while True:
            try:
                if p<0 or q<0:
                    return False
                if self.board()[p][q]==self.opposite_turn():
                    flip_indices.append((p,q))
                    p+=1
                    q+=-1
                elif self.board()[p][q]==self.turn():
                    if intention=='flip':
                        for index in flip_indices:
                            self._board[index[0]][index[1]]=self.turn()
                    return len(flip_indices)>0
                else:
                    return False
            except IndexError:
                return False
    def lower_left_diagnol_check(self,row_number,column_number,intention):
        p=column_number-2
        q=row_number
        flip_indices=[]
        while True:
            try:
                if p<0 or q<0:
                    return False
                if self.board()[p][q]==self.opposite_turn():
                    flip_indices.append((p,q))
                    p+=-1
                    q+=1
                elif self.board()[p][q]==self.turn():
                    if intention=='flip':
                        for index in flip_indices:
                            self._board[index[0]][index[1]]=self.turn()
                    return len(flip_indices)>0
                else:
                    return False
            except IndexError:
                return False

    def upper_left_diagnol_check(self,row_number,column_number,intention):
        p=column_number-2
        q=row_number-2
        flip_indices=[]
        while True:
            try:
                if p<0 or q<0:
                    return False
                if self.board()[p][q]==self.opposite_turn():
                    flip_indices.append((p,q))
                    p+=-1
                    q+=-1
                elif self.board()[p][q]==self.turn():
                    if intention=='flip':
                        for index in flip_indices:
                            self._board[index[0]][index[1]]=self.turn()
                    return len(flip_indices)>0
                else:
                    return False
            except IndexError:
                return False
        
    def lower_right_diagnol_check(self,row_number,column_number,intention):
        p=column_number
        q=row_number
        flip_indices=[]
        while True:
            try:
                if p<0 or q<0:
                    return False
                if self.board()[p][q]==self.opposite_turn():
                    flip_indices.append((p,q))
                    p+=1
                    q+=1
                elif self.board()[p][q]==self.turn():
                    if intention=='flip':
                        for index in flip_indices:
                            self._board[index[0]][index[1]]=self.turn()
                    return len(flip_indices)>0
                else:
                    return False
            except IndexError:
                return False
                    

# PRIVATE FUNCTIONS
def _new_game_board(BOARD_COLUMNS,BOARD_ROWS,top_left) -> [[str]]:
    '''
    Creates a new game board.  Initially, a game board has the size
    BOARD_COLUMNS x BOARD_ROWS and is comprised only of strings with the
    value NONE
    '''
    if top_left=='w':
        p=WHITE
        q=BLACK
    else:
        p=BLACK
        q=WHITE
    board = []
    for col in range(BOARD_COLUMNS):
        board.append([])
        for row in range(BOARD_ROWS):
            board[-1].append(NONE)
    board[int(BOARD_COLUMNS/2)-1][int(BOARD_ROWS/2)-1] =p
    board[int(BOARD_COLUMNS/2)-1][int(BOARD_ROWS/2)] =q
    board[int(BOARD_COLUMNS/2)][int(BOARD_ROWS/2)-1] =q
    board[int(BOARD_COLUMNS/2)][int(BOARD_ROWS/2)] =p
    return board

        
                    
                    
                    
                    
                    
                    
                    
            
            
            
            
        
        
        
        
    



