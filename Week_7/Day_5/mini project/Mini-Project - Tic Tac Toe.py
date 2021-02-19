#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'00': ' ' , '01': ' ' , '02': ' ' ,
            '10': ' ' , '11': ' ' , '12': ' ' ,
            '20': ' ' , '21': ' ' , '22': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print("*************")
    print("* " + board['00'] + ' | ' + board['01'] + ' | ' + board['02'] + " *")
    print('* --|---|-- *')
    print("* " + board['10'] + ' | ' + board['11'] + ' | ' + board['12'] + " *")
    print('* --|---|-- *')
    print("* "+ board['20'] + ' | ' + board['21'] + ' | ' + board['22']+ " *")
    print('* --|---|-- *')
    print("*************")



# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)

        row = input("enter row : ")
        col = input("enter column : ") 
        move = row + "" + col
        if move != "" :       
            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                continue
        elif move == "" :
            printBoard(theBoard)
            row = input("enter row : ")
            col = input("enter column : ") 
            move = row + "" + col


        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['00'] == theBoard['01'] == theBoard['02'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['10'] == theBoard['11'] == theBoard['12'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['20'] == theBoard['21'] == theBoard['22'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['20'] == theBoard['10'] == theBoard['00'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['21'] == theBoard['11'] == theBoard['01'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['22'] == theBoard['12'] == theBoard['02'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['00'] == theBoard['11'] == theBoard['22'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['20'] == theBoard['11'] == theBoard['02'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()