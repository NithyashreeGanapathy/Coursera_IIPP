# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math

#iniatilizing global variables here...
num_range = 100
no_of_remaining_guess = 0
secret_no = 0


# helper function to start and restart the game
def new_game():
        # initialize global variables used in your code here
    global no_of_remaining_guess , secret_no
    secret_no = random.randrange(0, num_range)
    no_of_remaining_guess = int(math.ceil((math.log(num_range, 2))))
    print " " 
    # remove this when you add your code    
   



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
        
    # remove this when you add your code    
    global num_range
    num_range = 100
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is ", no_of_remaining_guess
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
                
    global num_range
    num_range = 1000
    print "New game. Range is from 0 to", num_range
    print "Number of remaining guesses is ", no_of_remaining_guess
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global no_of_remaining_guess
    # remove this when you add your code
    no = int(guess)
    no_of_remaining_guess -= 1
    print "Guess was ",no
    print "Guesses Remaining : ",no_of_remaining_guess
    if no == secret_no :
        print "Hurray! You are Corrrect!!!"
        print " "
        new_game()
        return 
    elif no > secret_no :
        print "Lower"
        print " "
    else :
        print "Higher"
        print " "
        
    if no_of_remaining_guess == 0:
        print "Alas!! Moves are exhausted !"
        print "The Secret Number is : ",secret_no
        new_game()
        print " "
        return
    
        
        
# create frame
n = simplegui.create_frame("Guess the number game!" ,234 ,234)
n.add_button("Range is [0 , 100)", range100 , 200)
n.add_button("Range is [0 , 1000)",range1000 , 200)
n.add_input("Enter your guess here : ",input_guess , 150)
# register event handlers for control elements and start frame
n.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
