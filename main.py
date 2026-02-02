# Tic Tac Toe ################################################################



# vars for move numbers and states
playerMove_1 = "n" 
playerMove_2 = "n" 
playerMove_3 = "n" 
playerMove_4 = "n" 
playerMove_5 = "n" 

botMove1 = "n"
botMove2 = "n"
botMove3 = "n"
botMove4 = "n"
botMove5 = "n"

# this helps the convertMovesToSquare FUNC work correctly
# move just takes on the value of the most recent (closet above) var
move = playerMove_1
move = playerMove_2
move = playerMove_3
move = playerMove_4


# vars for square states
s1 = "1"
s2 = "2"
s3 = "3"
s4 = "4"
s5 = "5"
s6 = "6"
s7 = "7"
s8 = "8"
s9 = "9"


# intro
intro = ("""
Let's play Tic-Tac-Toe!
You're Xs, I'm Os.
I'm gonna whip your tail!
""")

# FUNCs ################################################################

def showBoard():    

    # show the board with dynamic states
    print("\n"
    ,s1,"|",s2,"|",s3,"\n"
    #,"----------\n"
    ,s4,"|",s5,"|",s6,"\n"
    #,"----------\n"
    ,s7,"|",s8,"|",s9)


# check to see if anyone won
def didAnyoneWin():

    # the 3 horizontal PLAYER wins
    if s1 == "X" and s2 == "X" and s3 == "X":
        print("\n You won sassypants!")
        exit()
    elif s4 == "X" and s5 == "X" and s6 == "X":
        print("\n You won, but you're still ugly!")
        exit()
    elif s7 == "X" and s8 == "X" and s9 == "X":
        print("\n You won, but your personality is straight trash!")
        exit()

    # the 3 vertical PLAYER wins
    elif s1 == "X" and s4 == "X" and s7 == "X":
        print("\n You won, but I'm pretty sure you cheated somehow.")
        exit()
    elif s2 == "X" and s5 == "X" and s8 == "X":
        print("\n You won sweety-pie!")
        exit()
    elif s3 == "X" and s6 == "X" and s9 == "X":
        print("\n You won sweaty-pie! (not a typo)")
        exit()

    # the 3 diagonal PLAYER wins
    elif s1 == "X" and s5 == "X" and s9 == "X":
        print("\n You won, but yo mama fat!")
        exit()
    elif s3 == "X" and s5 == "X" and s7 == "X":
        print("\n You won, but yo daddy hairline is dogwater!")
        exit()

    # the 3 horizontal BOT wins
    elif s1 == "O" and s2 == "O" and s3 == "O":
        print("\n I won, and YOU SUCK!")
        exit()
    elif s4 == "O" and s5 == "O" and s6 == "O":
        print("\n I won because you are so dumb!")
        exit()
    elif s7 == "O" and s8 == "O" and s9 == "O":
        print("\n I won! :D")
        exit()

    # the 3 vertical BOT wins
    elif s1 == "O" and s4 == "O" and s7 == "O":
        print("\n I won, and I will keep on winning because you are terrible.")
        exit()
    elif s2 == "O" and s5 == "O" and s8 == "O":
        print("\n Guess what sweetcheeks? I WON!")
        exit()
    elif s3 == "O" and s6 == "O" and s9 == "O":
        print("\n I won becuase you are buns hun!")
        exit()

    # the 3 diagonal BOT wins
    elif s1 == "O" and s5 == "O" and s9 == "O":
        print("\n I won and you smell like cheese!")
        exit()
    elif s3 == "O" and s5 == "O" and s7 == "O":
        print("\n I won. Maybe you would like to play something easier, like catch?")
        exit()

    
    else:
        #print("Nobody won yet!")
        pass
    
    

# convert player numbers to squares to display the board
def convertPlayerMovesToSquares(move):

    global s1,s2,s3,s4,s5,s6,s7,s8,s9
    
    if move == 1 and s1 == " ":
        s1 = "X"
    elif move == 2 and s2 == " ":
        s2 = "X"
    elif move == 3 and s3 == " ":
        s3 = "X"
    elif move == 4 and s4 == " ":
        s4 = "X"
    elif move == 5 and s5 == " ":
        s5 = "X"
    elif move == 6 and s6 == " ":
        s6 = "X"
    elif move == 7 and s7 == " ":
        s7 = "X"
    elif move == 8 and s8 == " ":
        s8 = "X"
    elif move == 9 and s9 == " ":
        s9 = "X"

    else:
            print("ERROR 1: This error must be fixed BEFORE we get to this convert FUNC.")
    



