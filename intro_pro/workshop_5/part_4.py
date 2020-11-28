# 1. create a program taht picks a winner for a contest or prize draw. The program should prompt for the names of the entrants and their contant details( address, mobile no ets ) until the user enters a black string. then select a winner at random and print their details. this is showcased in the demo program called coin_change included in last week's sample code.

import random 
def get_contest_info():
    first_name = input('please enter first name: ')
    family_name = input('please enter your second name: ')
    date_of_birth = int(input('please enter your date of birth: '))
    email = input('please enter your email: ')
    phone_number = int(input('please enter your phone number: '))
    return first_name, family_name, date_of_birth, email, phone_number



# b. add a text based menu to the program with two initial options:

    # add contentant or quit with the relevant functions.
# c. add menu option that aloows users to view the current list of contets.
# d. add a menu option that allows users to delete contestants.
