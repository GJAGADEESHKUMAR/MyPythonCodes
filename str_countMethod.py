#1)Python count method
str = "JagguJagadeesh"
#using string count() method
char_count = str.count('g')
#printing the result
print(char_count)
print(str.count('Ja'))

#we can count the number of occurances of a character in a string
strings = ["Red", "Green", "orange"]
char_to_count = 'e'
total_count = sum(string.count(char_to_count) for string in strings)
print(total_count)

import re
my_string = "Good Morning and Morning is Great."
substring = "Morning"
substring_count = len(re.findall(substring, my_string))
print(substring_count)

# string in which occurrence will be checked
string = "jagadeesh kumar patel jaggu"
print(string.count("jaggu", 0, 5))
print(string.count("jaggu", 0, len(string)))



