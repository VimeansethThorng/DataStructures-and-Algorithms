list = ["a", "caaa", "exxx", "daaa"]

# sort in place
temp_list = list
temp_list.sort()    # ascending
# temp_list.sort(reverse=True) # descending
print(temp_list)

# sort and output as a new list
new_list = sorted(list)
new_reverse_list = sorted(list, reverse=True)
print(new_list)
print(new_reverse_list)


