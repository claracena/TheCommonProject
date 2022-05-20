# -*- coding: utf-8 -*-
###############################################################################
## Copyright - 2022
## This work is licenced under Creative Commons Zero Universal
###############################################################################
## Author: Cesar Aracena
## Contributors:
###############################################################################

# Imports
# import enum
# import template_mod as mod
# import template_mod_2 as mod_2

# modules = {'template_mod': 'mod', 'template_mod_2': 'mod_2'}

# # Put your work under this line and call it from inside main():
# def index():
#     groups = []
#     menu = []
#     welcome_msg = '#################################\n'
#     welcome_msg += '# Welcome to The Common Project #\n'
#     welcome_msg += '#################################\n'
#     main_question = 'Please select an option from the list:\n'
#     selection = None

#     print(welcome_msg)
#     print(main_question)

#     for module, mod_name in modules.items():
#         modx = globals()[mod_name].head()
#         groups.append(
#             {'cat': modx['group'],
#             'name': modx['name'],
#             'desc': modx['description'],
#             'file': module}
#             )
#         # menu.append(modx['group']) if modx['group'] not in groups else
#         if modx['group'] not in menu:
#             menu.append(modx['group'])

#     # print(groups)
    
#     for i, item in enumerate(menu):
#         print(f'{i + 1} - {item}')

#     selection = input('\nOption (any other option to exit): ')

#     try:
#         int(selection)
#     except:
#         exit()
#     else:
#         if int(selection) - 1 < len(menu):
#             print(f'\n{menu[int(selection) - 1]}:\n')
#             i = 1
#             for mod in groups:
#                 if mod['cat'] == menu[int(selection) - 1]:
#                     print(f'{i} - {mod["name"]}')
#                     i += 1





# Manual imports
import importlib

# List of mods to import dynamically
modules = ['template_mod', 'template_mod_2', 'template_mod_3']

# Dynamic modules imports
for mod in modules:
    globals()[mod] = importlib.import_module('..' + mod, 'modules.subpkg')

# Menu parts generation class
class Menu:
    def __init__(self):
        self.modules = modules

    # Fill the categories list
    def main_categories(self):
        categories = []
        for mod in self.modules:
            if globals()[mod].head()['category'] not in categories:
                categories.append(globals()[mod].head()['category'])
        return categories
    
    # Select the modules for the selected category
    def modules_list(self, category):
        mod_list = []
        for mod in self.modules:
            if globals()[mod].head()['category'] == category:
                mod_list.append({'name': globals()[mod].head()['name'],
                    'description': globals()[mod].head()['description'],
                    'module': mod
                    })
        return mod_list
    
    def generate_menu(self, selection):
        if selection == [0, 0]:
            for category_number, category in enumerate(self.main_categories()):
                print(f'{category_number + 1} - {category}')

    # Launch the module main() app for the selected module
    def launch_module(self, module_name):
        return globals()[module_name].main()

# Main function to call all other methods
def main():
    menu = Menu()
    main_menu = menu.generate_menu([0, 0])

# Check to only run the code in this file
# Do not edit under this line
if __name__ == '__main__':
    main()
