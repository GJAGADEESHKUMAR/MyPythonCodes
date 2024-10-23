text = "Hello Geeks and welcome to Geeksforgeeks"
substring_list = ["Geeks", "welcome", "notfound"] 

indices = [text.index(sub) if sub in text else -1 for sub in substring_list] 
print(indices) 

#using tuple handling ValueError of index() method
text = "Hello Geeks! and welcome to Geeksforgeeks"
substring_tuple = ("Geeks", "to", "!", "notfound") 

for sub in substring_tuple: 
	try: 
		index = text.index(sub) 
		print(f"Index of '{sub}': {index}") 
	except ValueError as e: 
		print(f"Substring '{sub}' not found!") 

# initializing target strings 
VOLTAGES = ["001101 AC", "0011100 DC", "0011100 AC", "001 DC"]
# initializing argument string 
TYPE = "AC"
# initializing bit-length calculator 
SUM_BITS = 0
for i in VOLTAGES: 
	ch = i 
	if ch[len(ch) - 2] != "D": 
		# extracts the length of bits in string 
		bit_len = ch.index(TYPE) - 1
		# adds to total 
		SUM_BITS = SUM_BITS + bit_len 
print("The total bit length of AC is : ", SUM_BITS) 
