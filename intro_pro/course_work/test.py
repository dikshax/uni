def print_intro():
    return ('''
Welcome to the Wolving compound interest calculator.
This program calculates your potential returns whenn you invest with us.
        ''')



def get_input():
    principal = float(input('How much would you like to invest? '))
    rate = float(input('What is the intrest rate on your account? '))
    years = int(input('How logn are you planning to  invest (in years)? '))
    return principal, rate, years



def simple_interest(principal, rate, years):
    end_amount_simp = principal*(1 + (rate/100) * years)
    return end_amount_simp


def compound_interest(principal, rate, years):
    end_amount_comp = principal * (1 + (rate/100) / 4) ** (4 * years)
    return end_amount_comp


def print_simple_output(principal, rate, years, result):
    return f'£{principal} invested at {rate}% for {years} years is: £{round(result, 2)}'


def print_compounding_output(principal, rate, years, result):
    return f'£{principal} invested at {rate}% for {years} years compounded 4 times per year is: £{round(result, 2)}'




def main():
    print(print_intro())

    principal, rate, years = get_input()

    end_amount_simp = simple_interest(principal, rate, years)

    end_amount_comp = compound_interest(principal, rate, years)

    simple_int_result = print_simple_output(principal, rate, years, end_amount_simp)
    print(simple_int_result)

    compound_int_result = print_compounding_output(principal, rate, years, end_amount_comp)
    print(compound_int_result)

if __name__ == '__main__':
    main()

