# 1. Write a Python function called add_daily_temp that is given a (possibly empty) dictionary meant to hold the average daily temperature for each day of the week, a temperature value, and the day of the week for the recorded temperature. The function should then add the temperature to the dictionary only if does not already contain a temperature for that day. The function should return the resulting dictionary, whether it is updated or not.



def add_daily_temp(day, temp):
    daily_temp = {'monday': 21}
    if day in daily_temp:
        print(f'already in record, {day}: {daily_temp.get(day)}')
    else:
        daily_temp[day] = temp
    return daily_temp

# one = add_daily_temp('Friday', 23)
# print(one)

# 2. Write a Python function named moderate_days that is given a dictionary containing the average daily temperature for each of the days of a week and returns a list of the days in which the average was between 70 and 79 degrees.

def moderate_days():
    D = {'monday': 121, 'tuesday': 98, 'wednesday':90, 'thursday':65, 'friday':91, 'sturday':80, 'sunday': 72}
    days = [x for x in D if  D.get(x) >= 70 and D.get(x) <= 90]
    return days

# one = moderate_days()
# print(one)

# 3. Write a Python function named get_daily_temps that prompts the user for the average temperature for each day of the week and returns a dictionary containing the information the user entered.

def get_daily_temps():
    dict_week = dict()
    days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    for x in days_of_week:
        temp = int(input(f'Please enter the temp for {x}: '))
        dict_week[x] = temp
    return dict_week

# one = get_daily_temps()
# print(one)


# 4. Write a Python function named get_weekend_average_temp that is passed a dictionary of daily temperatures and returns the average temperature over the weekend for the weekly temperatures given.


not_weekend = {'monday': 17, 'tuesday': 17, 'wednesday': 14, 'thursday': 13, 'friday': 14}
def get_weekend_average_temp(days):
    total = 0
    for x in days:
        total += days.get(x) 
    average = total / len(days)
    return f'the average temp for the weekend is : {round(average, 2)}'

# one = get_weekend_average_temp(not_weekend)
# print(one)


# 5. Write a Python function named add_vegetable that is passed a (possible empty) set of vegetable names and raises a ValueError exception if the given vegetable is already in the set, otherwise, add the vegetable and return a new set.

def add_vegetable(veg):
    set_veg = {'ornage', 'banana', 'kiwi'}
    if veg in set_veg:
        raise Exception (f'{veg} is in the set already!')
    else:
        set_veg.add(veg)
    return set_veg

# one = add_vegetable('grapes')
# print(one)

# 6. Write a Python function named num_vowels_consonants that is passed a string containing letters, each of which may be in either upper or lower case and returns how many vowels and consonants the string contains.

def num_vowels_consonants(something):
    num_vowels = 0
    num_consonants = 0 
    vowels = ['a', 'e', 'i', 'o', 'u']

    for x in something.lower():
        if x in vowels:
            num_vowels += 1
        else:
            num_consonants += 1
    return (f'there is {num_vowels} vowels and {num_consonants} consonants in {something}')


# one = num_vowels_consonants('mAnsoud MANsouri')
# print(one)



