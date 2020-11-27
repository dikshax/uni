# 1. Write a Python function called add_daily_temp that is given a (possibly empty) dictionary meant to hold the average daily temperature for each day of the week, a temperature value, and the day of the week for the recorded temperature. The function should then add the temperature to the dictionary only if does not already contain a temperature for that day. The function should return the resulting dictionary, whether it is updated or not.

def add_daily_temp(day, temp):
    daily_temp = {}

    for day, temp in daily_temp.items():
        if day, temp in daily_temp.items():
            print('already there!')
        else:
            daily_temp.update({day:temp})
    
    return daily_temp

one = add_daily_temp('Thursday', 12)
print(one)