my_string = "geeks for geeks"
old_substring = "k"
new_substring = "x"

split_list = my_string.split(old_substring)
print(split_list)
print(len(split_list)-1)
print(len(my_string))
new_list = [new_substring if i < len(split_list)-1 else '' for i in range(len(split_list)-1)]
print(new_list)
new_string = ''.join([split_list[i] + new_list[i] for i in range(len(split_list)-1)] + [split_list[-1]])

print(new_string)
