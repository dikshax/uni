# 1. create three dictionaries:

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

# a. write code to concatenate these dictionaries to creat a new one. create a variable called nums to store the resulting dictionary. there are multiple ways to do this, however, one of the easiest is to convert each of the dictionaries items to a list (which can be added together) and pass them to the dic() constructor. 

nums = {**dic1, **dic2, **dic3}
# print(nums)


# b. write code to add a new key/value pair to the dictionary nums

nums.update({7:70})

# c. write code to update the value of he item with key 3 in nums to 80

nums.update({3:80})

# d. write code to remove the third item from dictionary nums.
del nums[3]

# e. write code to sum all the items in the dictionary nums.
total = 0
for x in nums.values():
    total += x

# f. write code to multiply all the items in the dictionary nums.

total = 1
for x in nums.values():
    total *= x

# g. write code to retrieve the maximum and minimum balues in nums.

maximum = 0
for x in nums.values():
    if x > maximum:
        maximum = x

minimum = nums[1]
for x in nums.values():
    if minimum > x:
        minimum = x

# print(maximum)
# print(minimum)

# 2. create two sets:
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

# a. write code to perform a union of these sets. print the length of the resulting set.

share = set1.union(set2)
length = len(share)

# print(share)
# print(length)

# b. write code to perform an intersection of set1 and set2.
in_both = set1.intersection(set2)
# print(in_both)

# c. write code to compute the summetric difference between set1 and set2.

sym_dif = set1.symmetric_difference(set2)
# print(sym_dif)

# d. write code to add the value 40 to set1, did the set change?

set1.add(40) # can not have duplicate values in sets
# print(set1)

# e. write code to remoce value 20 from set2.
set2.remove(20)
# print(set2)
