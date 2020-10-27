nums = [23, 16, 14, 33, 19, 6, 1]

#(a) Give the index values of all the odd numbers assuming zero-based indexing

i = 0
while i < len(nums):
    if nums[i] % 2 == 1:
        print(i, nums[i])
    i += 1

one = range(1, 12)
print(one)
