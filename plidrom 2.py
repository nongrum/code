string = input("Please enter a Text : ")
str = ""

for i in string:
    str = i + str  
# print("Reverse Order :  ", str)
if(string == str):
   print("This is a Palindrome String")
else:
   print("This is Not")