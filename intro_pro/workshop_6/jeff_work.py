dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}


nums = [*dic1.items(), *dic2.items(), *dic3.items()]
print(nums)
