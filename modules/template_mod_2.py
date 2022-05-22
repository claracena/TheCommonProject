# -*- coding: utf-8 -*-
###############################################################################
## Copyright - 2022
## This work is licenced under Creative Commons Zero Universal
###############################################################################
## Author: 
## Contributors:
###############################################################################

# Imports


# This function defines the basic information about this module.
def head():
    # Write the group this module belongs to
    # If it doesn't belong in any group, write 'root'
    category = 'Quiz'
    # Put the name for the option to appear in the main menu
    name = 'Quiz 1'
    # Write a quick description of this module
    description = 'This is a test feature/module'

    return {'category': category, 'name': name, 'description': description}

# Put your work under this line and call it from inside main():


# Main function to call all other methods
def main():
    print('This is the main() app of Quiz 1')

# Check to only run the code in this file
# Do not edit under this line
if __name__ == '__main__':
    main()
