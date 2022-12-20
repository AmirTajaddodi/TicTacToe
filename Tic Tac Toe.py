def display_board(board):
    
    print( board[1] + ' | ' + board[2] + ' | ' + board[3])
    print( board[4] + ' | ' + board[5] + ' | ' + board[6])
    print( board[7] + ' | ' + board[8] + ' | ' + board[9])

def user_sign():
    
    
    sign = ''
    
    while sign != 'X' and sign != 'O':
        
        sign = input('Player 1, Choose X or O: ').upper()
        
    player_1 = sign
    
    if player_1 == 'X':
        player_2 = 'O'
        
    elif player_1 == 'O':
        player_2 = 'X'
        
    return player_1,player_2

def place_marker(board,marker,player):
    
    position  = ''
    
    within_range = False
 
    
    while within_range == False or position.isdigit() == False:
        position = input(f'{player} Pick a Box to Place Your Marker: ')
       
        if position.isdigit() == False:
            print('Not valid. Please Pick a number between 0-8')
            
        else:
            if int(position) in range(1,10):
                within_range = True
                
            else:
                print('Not valid range. Please Pick a Number Between 0-8')
                

    while board[int(position)] != ' ':
        
        if board[int(position)] != ' ':
            print('This Position is Not Valid as it is Already Taken')
            position = input('Pick a Box to Place Your Marker: ')
        
  
    
    else:
        board[int(position)] = marker

def win_check(board,marker):
    
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or 
    (board[4] == marker and board[5] == marker and board[6] == marker) or
    (board[6] == marker and board[7] == marker and board[8] == marker) or 
    (board[1] == marker and board[5] == marker and board[9] == marker) or
    (board[3] == marker and board[5] == marker and board[7] == marker) or
    (board[1] == marker and board[4] == marker and board[7] == marker) or
    (board[2] == marker and board[5] == marker and board[8] == marker) or
    (board[3] == marker and board[6] == marker and board[9] == marker))

def replay():
    
    answer = ''
    
    while answer != 'Y' and answer != 'N':
        
        answer = input('Do You Want to Replay (Y/N): ').upper()
        
    return answer == 'Y'

def full_board_check(board):
    empty= ' '
    if empty not in board:
        return True
    else:
        return False

import random
def who_goes_first():
    
    if random.randint(0,1) == 0:
        turn = player_1
    elif random.randint(0,1) == 1:
        turn = player_2
        
    return turn

print('Welcome to Tic Tac Toe!')

game_on = True

player_1 = 'Player 1'
player_2 = 'Player 2'

turn = who_goes_first()

while game_on:

    game_board = ['#'] +[' ']*9
    
    player1_marker,player2_marker = user_sign()
    print('\n'+turn +', Will Go First!\n')
    
    while True:
        if turn == 'Player 1':
            display_board(game_board)

            place_marker(game_board,player1_marker,player_1)
        
            if win_check(game_board,player1_marker):
                print('\nPlayer 1 Wins!!' )
                display_board(game_board)
                break
                
            if full_board_check(game_board):
                display_board(game_board)
                print('\nThe Game is a Draw\n')
                break
                
            turn = 'Player 2'
        else:
            display_board(game_board)
            
            place_marker(game_board,player2_marker,player_2)
        
            if win_check(game_board,player2_marker):
                print('\nPlayer 2 Wins!!')
                display_board(game_board)
                break
                
            if full_board_check(game_board):
                display_board(game_board)
                print('\nThe Game is a Draw\n')
                break  
                
            turn  =  'Player 1'

    if not replay():
        
        game_on = False
        print('\nThank You For Playing!')
        