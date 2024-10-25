def count_ones(n):
    return bin(n).count('1')
n=int(input("Enter any number:"))
print("Number of ones in the given number is:",count_ones(n))