# error-handling FUNCs for the player inputs - 1
def playerMove1FUNC():
    global playerMove_1
    try: 
        playerMove_1 = int(input("\n 1. You get the first turn. Choose a square (1-9). ")) # player move 1 input 
        if playerMove_1 == 0 or playerMove_1 > 9:
            print("Gimme a number between 1-9 genius!")
            playerMove1FUNC()
        elif playerMove_1 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            pass #print("Thanks: ", playerMove_1)
            #print("playerMove1FUNC is working great!")
        else:
            print("ERROR 2")
    except ValueError:
        print("Gimme a number between 1-9 genius!")
        playerMove1FUNC()

# error-handling FUNCs for the player inputs - 2
def playerMove2FUNC():
    global playerMove_2
    try: 
        playerMove_2 = int(input("\n 2. This is your second turn. Choose a square (1-9). ")) # player move 2 input 
        if playerMove_2 == 0 or playerMove_2 > 9:
            print("Gimme a number between 1-9 genius!")
            playerMove2FUNC()
        elif playerMove_2 == playerMove_1:
            print("You already used that square ding-dong!")
            playerMove2FUNC()
        elif botMove1 == playerMove_2:
            print("I already used that square you dolt!")
            playerMove2FUNC()
        elif playerMove_2 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            pass #print("Thanks: ", playerMove_1)
            #print("playerMove2FUNC is working great!") 
        else:
            print("ERROR 3")
    except ValueError:
        print("Gimme a number between 1-9 genius!")
        playerMove2FUNC()

# error-handling FUNCs for the player inputs - 3
def playerMove3FUNC():
    global playerMove_3
    try: 
        playerMove_3 = int(input("\n 3. This is your third turn. Choose a square (1-9). ")) # player move 3 input 
        if playerMove_3 == 0 or playerMove_3 > 9:
            print("Gimme a number between 1-9 genius!")
            playerMove3FUNC()
        elif playerMove_3 == playerMove_1 or playerMove_3 == playerMove_2:
            print("You already used that square ding-dong!")
            playerMove3FUNC()
        elif botMove2 == playerMove_3 or botMove1 == playerMove_3:
            print("I already used that square you dolt!")
            playerMove3FUNC()
        elif playerMove_3 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            pass #print("Thanks: ", playerMove_1)
            #print("playerMove3FUNC is working great!")
            #print("Diagnostics for botMove2:",botMove2)
        else:
            print("ERROR 4")
    except ValueError:
        print("Gimme a number between 1-9 genius!")
        playerMove3FUNC()

# error-handling FUNCs for the player inputs - 4
def playerMove4FUNC():
    global playerMove_4
    try: 
        playerMove_4 = int(input("\n 4. This is your fourth turn, great game! Choose a square (1-9). ")) # player move 4 input 
        if playerMove_4 == 0 or playerMove_4 > 9:
            print("Gimme a number between 1-9 genius!")
            playerMove4FUNC()
        elif playerMove_4 == playerMove_3 or playerMove_4 == playerMove_2 or playerMove_4 == playerMove_1:
            print("You already used that square ding-dong!")
            playerMove4FUNC()
        elif botMove3 == playerMove_4 or botMove2 == playerMove_4 or botMove1 == playerMove_4:
            print("I already used that square you dolt!")
            playerMove4FUNC()
        elif playerMove_4 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            pass #print("Thanks: ", playerMove_1)
            #print("playerMove4FUNC is working great!")
        else:
            print("ERROR 5")
    except ValueError:
        print("Gimme a number between 1-9 genius!")
        playerMove4FUNC()

