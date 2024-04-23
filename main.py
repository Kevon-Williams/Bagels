import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print('''Bagels, a deductive logic game.
          I am thinking of a {} digit number with no repeated digits.
          Try to guess what it is. Here are some clues:
          When I say:       That means:
            Pico                One digit is correct but in the wrong position.
            Fermi               One digit is correct and in the right position. 
            Bagels              No digit is correct.'''.format(NUM_DIGITS))

    while True:
        secret_num = get_secret_num()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal(): #Validates guess for correct length and type
                print('Guess #{}: '.format(numGuesses))              #if not 3 digits or not a decimal(0-9), loop gets entered       
                guess = input('> ')                                  #loops until user's guess is valid

            clues = get_clues(guess,secret_num)
            print(clues)
            numGuesses += 1 #increment loop controller

            #Break out of the loop if they're correct
            if guess == secret_num:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.' .format(secret_num))
            
            #Ask a player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'): #converts input to lower case, and breaks if it does not start with y
                break
    print('Thanks for playing!')


def get_secret_num():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS): #loops NUM_DIGITS (3) times
        secret_num += str(numbers[i])
    return secret_num
    
def get_clues(guess, secret_num):
     #Returns a string with the pico, fermi, bagels clues for a guess
    #and secret number pair.

    if guess == secret_num:
        return 'You got it!' #ignore this comment
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]: #checks the corresponding guess digit to secret num digit
             clues.append('Fermi') # A correct digit is in the correct place.
        elif guess[i] in secret_num:
            clues.append('Pico') # A correct digit is in the incorrect place.
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits at all.
    else:
        # Sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        return ' '.join(clues)


if __name__ == '__main__':
    main()