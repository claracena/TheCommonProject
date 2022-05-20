# -*- coding: utf-8 -*-
###############################################################################
## Copyright - 2022
## This work is licenced under Creative Commons Zero Universal
###############################################################################
## Author: Cesar Aracena
## Contributors:
###############################################################################

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
