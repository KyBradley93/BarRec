import drinks
import dinner

drink = []
meal = []
dessert = []

def order():
    print("Starting drink")
    dr = drinks.pick_drink()

    print("Finished drink")
    print("Starting dinner")
    me = dinner.pick_dinner()

    print("Finished dinner")
    print("Starting dessert")
    de = dinner.pick_dessert()

    print("Finished dessert")

    drink.append(dr)
    meal.append(me)
    dessert.append(de)

    print("Starting total")
    get_total()

    print("Starting restart")
    restart()
    
def get_total():
    total = drink[0][1] + meal[0][1] + dessert[0][1]

    print('Bill tonight: ', total)

    tip = input('What % would you like to tip? 10, 20, 30, 40, or 50')

    while tip not in ['10', '20', '30', '40', '50']:
        print('Must pick asshole')
        tip = input('What % would you like to tip? 10, 20, 30, 40, or 50')

    tip = int(tip)

    tip_amount = total * (tip / 100)

    final_total = total + tip_amount

    print('Total tonight: ', final_total)

def restart():
    restart = input('Would you like another round? Y or N')

    while restart not in ['Y', 'N']:
        print('Type Y or N')
        restart = input('Would you like another round? Y or N')

    if restart == 'Y':
        order()
    else:
        print('Bye')


order()

