###############################################################################
## Copyright - 2022
## This work is licenced under Creative Commons Zero Universal
###############################################################################
## Author: Cesar Aracena
## Contributors:
###############################################################################
# -*- coding: utf-8 -*-

# Imports


# Put your work under this line and call it from inside main():
def index():
    welcome_msg = '#################################\n'
    welcome_msg += '# Welcome to The Common Project #\n'
    welcome_msg += '#################################\n'
    main_question = 'Please select an option from the list:\n'
    options = ['First option',
                'Second option',
                'Tercer option'
                ]
    selection = None

    print(welcome_msg)
    print(main_question)

    while selection == None:
        for i, option in enumerate(options):
            print(f'{i} - {option}')
        print()
        print(int(input('Option: ')))

# Main function to call all other methods
def main():
    index()

# Check to only run the code in this file
# Do not edit under this line
if __name__ == '__main__':
    main()
