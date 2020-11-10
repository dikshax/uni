# 1. write a python program that prompts the user for a series of integers and stores in a list only the values between 1-100, and dislays the resulting list.

def numbers(*agrs):

    lst_number = []
    for x in agrs:
        intro = print('please enter number or numbers: ')
        lst_number += x
    return lst_number

one = numbers()
print(one)
