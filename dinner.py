style = ['seafood', 'island', 'asian', 'spanish', 'southern']

food_preference = ['light', 'heavy']

seafood_choices = [[['sushi', 21], ['chowder', 15]], [['paella', 32], ['mixed grill', 28]]]
island_choices = [[['mofungo', 8], ['beef patty', 10]], [['roast pork', 19], ['goat curry', 22]]]
asian_choices = [[['egg rolls', 9], ['shrimp toast', 12]], [['pu pu platter', 15], ['general tso', 25]]]
spanish_choices = [[['nachos', 9], ['taquitos', 11]], [['fried fish', 17], ['mole', 20]]]
southern_choices = [[['pimento cheese', 11], ['gumbo', 9]], [['fried chicken', 20], ['brisket', 40]]]

desserts = [['pecan pie', 10], ['flan', 11], ['gelato', 9]]

def get_style_choice():
    print(style)

    chosen_style = input('What style?')

    while chosen_style not in style:
            print('Must pick a style listed')
            chosen_style = input('What style?')

    return chosen_style

def get_pref_choice():
    print(food_preference)

    chosen_pref = (input('light or heavy?'))

    while chosen_pref not in food_preference:
            print('Must pick light or heavy')
            chosen_pref = input('light or heavy?')

    return int(chosen_pref)

def get_food_recs():
    style_choice = get_style_choice()
    pref_choice = get_pref_choice()
    choices = []

    while style_choice and pref_choice:
        if style_choice == 'seafood':
            choices.append(seafood_choices[pref_choice])
        elif style_choice == 'island':
            choices.append(island_choices[pref_choice])
        elif style_choice == 'asin':
            choices.append(asian_choices[pref_choice])
        elif style_choice == 'spanish':
            choices.append(spanish_choices[pref_choice])
        elif style_choice == 'southern':
            choices.append(southern_choices[pref_choice])

    return choices

def pick_dessert():
    for dessert in desserts:
        print('We have: ', dessert[0])
        
    choice = input('Pick 1, 2, or 3!')

    while choice not in ['1', '2', '3']:
        print('Please pick 1, 2, or 3')
        choice = input('Pick 1, 2, or 3!')

    return choice[int(choice) - 1]
    


def pick_dinner():
    choices = get_food_recs()
    
    print(choices)

    choice = input('Pick a dinner! 1 or 2?')

    while choice not in ['1', '2']:
        print('Please pick 1 or 2.')
        choice = input('Pick a dinner! 1 or 2? ')

    return choices[int(choice) - 1]