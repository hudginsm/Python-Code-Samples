'''
Guess the Number
author: Marcus Hudgins
version: Pyhton 3
'''
##import random

def startGame():
    #Set number equal to my number that the user has to guess
    number = 5 ##random.randint(1, 20)
##    print (number) #FOR TESTING

    #Asks player what thier name is and what their guess is
    PlayerName = input('Hello! What is your name? \n')
    print('Well, {0}, I am thinking of a number between 1 and 20.'.format(PlayerName))
    PlayerGuess = int(input('Take a guess. \n'))

    #Checks to see if players guess matches number
    if PlayerGuess == number:
        print('Good job, {0}! You guessed my number! \nYou Win!'.format(PlayerName))
    elif PlayerGuess > number:
        print('Your guess is too high. \nYou Lose.')
    elif PlayerGuess < number:
        print('Your guess is too low. \nYou Lose.')

if __name__ == '__main__':
    startGame()
