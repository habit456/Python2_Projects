
# Determines if number is even or odd and then if it's divisible by 4.


def odd_or_even(number):
    if number % 2 == 0:
        print 'Your number is even.'
        if number % 4 == 0:
            print 'Your number is also a multiple of 4.'
    else:
        print 'Your number is odd.'


odd_or_even(int(raw_input('Please enter a number: ')))

# Extra 2

num1 = int(raw_input('Please give me a number: '))
check1 = int(raw_input('Please give me another number: '))


def divide2(check, num):
    if num % check == 0:
        print '%d divides evenly into %d.' % (check, num)


divide2(check1, num1)
