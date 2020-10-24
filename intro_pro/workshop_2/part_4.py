# the train gonna be late 13445 seconds
# there is 60 minutes in an hour
# there is 3600 seconds in an hour
# there is 60 second in a minute

#  storing the seconds to wait in a veriable
seconds_to_wait = 13445

#  dividing the seconds by 3600 to get the hours
# re-assign the veriable to the remainder of the division

hours = seconds_to_wait // 3600
remainder = seconds_to_wait % 3600

# dividing the seconds by 60 to get the minutes
# re-assign the veriable to remainder of the division

minutes = remainder // 60
remainder %= 60

# the remainder will be the seconds left over
seconds = remainder

# using the f-string to layout the output in a nicer format
print(f'{seconds_to_wait} Seconds is: {hours} Hours, {minutes} Minutes, {seconds} Seconds')
