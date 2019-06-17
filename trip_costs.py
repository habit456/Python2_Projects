def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburgh':
        return 222
    elif city == 'Los Angeles':
        return 475


def rental_car_cost(days):
    total_cost = days * 40
    if days >= 7:
        total_cost -= 50
    elif days >= 3 and days < 7:
        total_cost -= 20
    return total_cost


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money


# Gathering data

print
print 'Hello and welcome to Trip Cost Calculator 1.0!'
print
city = raw_input('What city do you plan on visiting? Your options are \nCharlotte, Tampa, Pittsburgh,'
                  ' and Los Angeles: ')
days = raw_input('How many days do you plan on spending there? ')
spending_money = raw_input('How much extra money do you plan on spending? ')

# Giving data back

print
print 'Your Results'
print 'Rental Car Costs: %d' % (rental_car_cost(int(days)))
print 'Hotel Costs: %d' % (hotel_cost(int(days) - 1))
print 'Plane Costs: %d' % (plane_ride_cost(city))
print 'Total Trip Cost: %d' % (trip_cost(city, int(days), int(spending_money)))

# Goodbye

print
print 'Thank you for using Trip Cost Calculator 1.0!'