import connectfour
import common_file

def game_play(s:'GameState'):
    '''Takes a game state and asks the user to enter their move (DROP OR POP) and  calls the
      game move function (with the User Move as a parameter) and returns the new game
      state after the user has made their move
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
            return g

def game_handler(s:'Game State'):
    '''Takes the current game state as an argument and calls the game_play function
       and the board_display function for each players move and returns the winning player
    '''
    while True:
        if connectfour.winning_player(s)==connectfour.NONE:
            if s.turn==connectfour.RED:
                print('Player RED')
                s=game_play(s)
                common_file.board_display(s)
            elif s.turn==connectfour.YELLOW:
                print('Player YELLOW')
                s=game_play(s)
                common_file.board_display(s)                             
        elif connectfour.winning_player(s)==connectfour.RED:
            return 'RED'
        elif connectfour.winning_player(s)==connectfour.YELLOW:
            return 'YELLOW'
    

if __name__ == '__main__':
    print('Connect Four game')
    winner=game_handler(connectfour.new_game_state())
    print('GAME OVER')
    print('Player ',winner,' wins')
