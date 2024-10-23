#Python string formatting
str = "{} {} {}".format('Believe', 'in', 'Your power')
print(str)
# Positional Formatting
str = "{1} {0} {2}".format('Believe', 'in', 'Your Power')
print(str)
# Keyword Formatting
str = "{l} {f} {g}".format(g='Believe', f='in', l='Your Power')
print(str)

# Formatting of Integers
str1= "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(str1)
str1="{0:o}".format(16)
print("\nOctal representation of 16 is ")
print(str1)

# Formatting of Floats
str1 = "{0:e}".format(16535.6458)
print("\nExponent representation of 165.6458 is ")
print(str1)

# Rounding off Integers
str1 = "{0:.4f}".format(5/9)
print("\none-sixth is : ")
print(str1)

str2 = "|{:<10}|{:^10}|{:>10}|".format('Vinay','Kumar','Patel')
print(str2)
