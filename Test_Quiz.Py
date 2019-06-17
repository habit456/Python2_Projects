score = 100

print 'Hello. Welcome to my test!'

name = raw_input('What is your name? ')

answer1 = raw_input('What is 2+2? ')
if answer1 == '4':
    score += 0
else:
    score -= 25

answer2 = raw_input('What is 3 x 10? ')
if answer2 == '30':
    score += 0
else:
    score -= 25

answer3 = raw_input('What is 10/10? ')
if answer3 == '1':
    score += 0
else:
    score -= 25

answer4 = raw_input('Is Joshua Kaplan the sexiest man alive? Y/N. ')
if answer4 == 'Y' or answer4 == 'y':
    score += 0
else:
    score -= 25

print 'You scored %s.' % score

if score == 100:
    print 'Good job, %s!' % name
else:
    print 'Better luck next time, %s!' % name
