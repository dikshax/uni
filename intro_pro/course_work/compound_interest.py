# Coding Challenge 1
# Name: Mansoud Masnouri
# Student No: 1916829


# imported modules
import math   # using the python math module to round the answers


# A Simple and Compound Interest Calulator

def print_intro():
    ''' printing a welcome note, explain the purpose of the programm to the user'''
    print('''Welcome to the Wolving compound interest calculator.
This program calculates your potential returns when you invest with us.''')



def get_input():
    '''Asking the user for principal, rate and years.

    Returns:
        principal, rate and years
    '''
    principal = float(input('How much would you like to invest? '))
    rate = float(input('What is the intrest rate on your account? '))
    years = int(input('How logn are you planning to  invest (in years)? '))
    return principal, rate, years



def simple_interest(principal, rate, years):
    '''
    This function will calculate simple interest and return it.

    Keyword argumrnts:
        principal: the original value for the investment.
        rate: the rate of investment.
        years: how many years invested for?

    Return:
        The simple interest.
    '''
    end_amount_simp = principal*(1 + (rate/100) * years)
    return end_amount_simp


def compound_interest(principal, rate, years):
    '''
    This function will calcualte compount interest and return it.

    Keyword argumrnts:
        principal: the original value for the investment.
        rate: the rate of investment.
        years: how many years invested for?

    Returns:
        The compount interest.
    '''
    end_amount_comp = principal * (1 + (rate/100) / 4) ** (4 * years)
    return end_amount_comp


def print_simple_output(principal, rate, years, result):
    '''
    Returning a formatted stirng.

    Parameters:
        principal: the original value for the investment.
        rate: the rate of investment.
        years: how many years invested for?
        result: the result from simple_interest()

    Returns:
        uses f-string to format the output nicely.
    '''
    return f'£{principal} invested at {rate}% for {years} years is: £{round(result, 2)}'


def print_compounding_output(principal, rate, years, result):
    '''
    Returning a formatted stirng.

    Parameters:
        principal: the original value for the investment.
        rate: the rate of investment.
        years: how many years invested for?
        result: the result from compound_interest()

    Returns:
        uses f-string to format the output nicely.
    '''
    return f'£{principal} invested at {rate}% for {years} years compounded 4 times per year is: £{round(result, 2)}'


# ---------- Challenge Functions (Optional) ----------

def get_target_input():
    '''
    Asking the user for principal, rate and goal.

    Returns:
        principal, value, rate, goal.
    '''
    principal = float(input('What is the principal amount? '))
    rate = float(input('What is the rate? '))
    goal = float(input('What is your savings goal? '))
    return principal, rate, goal



def calculate_years_to_target(principal, rate, target):
    '''this function will calculate the numbers of years to reach your goal'''
    years = (target - principal) / (principal * (rate/100))
    return math.floor(years)


def print_target_output(principal, rate, years):
    '''This function will just display its passed in arguments in a readable way.'''
    return f'£{principal} invested at {rate}% will allow you to reach your goal in {years} years.'


# ---------- Main driver function ----------
# 1.	Print a welcome message explaining the purpose of the program.
# 2.	Prompt the user for the necessary inputs (see formulae and brief) and convert the values the user enters into suitable data types.
# 3.	Perform the simple and compound interest calculations.
# 4.	Print the results to the terminal in the format specified.
def main():
    print_intro()

    answer = int(input('''Would you like to:
        1. Calculate simple and compoint interest over time
        2. Calculate the amount of time required to hit a savings goal.
        '''))

    if answer == 1:

        principal, rate, years = get_input()

        end_amount_simp = simple_interest(principal, rate, years)

        end_amount_comp = compound_interest(principal, rate, years)

        simple_int_result = print_simple_output(principal, rate, years, end_amount_simp)
        print(simple_int_result)

        compound_int_result = print_compounding_output(principal, rate, years, end_amount_comp)
        print(compound_int_result)

    elif answer == 2:
        principal, rate, target = get_target_input()
        years = calculate_years_to_target(principal, rate, target)

        massage = print_target_output(principal, rate, years)
        print(massage)

    else:
        print('something went wrong please check your inputs!!')


# Program execution begins here
if __name__ == '__main__':
    main()
