import os
from pprint import pprint
import json
import sys
# import pdb
# pdb.set_trace()


filename = os.getcwd() + '//' + 'themes_data.json'

themes_dict = {'mexican': {'carb': ['mexican rice'],
                           'meats': {'beef': ['beef tacos'],
                                     'chicken': ['chicken quesadilla'],
                                     'pork': ['carne adovada']},
                           'seafood': ['ceviche'],
                           'veg': ['veg fajitas']}}

program_running = True


def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_to_file(themes_dict, filename):
    with open(filename, 'w') as file:
        json.dump(themes_dict, file)


def theme_handler():
    global theme_name

    if theme_name != 'quit':
        if theme_name not in themes_dict:
            themes_dict[theme_name] = {'meats': {}}
            print(f"{theme_name} added")
            print('\n')
        else:
            print(f"{theme_name} exists")
            print('\n')
    else:

        save_to_file(themes_dict, filename)
        pprint(themes_dict, width=10)
        print('\n')
        print(f"Your dictionary has been saved in the current directory as {filename}.")
        print('\n')
        sys.exit()


def cat_handler():
    global cat_name
    global meat_check

    while meat_check not in ['yes', 'no']:
        print("INVALID CHOICE!")
        print('\n')
        meat_check = input("Is this a meat category? YES or NO? >>> ")
        print('\n')

    if meat_check == "yes":
        if cat_name not in themes_dict[theme_name]['meats']:
            themes_dict[theme_name]['meats'][cat_name] = []
            print(f"{cat_name} added")
            print('\n')
        else:
            print(f"{cat_name} exists")
            print('\n')
    if meat_check == 'no':
        while cat_name not in ['seafood', 'carb', 'dessert', 'breakfast', 'extras', 'veg']:
            print(f'{cat_name} is an INVALID CHOICE!')
            print('\n')
            cat_name = input("Enter the CATEGORY or MEAT >>> ").lower()
            print('\n')
        if cat_name not in themes_dict[theme_name]:
            themes_dict[theme_name][cat_name] = []
            print(f"{cat_name} added")
            print('\n')
        else:
            print(f'{cat_name} exists')
            print('\n')


def dish_handler():
    if meat_check == 'yes':
        if dish_name not in themes_dict[theme_name]['meats'][cat_name]:
            themes_dict[theme_name]['meats'][cat_name].append(dish_name)
            print(f"{dish_name} added")
            print('\n')
        else:
            print(f"{dish_name} exists")
            print('\n')
    if meat_check == 'no':
        if dish_name not in themes_dict[theme_name][cat_name]:
            themes_dict[theme_name][cat_name].append(dish_name)
            print(f"{dish_name} added")
            print('\n')
        else:
            print(f'{dish_name} exists')
            print('\n')


load_check = input('Do you want to load an existing database from an earlier session (YES / NO)? >>> ').lower()
print('\n')
if load_check == 'yes':
    themes_dict = load_from_file(filename)
    pprint(themes_dict, width=10)
    print('\n')
else:
    pass

while program_running:
    theme_name = input("Enter the THEME or type QUIT to exit >>> ").lower()
    print('\n')
    theme_handler()
    cat_name = input("Enter the CATEGORY or MEAT >>> ").lower()
    print('\n')
    meat_check = input("Is this a meat category? YES or NO? >>> ").lower()
    print('\n')
    cat_handler()
    dish_name = input("Enter the DISH name >>> ").lower()
    print('\n')
    dish_handler()
    pprint(themes_dict, width=10)
    print('\n')

#  todo don't show meat choice if a known category is entered
# todo backup to 2nd location
# todo test what happens if a non-letter or number is input
# can call it Whats for dinner or whats cookinyes