# error-handling FUNCs for the player inputs - 5
def playerMove5FUNC():
    global playerMove_5
    try: 
        playerMove_5 = int(input("\n 5. This is your fifth and final turn, make it count! Choose a square (1-9). ")) # player move 5 input 
        if playerMove_5 == 0 or playerMove_5 > 9:
            print("Gimme a number between 1-9 genius!")
            playerMove5FUNC()
        elif playerMove_5 == playerMove_4 or playerMove_5 == playerMove_3 or playerMove_5 == playerMove_2 or playerMove_5 == playerMove_1:
            print("You already used that square ding-dong!")
            playerMove5FUNC()
        elif botMove4 == playerMove_5 or botMove3 == playerMove_5 or botMove2 == playerMove_5 or botMove1 == playerMove_5:
            print("I already used that square you dolt!")
            playerMove5FUNC()
        elif playerMove_5 == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
            pass #print("Thanks: ", playerMove_1)
            #print("playerMove5FUNC is working great!")
        else:
            print("ERROR 6")
    except ValueError:
        print("Gimme a number between 1-9 genius!")
        playerMove5FUNC()

'''
# some version of this delay might be helpful but i dont know how yet
import time
time.sleep(15) # mkes it impossible to move forward before the 15 secs
print("\nHurry up the program is about to time out!")
'''

# BOT DECISION-MAKING FOR EACH BOT TURN -------------------------------------------


