import socket
from collections import namedtuple

GameConnection = namedtuple('GameConnection',['socket', 'socket_in', 'socket_out'])

def read_host()->str:
    '''Prompts the user to enter a valid host name and returns it
    '''
    while True:
        host=input('Enter host name: ')
        if len(host)==0:
            print('Invalid Host Name')
        elif type(host) is not str:
            print('Host name must be alphabets')
        else:
            break
    return host

def read_port() -> int:
    '''Prompts the user to enter a valid port number and returns it
    '''
    while True:
        try:
            port = int(input('Port: ').strip())
            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port
        except ValueError:
            print('Ports must be an integer between 0 and 65535')

def connect(H:'host',P:'Port')->namedtuple:
    '''Takes the host and port as parameters and creates a socket object and makes
       pseudo_files for socket_in and socket_out and connects to the host and port
    '''
    game_socket=socket.socket()
    
    game_socket.connect((H,P))   
    game_socket_in=game_socket.makefile('r')
    game_socket_out=game_socket.makefile('w')

    return GameConnection(socket = game_socket,socket_in =game_socket_in,socket_out = game_socket_out)

def establish_connection():
    '''Calls the connect function and establishes a connection between the host and
      port entered by the user and prints an error message if the entered host or port
      is incorrect.
    '''
    while True:
        try:
            connection=connect(read_host(),read_port())
            if type(connection)==GameConnection:
                return connection
        except socket.gaierror:
            print('Host does not exist')
        except ConnectionRefusedError:
            print('Connection refused as port number was incorrect')
        except OSError:
            print('No route to Host')
            
def read(connection:GameConnection):
    '''Takes the game connection as an argument and receives
      and prints the messages from the server. If the server sends a move(DROP/POP)
      it returns the message   
    '''
    while True:
        line = read_line(connection)
        if line.split()[0]=='DROP' or line.split()[0]=='POP':
            print(line)
            return line
            
def send(connection:GameConnection,message:str):
    _write_line(connection,message)
    
def close(connection: GameConnection) -> None:
    'Closes the connection to the server'
    connection.socket_in.close()
    connection.socket_out.close()
    connection.socket.close()

def read_line(connection: GameConnection) -> str:
    '''
    Reads a line of text sent from the server and returns it without
    a newline on the end of it
    '''
    return connection.socket_in.readline()[:-1]

# PRIVATE FUNCTIONS

def _write_line(connection: GameConnection, line: str) -> None:
    '''
    Writes a line of text to the server, including the appropriate
    newline sequence, and ensures that it is sent immediately.
    '''
    connection.socket_out.write(line + '\r\n')
    connection.socket_out.flush()
