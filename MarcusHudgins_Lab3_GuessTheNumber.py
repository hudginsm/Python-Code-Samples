'''
Guess the Number v.2
author: Marcus Hudgins
version: Pyhton 3
'''
##import random

def startGame():
    #Set number equal to my number that the user has to guess
    number = 5 ##random.randint(1, 20)
    PlayerGuess = 0
##    print (number) #FOR TESTING

    #Asks player what thier name is and what their guess is
    PlayerName = input('Hello! What is your name? \n')
    print('Well, {0}, I am thinking of a number between 1 and 20.'.format(PlayerName))
    PlayerGuess = int(input('Take a guess. \n'))

    #Checks to see if players guess matches number

    while PlayerGuess != number:
        if PlayerGuess < number:
            print('Your guess is too low.')
        elif PlayerGuess > number:
            print('Your guess is too high.')
        PlayerGuess = int(input('Guess again.\n'))
        
    if PlayerGuess == number:
        print('Good job, {0}! You guessed my number! \nYou Win!'.format(PlayerName))

if __name__ == '__main__':
    startGame()