# bot's decision-making for his 2nd turn
def bot2ndTurn():

    global s1,s2,s3,s4,s5,s6,s7,s8,s9
    global playerMove_2
    global botMove1,botMove2,botMove3,botMove4,botMove5,botMove6,botMove7,botMove8,botMove9 


    '''
    # TEMPORARY CODE TO TRY TO MAKE BOT MORE AGGRESSIVE

    # make any move if no blocks are possible
    # bot move 2 just is not offensive, but move 3 is so its fine.
    if s5 == " ":
        s5 = "O"
        botMove2 = 5

    elif s1 == " ":
        s1 = "O"
        botMove2 = 1
    elif s2 == " ":
        s2 = "O"
        botMove2 = 2
    elif s3 == " ":
        s3 = "O"
        botMove2 = 3
    elif s4 == " ":
        s4 = "O"
        botMove2 = 4
    elif s6 == " ":
        s6 = "O"
        botMove2 = 6
    elif s7 == " ":
        s7 = "O"
        botMove2 = 7
    elif s8 == " ":
        s8 = "O"
        botMove2 = 8
    elif s9 == " ":
        s9 = "O"
        botMove2 = 9
    '''




    # 1-2-3 HORIZ    
    if playerMove_2 == 1 and s2 == "X" and s3 == " ": 
        s3 = "O" #the overwrite logic is: bot can only take squares that are empty.
        botMove2 = 3
    elif playerMove_2 == 2 and s1 == "X" and s3 == " ":  
        s3 = "O" 
        botMove2 = 3
    elif playerMove_2 == 3 and s1 == "X" and s2 == " ":
        s2 = "O"
        botMove2 = 2
    elif playerMove_2 == 1 and s3 == "X" and s2 == " ":
        s2 = "O" 
        botMove2 = 2
    elif playerMove_2 == 2 and s3 == "X" and s1 == " ":
        s1 = "O" 
        botMove2 = 1
    elif playerMove_2 == 3 and s2 == "X" and s1 == " ":
        s1 = "O" 
        botMove2 = 1

    # 4-5-6 HORIZ
    elif playerMove_2 == 4 and s5 == "X" and s6 == " ":
        s6 = "O"
        botMove2 = 6 
    elif playerMove_2 == 5 and s4 == "X" and s6 == " ":
        s6 = "O"
        botMove2 = 6 
    elif playerMove_2 == 4 and s6 == "X" and s5 == " ":
        s5 = "O" 
        botMove2 = 5
    elif playerMove_2 == 6 and s4 == "X" and s5 == " ":
        s5 = "O" 
        botMove2 = 5
    elif playerMove_2 == 5 and s6 == "X" and s4 == " ":
        s4 = "O" 
        botMove2 = 4
    elif playerMove_2 == 6 and s5 == "X" and s4 == " ":
        s4 = "O" 
        botMove2 = 4

    # 7-8-9 HORIZ
    elif playerMove_2 == 7 and s8 == "X" and s9 == " ":
        s9 = "O" 
        botMove2 = 9
    elif playerMove_2 == 8 and s7 == "X" and s9 == " ":
        s9 = "O" 
        botMove2 = 9
    elif playerMove_2 == 7 and s9 == "X" and s8 == " ":
        s8 = "O" 
        botMove2 = 8
    elif playerMove_2 == 9 and s7 == "X" and s8 == " ":
        s8 = "O" 
        botMove2 = 8
    elif playerMove_2 == 8 and s9 == "X" and s7 == " ":
        s7 = "O" 
        botMove2 = 7
    elif playerMove_2 == 9 and s8 == "X" and s7 == " ":
        s7 = "O" 
        botMove2 = 7

    # 1-4-7 VERTICAL
    elif playerMove_2 == 1 and s4 == "X" and s7 == " ":
        s7 = "O" 
        botMove2 = 7
    elif playerMove_2 == 4 and s1 == "X" and s7 == " ":
        s7 = "O" 
        botMove2 = 7
    elif playerMove_2 == 1 and s7 == "X" and s4 == " ":
        s4 = "O" 
        botMove2 = 4
    elif playerMove_2 == 7 and s1 == "X" and s4 == " ":
        s4 = "O" 
        botMove2 = 4
    elif playerMove_2 == 4 and s7 == "X" and s1 == " ":
        s1 = "O"
        botMove2 = 1 
    elif playerMove_2 == 7 and s4 == "X" and s1 == " ":
        s1 = "O" 
        botMove2 = 1

    # 2-5-8 VERTICAL
    elif playerMove_2 == 2 and s5 == "X" and s8 == " ":
        s8 = "O" 
        botMove2 = 8
    elif playerMove_2 == 5 and s2 == "X" and s8 == " ":
        s8 = "O" 
        botMove2 = 8
    elif playerMove_2 == 2 and s8 == "X" and s5 == " ":
        s5 = "O" 
        botMove2 = 5
    elif playerMove_2 == 8 and s2 == "X" and s5 == " ":
        s5 = "O"
        botMove2 = 5 
    elif playerMove_2 == 8 and s5 == "X" and s2 == " ":
        s2 = "O" 
        botMove2 = 2
    elif playerMove_2 == 5 and s8 == "X" and s2 == " ":
        s2 = "O" 
        botMove2 = 2

    # 3-6-9 VERTICAL
    elif playerMove_2 == 3 and s6 == "X" and s9 == " ":
        s9 = "O" 
        botMove2 = 9
    elif playerMove_2 == 6 and s3 == "X" and s9 == " ":
        s9 = "O" 
        botMove2 = 9
    elif playerMove_2 == 3 and s9 == "X" and s6 == " ":
        s6 = "O" 
        botMove2 = 6
    elif playerMove_2 == 9 and s3 == "X" and s6 == " ":
        s6 = "O" 
        botMove2 = 6
    elif playerMove_2 == 9 and s6 == "X" and s3 == " ":
        s3 = "O" 
        botMove2 = 3
    elif playerMove_2 == 6 and s9 == "X" and s3 == " ":
        s3 = "O" 
        botMove2 = 3

    # 1-5-9 DIAGONAL
    elif playerMove_2 == 1 and s5 == "X" and s9 == " ":
        s9 = "O" 
        botMove2 = 9
    elif playerMove_2 == 5 and s1 == "X" and s9 == " ":
        s9 = "O" 
        botMove2 = 9
    elif playerMove_2 == 1 and s9 == "X" and s5 == " ":
        s5 = "O" 
        botMove2 = 5
    elif playerMove_2 == 9 and s1 == "X" and s5 == " ":
        s5 = "O" 
        botMove2 = 5
    elif playerMove_2 == 5 and s9 == "X" and s1 == " ":
        s1 = "O" 
        botMove2 = 1
    elif playerMove_2 == 9 and s5 == "X" and s1 == " ":
        s1 = "O" 
        botMove2 = 1

    # 3-5-7 DIAGONAL
    elif playerMove_2 == 3 and s5 == "X" and s7 == " ":
        s7 = "O" 
        botMove2 = 7
    elif playerMove_2 == 5 and s3 == "X" and s7 == " ":
        s7 = "O"
        botMove2 = 7 
    elif playerMove_2 == 3 and s7 == "X" and s5 == " ":
        s5 = "O"
        botMove2 = 7 
    elif playerMove_2 == 7 and s3 == "X" and s5 == " ":
        s5 = "O" 
        botMove2 = 5
    elif playerMove_2 == 5 and s7 == "X" and s3 == " ":
        s3 = "O"
        botMove2 = 3 
    elif playerMove_2 == 7 and s5 == "X" and s3 == " ":
        s3 = "O" 
        botMove2 = 3

    elif playerMove_2 == 9 and s4 == "X" and s5 == " ":
        s5 = "O" 
        botMove2 = 5

    else:
        print("ERROR 8")

    '''
    # make any move if no blocks are possible
    # bot move 2 just is not offensive, but move 3 is so its fine.
    elif s5 == " ":
        s5 = "O"
        botMove2 = 5

    elif s1 == " ":
        s1 = "O"
        botMove2 = 1
    elif s2 == " ":
        s2 = "O"
        botMove2 = 2
    elif s3 == " ":
        s3 = "O"
        botMove2 = 3
    elif s4 == " ":
        s4 = "O"
        botMove2 = 4
    elif s6 == " ":
        s6 = "O"
        botMove2 = 6
    elif s7 == " ":
        s7 = "O"
        botMove2 = 7
    elif s8 == " ":
        s8 = "O"
        botMove2 = 8
    elif s9 == " ":
        s9 = "O"
        botMove2 = 9
    '''


    #print("Diagnostics for botMove2:",botMove2)



