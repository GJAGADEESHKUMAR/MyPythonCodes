expr1 = "4²"
print("expr isdigit(4²)?", expr1.isdigit()) # yes contains only digits

print("expr isdecimal(4²)?", expr1.isdecimal()) # not a pure decimal

print("expr isnumeric(4²)?", expr1.isnumeric()) # sorts of evaluates

expr2 = "⅔"
print("expr isdigit(⅔)?", expr2.isdigit()) #also / is not a digit
print("expr isnumeric(⅔)?", expr2.isnumeric()) # but it evaluates

print("expr isdecimal(⅔)?", expr2.isdecimal()) # only decimal numbers?not
