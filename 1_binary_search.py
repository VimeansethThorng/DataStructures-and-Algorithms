from bisect import bisect_left  


a_list = [3, 4, 5, 6, 7]
target = 5

target_index = bisect_left(a_list, target)
print(target_index)
