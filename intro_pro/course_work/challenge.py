import math

def get_target_input():
    print('''Would you like to:
        1. Calculate simple and compoint interest over time
        2. Calculate the amount of time required to hit a savings goal.
        ''')
    answer = int(input('> '))
    principal = float(input('What is the principal amount? '))
    rate = float(input('What is the rate? '))
    target = float(input('What is your savings goal? '))


    return principal, rate, target, answer


def calculate_years_to_target(principal, rate, target):
    years = (target - principal) / (principal * (rate/100))

    return math.floor(years)


def print_target_output(principal, rate, years):
    return f'£{principal} invested at {rate}% will allow you to reach your goal in {years} years.'



def main():
    principal, rate, target, answer = get_target_input()
    print(principal, rate, target, answer)

    years = calculate_years_to_target(principal, rate, target)

    massage = print_target_output(principal, rate, years)
    print(massage)

if __name__ == '__main__':
    main()
