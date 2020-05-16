#Othello_UI.py
# This module implements the User Interface for the game

import Othello_Class

def game_move(s:'Game State'):
    while True:
        try:
            print('Player ', Othello_Class.GameState.turn(s))
            col=int(input('Enter column number: '))
            row=int(input('Enter row number: '))
            if col<1 or row<1:
                print('Invalid Column number or row number')
            elif Othello_Class.GameState.board(s)[col-1][row-1]==Othello_Class.NONE:
                valid_move=Othello_Class.GameState.board_check(s,row,col,'flip')
                if valid_move==True:
                    Othello_Class.GameState.drop_piece(s,row,col)
                    board_display(s)
                    return
                else:
                    print('Not a Valid move')
            else:
                print('Not a valid move.Cell already filled')
        except Othello_Class.InvalidOthelloMoveError:
            print('Invalid Move')
        except ValueError:
            print('Column and row number must be an integer')
        except IndexError:
            print('Invalid Column number or row number')
        

def game_handler(s:'Game State'):
    while True:
        winning_player=Othello_Class.GameState.winning_player(s)
        if winning_player==Othello_Class.NONE:
            game_move(s)
        else:
            return winning_player
    
def board_display(game:'Game state') -> None:  
    ''' Takes the Game State as a parameter and prints the Game Board
    '''
    print('SCORE')
    print('WHITE: ',Othello_Class.GameState.white_count(s),'BLACK: ',Othello_Class.GameState.black_count(s))
    i=''
    for col in range(Othello_Class.GameState.columns(s)):
        i=i+str(col+1)+'    '
    print(i)
        
    for row in range(Othello_Class.GameState.rows(s)):
        for col in range(Othello_Class.GameState.columns(s)):
            if game.board()[col][row]==' ':
                pixel='*'
            else:
                pixel=game.board()[col][row]
            print(pixel,sep=' ',end='     ')
        print()
    
def top_left()->str:
    while True:
        player=input('Enter the colour of top left disc')
        if player.lower() not in ['w','b']:
            print('Invalid input')
        else:
            return player.lower()
        
def winning_option():
     while True:
        option=input('Enter the winning option for the game (most discs or least discs ) (M/L)')
        if option.lower() not in ['m','l']:
            print('Invalid input')
        else:
            return option.lower()

def first_turn()->str:
    while True:
        player=input('Enter whose turn should be first: (W,B)')
        if player.lower() not in ['w','b']:
            print('Invalid input')
        else:
            return player.lower()
        
def get_rows()->int:
    while True:
        try:
            rows=int(input('Enter the number of rows: '))
            if rows>= 4 and rows<=16 and (rows%2)==0:
                return rows
            else:
                print('Rows must be an even integer between 4 to 16')
        except ValueError:
            print('Rows must be an integer between 4 to 16')

def get_columns()->int:
    while True:
        try:
            columns=int(input('Enter the number of columns: '))
            if columns>= 4 and columns<=16 and (columns%2)==0:
                return columns
            else:
                print('Columns must be an even integer between 4 to 16')
        except ValueError:
            print('Columns must be an even integer between 4 to 16')
    

if __name__ == '__main__':
    print('Welcome to Othello Game')
    s=Othello_Class.GameState(get_columns(),get_rows(),first_turn(),top_left(),winning_option())
    board_display(s)
    winner=game_handler(s)
    print('Winner is ', winner)
    
    print('Game Over\n')
    print('Thank you for playing')
