# -*- coding: utf-8 -*-
###############################################################################
## Copyright - 2022
## This work is licenced under Creative Commons Zero Universal
###############################################################################
## Author: Cesar Aracena
## Contributors:
###############################################################################

# Imports
import enum
import template_mod as mod
import template_mod_2 as mod_2

modules = {'template_mod': 'mod', 'template_mod_2': 'mod_2'}

# Put your work under this line and call it from inside main():
def index():
    groups = []
    menu = []
    welcome_msg = '#################################\n'
    welcome_msg += '# Welcome to The Common Project #\n'
    welcome_msg += '#################################\n'
    main_question = 'Please select an option from the list:\n'
    selection = None

    print(welcome_msg)
    print(main_question)

    for module, mod_name in modules.items():
        modx = globals()[mod_name].head()
        groups.append({'cat': modx['group'], 'name': modx['name'], 'desc': modx['description'], 'file': module})
        # menu.append(modx['group']) if modx['group'] not in groups else
        if modx['group'] not in menu:
            menu.append(modx['group'])

    # print(groups)
    
    for i, item in enumerate(menu):
        print(f'{i + 1} - {item}')

    selection = input('\nOption (any other option to exit): ')

    try:
        int(selection)
    except:
        exit()
    else:
        if int(selection) - 1 < len(menu):
            print(f'\n{menu[int(selection) - 1]}:\n')
            i = 1
            for mod in groups:
                if mod['cat'] == menu[int(selection) - 1]:
                    print(f'{i} - {mod["name"]}')
                    i += 1


# Main function to call all other methods
def main():
    # pass
    index()
    # print(mod.head())

# Check to only run the code in this file
# Do not edit under this line
if __name__ == '__main__':
    main()
