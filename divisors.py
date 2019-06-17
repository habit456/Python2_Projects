x = [0]
divisor_list = []

user_num = int(raw_input('Please give me a number: '))

for num in x:
    num = num + 1
    x.append(num)
    if user_num % num == 0:
        divisor_list.append(num)
        if user_num / num == 1:
            break

print
print 'List of divisors for %d' % user_num
print divisor_list
