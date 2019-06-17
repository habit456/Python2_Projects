# This program is designed to roll a pair of dice and asks the user
# to guess the sum.

from random import randint
from time import sleep

# Prompts user for a guess

def get_user_guess():
  guess = int(raw_input('Please guess the sum of the 2 dice: '))
  return guess

# Simulates the rolling of a pair of dice

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print
  print 'The maximum sum value of the 2 dice is %d.' % max_val
  print
  guess = get_user_guess()
  if guess > max_val or guess < 2:
    print 'Invalid guess.'
  else:
    print
    print 'Rolling...'
    print
    sleep(2)
    print '%d' % first_roll
    print
    sleep(1)
    print '%d' % second_roll
    print
    sleep(1)
    total_roll = first_roll + second_roll
    print 'Total: %d' % total_roll
    print
    print 'Result...'
    print
    sleep(1)
    if guess == total_roll:
      print 'Congratulations! Your guess was correct!'
    else:
      print 'Sorry! Try again!'


print
print 'Welcome to Dice Guess 1.0!'
print
roll_dice(int(raw_input('How many sides will each die have? ')))
print
print 'Thank you for playing Dice Guess 1.0!'