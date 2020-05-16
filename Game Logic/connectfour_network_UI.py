import connectfour
import server
import common_file

def read_username()->str:
    '''Prompts the user to enter a valid username and returns it
    '''
    while True:
        username=input('Enter a username: ')
        username=username.strip()
        if len(username.split()) is not 1:
            print('Username cannot contain whitespace characters')
        else:
            break
    return username

def game_handler(connection:server.GameConnection,s:'Game State'):
    '''Takes the game state and game connection as arguments and calls the game_play function
       and the board_display function for each players move and returns the winning player
    '''
    print('WELCOME TO CONNECT 4 GAME')
    
    username=read_username()
    server.send(connection,'I32CFSP_HELLO '+username)
    print(server.read_line(connection))
    
    server.send(connection,'AI_GAME ')
    print(server.read_line(connection))
   
    while True:
        if connectfour.winning_player(s)==connectfour.NONE:
            if s.turn==connectfour.RED:
                print('Player ',username)
                s=game_play(s,connection)
                common_file.board_display(s)
            elif s.turn==connectfour.YELLOW:
                print('Player AI')
                s=common_file.game_move(s,server.read(connection))                  
                if s==None:
                    print('Invalid move by Server')
                    server.close(connection)
                    return None
                common_file.board_display(s)                             
        elif connectfour.winning_player(s)==connectfour.RED:
            return username
        elif connectfour.winning_player(s)==connectfour.YELLOW:
            return 'AI'
            
        
def game_play(s:'GameState',connection:server.GameConnection):
    '''Takes  game state and GameConnection as arguments asks the user to enter their
      move  and returns the game state after the user has made their move and sends the
      move to the server
    '''
    while True:
        User_input=input('Enter (D/P) to drop or pop: ')
        if User_input.strip().upper()=='D':
            move='DROP'
        elif User_input.strip().upper()=='P':
            move='POP'
        else :
            move=' '
        column_number=input('Please Enter Column Number: ')
        column_number=column_number.strip()

        User_message=move+' '+column_number
        g=common_file.game_move(s,User_message)
        if g==None:
            print('Invalid Move')
        else:
            server.send(connection,User_message)
            return g

if __name__ == '__main__':    
    connection=server.establish_connection()
    try:
        winner=game_handler(connection,connectfour.new_game_state())
        if winner==None:
            print('Connection closed due to incorrect move by Server')
        else:
            print('PLAYER ',winner,'WINS')
            print('Game Over')
    except OSError:
        print('Connection lost')
