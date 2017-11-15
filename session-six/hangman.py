'''
A simple version of the "classic" hangman game to "guess" the characters in a secret word
'''

#importing the time module
import time

def main():
    user = get_user_name()
    #set the number of turns
    TURNS = 10

    secret = get_secret_word()

    #wait for 1 second
    time.sleep(1)

    print("Start guessing...")
    time.sleep(0.5)

    if (game_loop(TURNS,secret)):
        print("You won!")
    else:
        print("You loose!")

def get_user_name():
    #welcoming the user
    name = input("What is your name? ")
    print("Hello, " + name, "Time to play hangman!")
    print()
    return name

def get_secret_word():
    # could be some complicated computation
    return "secret"

def game_loop(LIMIT, word):
    #creates an variable with an empty value
    guesses = ''
    turns = LIMIT

    #check if the turns are more than zero
    while turns > 0:         
        # make a counter that starts with zero
        failed = 0             

        # for every character in secret_word    
        for char in word:      
            # see if the character is in the players guess
            if char in guesses:    
                # print out the character
                print(char,end='')    
            else:
                # if not found, print a dash
                print("_",end='')
       
                # and increase the failed counter with one
                failed += 1

        print()

        # print You Won if no failed guesses
        if failed == 0:        
            # exit the script
            return True              

        # how many turns are left
        print("You have", turns, "more guesses")

        invalid = True
        while invalid:
            # ask the user to guess a character
            guess = input("guess a character: ")
            if guess in guesses:
                print("You have already tried", guess)
                print("Try something else")
            else:
                invalid = False

        # add the players guess to guesses
        guesses += guess                    

        # if the guess is not found in the secret word
        if guess not in word:  
            # one less turn
            turns -= 1        
 
            # print wrong
            print("Wrong guess")
 
        # if not turns left
        if turns == 0:           
            return False

if __name__ == "__main__": # only if the main script
    main()