# bot's decision-making for his 3rd turn
# this one looks for wins before looking for blocks
def bot3rdTurn():

    global s1,s2,s3,s4,s5,s6,s7,s8,s9
    global playerMove_3
    global botMove1,botMove2,botMove3,botMove4,botMove5,botMove6,botMove7,botMove8,botMove9

    
    # MAKE BOT TURN 3 A BIT MORE OFFENSIVE
    if s5 == "O" and s6 == "O" and s4 == " ":
        s4 = "O"
        botMove3 = "4"
    elif s1 == "O" and s2 == "O" and s3 == " ":
        s3 = "O"  
        botMove3 = "3"
    elif s7 == "O" and s8 == "O" and s9 == " ":
        s9 = "O"  
        botMove3 = "9"
    elif s1 == "O" and s5 == "O" and s9 == " ":
        s9 = "O"  
        botMove3 = "9"
    elif s2 == "O" and s5 == "O" and s8 == " ":
        s8 = "O"
        botMove3 = "8"
    elif s3 == "O" and s6 == "O" and s9 == " ":
        s9 = "O"  
        botMove3 = "9"
    elif s3 == "O" and s5 == "O" and s7 == " ":
        s7 = "O"
        botMove3 = "7"
    elif s4 == "O" and s5 == "O" and s6 == " ":
        s6 = "O"
        botMove3 = "6"
    elif s8 == "O" and s5 == "O" and s2 == " ":
        s2 = "O"
        botMove3 = "2"
    elif s7 == "O" and s4 == "O" and s1 == " ":
        s1 = "O"
        botMove3 = "1"
    elif s9 == "O" and s6 == "O" and s3 == " ":
        s3 = "O"
        botMove3 = "3"
    elif s3 == "O" and s2 == "O" and s1 == " ":
        s1 = "O"
        botMove3 = "1"
    elif s6 == "O" and s5 == "O" and s4 == " ":
        s4 = "O"
        botMove3 = "4"
 

    # 1-2-3 HORIZ
    elif playerMove_3 == 1 and s2 == "X" and s3 == " ":
        s3 = "O" #bot takes s3
        botMove3 = "3" 
    elif playerMove_3 == 2 and s1 == "X" and s3 == " ":
        s3 = "O"  
        botMove3 = "3"
    elif playerMove_3 == 3 and s1 == "X" and s2 == " ":
        s2 = "O"  
        botMove3 = "2" 
    elif playerMove_3 == 1 and s3 == "X" and s2 == " ":
        s2 = "O"  
        botMove3 = "2" 
    elif playerMove_3 == 2 and s3 == "X" and s1 == " ":
        s1 = "O"  
        botMove3 = "1" 
    elif playerMove_3 == 3 and s2 == "X" and s1 == " ":
        s1 = "O"  
        botMove3 = "1" 

    # 4-5-6 HORIZ
    elif playerMove_3 == 4 and s5 == "X" and s6 == " ":
        s6 = "O"  
        botMove3 = "6" 
    elif playerMove_3 == 5 and s4 == "X" and s6 == " ":
        s6 = "O"  
        botMove3 = "6" 
    elif playerMove_3 == 4 and s6 == "X" and s5 == " ":
        s5 = "O"
        botMove3 = "5"  
    elif playerMove_3 == 6 and s4 == "X" and s5 == " ":
        s5 = "O"
        botMove3 = "5"  
    elif playerMove_3 == 5 and s6 == "X" and s4 == " ":
        s4 = "O"
        botMove3 = "4"         
    elif playerMove_3 == 6 and s5 == "X" and s4 == " ":
        s4 = "O"
        botMove3 = "4" 

    # 7-8-9 HORIZ
    elif playerMove_3 == 7 and s8 == "X" and s9 == " ":
        s9 = "O"
        botMove3 = "9" 
    elif playerMove_3 == 8 and s7 == "X" and s9 == " ":
        s9 = "O"
        botMove3 = "9" 
    elif playerMove_3 == 7 and s9 == "X" and s8 == " ":
        s8 = "O" 
        botMove3 = "8"
    elif playerMove_3 == 9 and s7 == "X" and s8 == " ":
        s8 = "O" 
        botMove3 = "8"
    elif playerMove_3 == 8 and s9 == "X" and s7 == " ":
        s7 = "O"
        botMove3 = "7" 
    elif playerMove_3 == 9 and s8 == "X" and s7 == " ":
        s7 = "O" 
        botMove3 = "7"



    # 1-4-7 VERTICAL
    elif playerMove_3 == 1 and s4 == "X" and s7 == " ":
        s7 = "O"
        botMove3 = "7" 
    elif playerMove_3 == 4 and s1 == "X" and s7 == " ":
        s7 = "O"
        botMove3 = "7" 
    elif playerMove_3 == 1 and s7 == "X" and s4 == " ":
        s4 = "O"
        botMove3 = "4" 
    elif playerMove_3 == 7 and s1 == "X" and s4 == " ":
        s4 = "O"
        botMove3 = "4" 
    elif playerMove_3 == 4 and s7 == "X" and s1 == " ":
        s1 = "O"  
        botMove3 = "1" 
    elif playerMove_3 == 7 and s4 == "X" and s1 == " ":
        s1 = "O"  
        botMove3 = "1" 

    # 2-5-8 VERTICAL
    elif playerMove_3 == 2 and s5 == "X" and s8 == " ":
        s8 = "O" 
        botMove3 = "8"
    elif playerMove_3 == 5 and s2 == "X" and s8 == " ":
        s8 = "O"
        botMove3 = "8" 
    elif playerMove_3 == 2 and s8 == "X" and s5 == " ":
        s5 = "O"
        botMove3 = "5" 
    elif playerMove_3 == 8 and s2 == "X" and s5 == " ":
        s5 = "O"
        botMove3 = "5" 
    elif playerMove_3 == 8 and s5 == "X" and s2 == " ":
        s2 = "O"  
        botMove3 = "2" 
    elif playerMove_3 == 5 and s8 == "X" and s2 == " ":
        s2 = "O"  
        botMove3 = "2" 

    # 3-6-9 VERTICAL
    elif playerMove_3 == 3 and s6 == "X" and s9 == " ":
        s9 = "O"
        botMove3 = "9" 
    elif playerMove_3 == 6 and s3 == "X" and s9 == " ":
        s9 = "O"
        botMove3 = "9" 
    elif playerMove_3 == 3 and s9 == "X" and s6 == " ":
        s6 = "O"  
        botMove3 = "6" 
    elif playerMove_3 == 9 and s3 == "X" and s6 == " ":
        s6 = "O"  
        botMove3 = "6" 
    elif playerMove_3 == 9 and s6 == "X" and s3 == " ":
        s3 = "O"  
        botMove3 = "3" 
    elif playerMove_3 == 6 and s9 == "X" and s3 == " ":
        s3 = "O"  
        botMove3 = "3" 

    # 1-5-9 DIAGONAL
    elif playerMove_3 == 1 and s5 == "X" and s9 == " ":
        s9 = "O"
        botMove3 = "9" 
    elif playerMove_3 == 5 and s1 == "X" and s9 == " ":
        s9 = "O"
        botMove3 = "9" 
    elif playerMove_3 == 1 and s9 == "X" and s5 == " ":
        s5 = "O"
        botMove3 = "5" 
    elif playerMove_3 == 9 and s1 == "X" and s5 == " ":
        s5 = "O"
        botMove3 = "5" 
    elif playerMove_3 == 5 and s9 == "X" and s1 == " ":
        s1 = "O"  
        botMove3 = "1" 
    elif playerMove_3 == 9 and s5 == "X" and s1 == " ":
        s1 = "O"  
        botMove3 = "1" 

    # 3-5-7 DIAGONAL
    elif playerMove_3 == 3 and s5 == "X" and s7 == " ":
        s7 = "O"
        botMove3 = "7" 
    elif playerMove_3 == 5 and s3 == "X" and s7 == " ":
        s7 = "O"
        botMove3 = "7" 
    elif playerMove_3 == 3 and s7 == "X" and s5 == " ":
        s5 = "O"
        botMove3 = "5" 
    elif playerMove_3 == 7 and s3 == "X" and s5 == " ":
        s5 = "O" 
        botMove3 = "5"
    elif playerMove_3 == 5 and s7 == "X" and s3 == " ":
        s3 = "O"  
        botMove3 = "3" 
    elif playerMove_3 == 7 and s5 == "X" and s3 == " ":
        s3 = "O"  
        botMove3 = "3" 

    # make any move if no blocks are possible
    elif s5 == " ":
        s5 = "O"
        botMove3 = "5"
    elif s1 == " ":
        s1 = "O"  
        botMove3 = "1"
    elif s2 == " ":
        s2 = "O"  
        botMove3 = "2"
    elif s3 == " ":
        s3 = "O"  
        botMove3 = "3"
    elif s4 == " ":
        s4 = "O"
        botMove3 = "4"
    elif s6 == " ":
        s6 = "O"  
        botMove3 = "6"
    elif s7 == " ":
        s7 = "O"
        botMove3 = "7"
    elif s8 == " ":
        s8 = "O"
        botMove3 = "8"
    elif s9 == " ":
        s9 = "O"
        botMove3 = "9"
        
    else:
        print("ERROR 9")


