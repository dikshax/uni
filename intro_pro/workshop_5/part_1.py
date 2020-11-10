# 1. giben the following list: nums = nums = [23, 16, 14, 33, 19, 6, 1]

# a. give the index values of all the odd numbers assuming zero-based indesxing.

nums = [23, 16, 14, 33, 19, 6, 1]
for x in nums:
    if x % 2 != 0:
        print(f'{x} is odd and its index is: {nums.index(x)}')
    else:
        print(f'{x} is not odd but is in the list')


#b. how many elements would be looked at when the list is traversed (from top to bottom) until the value 19 was found?

count = 0
for x in nums:
    if x != 19:
        print(x)
        count += 1
    elif x == 19:
        print('found the number 19')
        break
print(f'has to look at {count} elements to get to 19!')

# 2. which of the following lists are syntactically corrent in Python?
one = [1, 2, 3, 'four']
two = [1, 2, [3, 4]]
three = [[1, 2, 3], ['four']]

print(one)
print(two)
print(three)


# 3. what is the result of each of the following list opetations performed on the following list?
lst = [4, 2, 9, 1]
print(f'lst[] is :{lst[1]}')
lst.insert(2, 3)
print(lst)
del lst[3]
print(lst)
lst.append(3)

# 4. perform a series of list operations on the following list:

fruit = ['apple', 'banana', 'pear', 'cherry']
print(fruit)
del fruit[0]
del fruit[2]
fruit.insert(0, 'Grapefruit')
fruit.insert(2, 'Date')
fruit.append('orange')
print(fruit)


# 5. give the code to retrieve the maximum values of the second hald of the following tuples:


lst = [4, 21, 17, 7, 9, 1, 13, 45]
middle = len(lst) // 2
first_half = lst[:middle]
second_half = lst[middle:]

print(first_half)
print(second_half)

maximum = 0
for x in second_half:
    if x > maximum:
        maximum = x
print(maximum)


# 6. which of the follwoing are valid operations that could be used on the following tuples:
t1 = (1, 7, 9)
t2 = (5, 10, 8, 3)

print(len(t1))
print(t1 + t2)

# t1.append(t2)
#t1.insert(t2)


# 7. for str1 = 'Hello world', answer the following
# a. give an instruction that prints the fourth character of the string.

str1 = 'Hello World'
print(str1[3])

# b. give an instruction that finds the location of the first occurrence of 'o'
print(str1.find('o'))


