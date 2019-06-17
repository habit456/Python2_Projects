from datetime import datetime

year = (datetime.now()).year
num_ask = 'Please give me a number:'

name = raw_input('What\'s your name? ')

def calculation(age):
    total_age = 100 - age + year
    print 'You will be 100 in %d, %s.' % (total_age, name)


calculation(int(raw_input('How old are you? ')))

num_x = int(raw_input(num_ask))

print num_x * (num_ask + '\n')