# bot's 4th turn here
# 4th bot turn logic was just "fill the next available empty space", so i made this fill ANY random space version
import random
def randoNumTry():
    randoNum1to9 = random.randint(1, 9)

    global fourthBotTurnSquare
    global s1,s2,s3,s4,s5,s6,s7,s8,s9
    global botMove1,botMove2,botMove3,botMove4,botMove5,botMove6,botMove7,botMove8,botMove9
    fourthBotTurnSquare = "s" + str(randoNum1to9) # turn the int into a str so i can concantenate it with the s.

    if fourthBotTurnSquare == "s1" and s1 == " ":
        s1 = "O"  
        botMove4 = "1"
    elif fourthBotTurnSquare == "s2" and s2 == " ":
        s2 = "O"  
        botMove4 = "2"
    elif fourthBotTurnSquare == "s3" and s3 == " ":
        s3 = "O"  
        botMove4 = "3"
    elif fourthBotTurnSquare == "s4" and s4 == " ":
        s4 = "O" 
        botMove4 = "4" 
    elif fourthBotTurnSquare == "s5" and s5 == " ":
        s5 = "O"
        botMove4 = "5" 
    elif fourthBotTurnSquare == "s6" and s6 == " ":
        s6 = "O"
        botMove4 = "6"
    elif fourthBotTurnSquare == "s7" and s7 == " ":
        s7 = "O"
        botMove4 = "7"
    elif fourthBotTurnSquare == "s8" and s8 == " ":
        s8 = "O"
        botMove4 = "8"
    elif fourthBotTurnSquare == "s9" and s9 == " ":
        s9 = "O" 
        botMove4 = "9" 

    else:    
        randoNumTry()
        fourthBotTurnSquare = "O"


