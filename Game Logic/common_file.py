#Common Functions between Console UI and Network UI
import connectfour

def board_display(game:'Game state') -> None:  
    ''' Takes the current game state as an argument and prints the the game board
    '''
    i=''
    for col in range(connectfour.BOARD_COLUMNS):
        i=i+str(col+1)+'   '
    print(i)
        
    for row in range(connectfour.BOARD_ROWS):
        for col in range(connectfour.BOARD_COLUMNS):
            if game.board[col][row]==' ':
                pixel='*'
            else:
                pixel=game.board[col][row]
            print(pixel,sep=' ',end='   ')
        print()

def game_move(s:'gamestate',message:str):
    '''Takes a game state and and message as arguments and drops or pops a piece if the message
       is DROP or POP respectively and returns the game state
    '''
    try:
        move=message.split()[0]
        column_number=int(message.split()[1])
        if len(message.split())>2:
            raise ValueError
        if move=='DROP':
            return connectfour.drop_piece(s,column_number-1)
        elif move=='POP':
            return connectfour.pop_piece(s,column_number-1)
        else:
            return None
    except connectfour.InvalidConnectFourMoveError:
        return None
    except ValueError:
        print('Invalid Column Number')
    except IndexError:
        return None
