from random import randint

list1 = [randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20),
         randint(1, 20), randint(1, 20), randint(1, 20)]

list2 = []

list3 = []

list1.sort()

for less_than_five in list1:
    if less_than_five < 5:
        list2.append(less_than_five)

user_number = int(raw_input('Please give me a number: '))

for less_than_x in list1:
    if less_than_x < user_number:
        list3.append(less_than_x)

print 'List 1'
print list1
print
print 'Numbers less than 5 in list 1'
print list2
print
print 'Numbers less than %d in list 1' % user_number
print list3