# begin script here #####################################################################


#intro
print(intro)

#showboard just BEFORE the numbers are removed
showBoard()

# vars for square states CHANGED TO EMPTY
s1 = " "
s2 = " "
s3 = " "
s4 = " "
s5 = " "
s6 = " "
s7 = " "
s8 = " "
s9 = " "




# player move 1 input ------------------------------------------------------------------
playerMove1FUNC()

#convert move to squares with the correct argument passed
convertPlayerMovesToSquares(playerMove_1)

#showboard AFTER the numbers are removed and the player has moved the game's first turn
showBoard()


input("\n 1. Ok it's my turn. Press enter. ")


# player move 1 bot DEFENSIVE responses
# OFFENSIVE responses to the first player move dont seem very vital so we'll just use a simple block to start

if playerMove_1 == 1:
    s2 = "O" #bot takes 2
    botMove1 = 2
elif playerMove_1 == 2:
    s1 = "O" 
    botMove1 = 1
elif playerMove_1 == 3:
    s1 = "O" 
    botMove1 = 1
elif playerMove_1 == 4:
    s6 = "O" 
    botMove1 = 6
elif playerMove_1 == 5:
    s4 = "O" 
    botMove1 = 4
elif playerMove_1 == 6:
    s4 = "O"
    botMove1 = 4
