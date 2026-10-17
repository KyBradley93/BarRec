liquor = ['vodka', 'rum', 'gin', 'tequila', 'whiskey']

drink_preference = ['sweet', 'strong']

vodka_drinks = [[['lemon drop martini', 14], ['espresso martini', 16]], [['dirty martini', 14], ['cosmo', 15]]]
rum_drinks = [[['pina colada', 10], ['mai tai', 10]], [['rum runner', 11], ['cuba libre', 9]]]
gin_drinks = [[['lavender fizz', 11], ['french 75', 13]], [['gimlet', 10], ['gin hugo', 13]]]
tequila_drinks = [[['strawberry marg', 10], ['tequila sunrise', 14]], [['margarita', 10], ['carrajillo', 14]]]
whiskey_drinks = [[['mint julip', 11], ['whiskey sour', 12]], [['old fashion', 15], ['manhatten', 15]]]


def get_liquor_choice():
    print(liquor)

    chosen_liquor = input('What liquor?')

    while chosen_liquor not in liquor:
            print('Must pick a liquor listed')
            chosen_liquor = input('What liquor?')

    return chosen_liquor

def get_pref_choice():
    print(drink_preference)

    drink_index = []

    chosen_pref = (input('sweet or strong?'))

    while chosen_pref not in drink_preference:
            print('Must pick sweet or strong')
            chosen_pref = input('sweet or strong?')

    if chosen_pref == 'sweet':
         drink_index.append(0)
    
    if chosen_pref == 'strong':
         drink_index.append(1)

    return drink_index

def get_drink_recs():
    liquor_choice = get_liquor_choice()
    pref_choice = get_pref_choice()
    choices = []


    pref = int(pref_choice[0])

    if liquor_choice == 'vodka':
        choices = vodka_drinks[pref]
    elif liquor_choice == 'rum':
        choices = rum_drinks[pref]
    elif liquor_choice == 'gin':
        choices = gin_drinks[pref]
    elif liquor_choice == 'tequila':
        choices = tequila_drinks[pref]
    elif liquor_choice == 'whiskey':
        choices = whiskey_drinks[pref]

    return choices


def pick_drink():
    choices = get_drink_recs()
    
    print(choices)

    choice = input('Pick a drink! 1 or 2?')

    while choice not in ['1', '2']:
        print('Please pick 1 or 2.')
        choice = input('Pick a drink! 1 or 2? ')

    return choices[int(choice) - 1]


    

    
    
    












