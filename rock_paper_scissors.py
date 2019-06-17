# This program plays rock, paper, scissors with the user

from random import randint
from time import sleep

options = ['ROCK', 'PAPER', 'SCISSORS']

message = {'tie': 'Yawn, it\'s a tie!',
           'won': 'Yay you won!',
           'lost': 'Aww you lost!'}


def decide_winner(user_choice, computer_choice):
    print
    print 'You have selected %s!' % user_choice
    sleep(1)
    print 'The computer has selected...'
    sleep(2)
    print computer_choice + '!'
    sleep(1)
    print
    if user_choice == computer_choice:
        print message['tie']
        print
        play_again(raw_input('Would you like to play again? ').upper())
    elif user_choice == options[0] and computer_choice == options[2]:
        print message['won']
        print
        play_again(raw_input('Would you like to play again? ').upper())
    elif user_choice == options[1] and computer_choice == options[0]:
        print message['won']
        print
        play_again(raw_input('Would you like to play again? ').upper())
    elif user_choice == options[2] and computer_choice == options[1]:
        print message['won']
        print
        play_again(raw_input('Would you like to play again? ').upper())
    else:
        print message['lost']
        print
        play_again(raw_input('Would you like to play again? ').upper())


def play_RPS():
    print
    user_choice = raw_input('Please enter Rock, Paper, or Scissors: ').upper()
    if user_choice == options[0]\
            or user_choice == options[1]\
            or user_choice == options[2]:
        computer_choice = options[randint(0, 2)]
        decide_winner(user_choice, computer_choice)
    else:
        print
        print 'Invalid selection!'
        print
        play_again(raw_input('Would you like to play again? ').upper())


def play_again(y_n):
    if y_n == 'YES':
        play_RPS()
    else:
        print
        print 'Thanks for playing!'


print
print 'Welcome to Rock, Paper, Scissors 1.0!'
sleep(1)
play_RPS()
