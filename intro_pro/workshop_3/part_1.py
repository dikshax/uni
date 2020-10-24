def avg(num1, num2, num3):
    return (num1 + num2 + num3) / 3.0

num1 = 37
num2 = 108
num3 = 67

# result = avg(num1, num2)  // missing 1 required positional argument

avg(num1, num2, num3)  # this is ok and will work

# result = avg(num1, num2, num3, num4, num5, num6) #this not gonna work, num4-num6 is not defined and excess of positional argument


print(avg(num1, num2, num3)) # this is one is working too

# result = avg(num1, num2, avg(num3, num4, num5)) # not gonna work, num4 and num5 is not defined.


result = avg(num1, num2, avg(num1, num2, num3))

print(result)

