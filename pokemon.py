from random import randint
from time import sleep

items = {
    'POKEBALL': 2,
    'POTION': 3
}

pokemon_health = {
    'PIKACHU': 100,
    'CHARMANDER': 100
}

print 'Welcome to Pokemon battle 1.0!'
user_name = raw_input('Please enter your name: ')
print 'Welcome, %s!' % user_name
raw_input('Press Enter to continue... ')

print 'A wild charmander appears!'
sleep(2)
print '%s sent out...' % user_name
sleep(2)
print 'Pikachu! Go Pikachu! \"Pikachuuu!\"'
print 'Battle starting...'
raw_input('Press Enter to continue...')


def main_interface():
    print
    choice = raw_input('Fight, Pokemon, Item, Run: ').upper()
    if choice == 'POKEMON':
        print 'Pikachu\'s health is %d.' % pokemon_health['PIKACHU']
        raw_input('Press Enter to continue...')
        main_interface()
    elif choice == 'RUN':
        print 'You can\'t run from this battle.'
        raw_input('Press Enter to continue...')
        main_interface()
    elif choice == 'ITEM':
        item_choice = raw_input('Pokeball(%s), Potion(%s), Return: ' % (items['POKEBALL'], items['POTION'])).upper()
        if item_choice == 'RETURN':
            main_interface()
        elif item_choice == 'POTION':
            if pokemon_health['PIKACHU'] + 50 >= 100 and items['POTION'] > 0:
                pokemon_health['PIKACHU'] = 100
                items['POTION'] = items['POTION'] - 1
                main_interface()
            elif pokemon_health['PIKACHU'] + 50 < 100 and items['POTION'] > 0:
                pokemon_health['PIKACHU'] = pokemon_health['PIKACHU'] + 50
                items['POTION'] = items['POTION'] - 1
                main_interface()
            else:
                print 'You\'re out of potions!'
                main_interface()
        elif item_choice == 'POKEBALL':
            if items['POKEBALL'] > 0:
                print 'Don\'t be silly! I\'m taking your pokeballs away!'
                items['POKEBALL'] = 0
                main_interface()
            else:
                print 'You have no pokeballs!'
                main_interface()
        else:
            print 'Huh?'
            main_interface()
    elif choice == 'FIGHT':
        print 'Pikachu attacks!'
        damage = randint(15, 25)
        print 'Pikachu does %d damage!' % damage
        pokemon_health['CHARMANDER'] = pokemon_health['CHARMANDER'] - damage
        if pokemon_health['CHARMANDER'] <= 0:
            print 'You win!'
        else:
            sleep(2)
            print 'Charmander attacks!'
            damage = randint(15, 20)
            print 'Charmander does %d damage!' % damage
            pokemon_health['PIKACHU'] = pokemon_health['PIKACHU'] - damage
            if pokemon_health['PIKACHU'] <= 0:
                print 'You lose!'
            else:
                main_interface()
    else:
        print 'Huh? What was that?'
        main_interface()


main_interface()
