# 1. Write a Python function called add_daily_temp that is given a (possibly empty) dictionary meant to hold the average daily temperature for each day of the week, a temperature value, and the day of the week for the recorded temperature. The function should then add the temperature to the dictionary only if does not already contain a temperature for that day. The function should return the resulting dictionary, whether it is updated or not.


# daily_temp = {}
# def add_daily_temp(day, temp):
#     daily_temp.update({day: temp})
#     # for day in daily_temp:
#     #     if day in daily_temp.keys():
#     #         print('already there!')
#     #     else:
#     #         daily_temp.update({day:temp})
#     #         print('was\'nt in dic, added!')
    
#     return daily_temp

# one = add_daily_temp('Sunday', 121)
# print(daily_temp)


one = {'one':1, 'two':2, 'three':3}
two = [x, z for x, z in one.items()]
# keys = [x,z for x in one.keys() for z in one.values()]
# values = [x for x in one.values()]
# twon = keys + values
# print(twon)