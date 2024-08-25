#Python :-


#simple way to print python 
print("hello dina ")

x = "Python is awesome"
print(x)
#----------------------------------------------------------
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#----------------------------------------------------------

x = 5                 # x is of type int
X = "John"              # Xis now of type str
print(x)   
print(X)
#Because python is case sensitive 
#Comment-used to make the code more readable.
#This is a comment
print("Hello, World!")

# 2 Variables- Variables are containers for storing data values.
#A variable is created the moment you first assign a value to it.
#A variable name must start with a letter or the underscore character
#A variable name cannot start with a number
#A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#Variable names are case-sensitive (age, Age and AGE are three different variables)
#A variable name cannot be any of the Python keywords.
myvar = "John"
my_var = "John"
_my__var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 

#Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# 3. Data Types:Variables can store data of different types, and different types can do different things.
x = 5 #(integer)
y = 3.14 #(float)
name = "John" #(string)
isAdmin = True #(boolean)
fruits = ["apple", "banana", "cherry"] #(list)
z = 1j+3   #complex 

#Check Data Type:
print(type(x))
print(type(y))

#4. Operators
a = 5; 
b = 3; 
print(a + b)  #(arithmetic)
x = 5; 
y = 3; 
print(x > y) #(comparison)
x = 5; 
y = 3; 
print(x and y) #(logical)
 

 #5#Conversion of datatypes
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))


#Slicing of string 
b = "Hello, World!"
print(b[2:5]) 

#Modifying string 
a = "Hello, World!"
print(a.upper())
print(a.lower())

#Replace String
a = "Hello, World!"
print(a.replace("H", "J")) # we replace h with j 

#String Concatenation
# concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)

#what if 2+ diana string to concat 
#we will use format function :-f

age = 28
txt = f"My name is diana, I am {age}"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars" #2fwill add two 00 at the end 
print(txt)   

#Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)

# or 
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#5#Operators
#Arithmetic operators : +-*/%**//
#Assignment operators:= x = x + 3 ,	

#Comparison operators
#==	Equal	x == y	
#!=	Not equal	x != y	
#>	Greater than	x > y	
#<	Less than	x < y	
#>=	Greater than or equal to	x >= y	>= y	
#<=	Less than or equal to	x <= y

#Logical operators
#and -	Returns True if both statements are true	
x < 5 and  x < 10	
#or	- Returns True if one of the statements is true
x < 5 or x < 4	
#not	- Reverse the result, returns False if the result is true	not
(x < 5 and x < 10)

#Identity operators
#Membership operators
#Bitwise operators

#Set
# Set items are unordered, unchangeable, and do not allow duplicate values.
#Sets are used to store multiple items in a single variable.
thisset = {"apple", "banana", "cherry"}
print(thisset)
#
#
#Dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered, changeable and do not allow duplicates.
Dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(Dict)

#Dictionary Items
#Dictionary items are ordered, changeable, and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dict.keys() #The keys() method will return a list of all the keys in the dictionary.
print(dict["brand"]) #You can access the items of a dictionary by referring to its key name, inside square brackets:
x = dict.get("model") #another method get

#Change value  : You can change the value of a specific item by referring to its key name
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict["year"] = 2018
#or we can use update function 
dict.update({"color": "red"})
dict.update({"year": 2020})  
#to add item in dict 
dict["color"] = "red"
print(dict)
#remove item we will use pop or we can use del 
del dict["color"]
dict.pop("model")
dict.popitem() #remove last item