elif playerMove_1 == 7:
    s8 = "O"
    botMove1 = 8
elif playerMove_1 == 8:
    s7 = "O"
    botMove1 = 7 
elif playerMove_1 == 9:
    s8 = "O" 
    botMove1 = 8

else:
    print("ERROR 7")


'''
# a decent all-purpose OFFENSIVE response to the player's 1st move is just to take 5 (if it's available)
# HOW DO I WORK THIS INTO MY DEFENSIVE LOGIC?

if playerMove_1 != 5:
    s5 = "O" #bot takes 5
else:
    s1 = "O" #bot takes 1
'''

#showboard
showBoard()



# player move 2 input ------------------------------------------------------------------
playerMove2FUNC()

#convert move to squares with the correct argument passed
convertPlayerMovesToSquares(playerMove_2)

#showboard
showBoard()


#bots pre-2nd-turn stopping point
input("\n 2. Now it's my second turn. Press enter. ")


'''
# import the logic FUNCs from a sep py file (for clairty on this script page)
from ttt_combos import bot2ndTurn 
# I could never get this to work without importing the whole page in and causing errors and codependencies :(
'''

#bots 2nd turn
bot2ndTurn()

#showboard
showBoard()

'''
is 2nd bot turn good??
print("make sure 2nd bot turn is clean before moving on!")
exit()
'''

# player move 3 input ------------------------------------------------------------------
playerMove3FUNC() 

#convert move to squares with the correct argument passed
convertPlayerMovesToSquares(playerMove_3)

#showboard
showBoard()

#check to see if anyone won yet
didAnyoneWin()

#bots pre-3rd-turn stopping point
input("\n 3. Here's my third turn. Press enter. ")

# bots 3rd turn
bot3rdTurn()

#showboard
showBoard()

#check to see if anyone won yet
didAnyoneWin()


'''
# is 3rd bot turn good??
print("make sure 3rd bot turn is clean before moving on!!!!!!")
exit()
'''





# player move 4 input ------------------------------------------------------------------
playerMove4FUNC()

#convert move to squares with the correct argument passed
convertPlayerMovesToSquares(playerMove_4)

#showboard
showBoard()

#check to see if anyone won yet
didAnyoneWin()


#bots pre-4th-turn stopping point
input("\n 4. Now it's my fourth turn. I'm gonna ring your pants! Press enter. ")


# this is actually bot's 4th turn
randoNumTry()


#showboard
showBoard()

#check to see if anyone won yet
didAnyoneWin()





# player move 5 input ------------------------------------------------------------------
playerMove5FUNC() 

#convert move to squares with the correct argument passed
convertPlayerMovesToSquares(playerMove_5)



#showboard
showBoard()

#check to see if anyone won yet
didAnyoneWin()

# gameover. this doesnt show if there's a win
print("\nStalemate, let's play again SUCKA!")
