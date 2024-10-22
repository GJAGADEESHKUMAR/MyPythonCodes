#Python program to update any string
str='Python Programming'
print(str)

#updation by converting into the list
list1=list(str)
list1[2]='p'
str="".join(list1)
print(str,"\t (Note here t is changed to p)")

#updation by using the string slicing
str=str[0:2]+'m'+str[3:]
print(str,"\t (Note here t is changed to m)")

str="This is new string with the same name"
print(str)
