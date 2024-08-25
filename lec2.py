#Python Conditions and If statements
#Python supports the usual logical conditions from mathematics:
#Equals: a += b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#if,else,elif -types of statements 
#statements help us to tell comptr to perfrm particulr function 
#if is ouse only for 1 condition

if 5>3: #every function ends with colon:
    print('true') #indentation -it is imp (space)

#if we have more then 2 condition
a=8
b=6 
if a<b:
    print('b')
else:
    print('a')
#elif :it has 3 values it can be use when we have more then 2 condition
a=1
b=2
c=3
if a>b:
    print('a')
elif b>c:
    print('b')
elif c>a:
    print('c')
else:
    print('none')
---------------------------------------------------------------
#If statement:
a = 33
b = 200

if b > a:
    print("b is greater than a")







#Elif statement
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#elseif 
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#---
a = 330
b = 330
print("A") if a > b else print("equal") if a == b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# The or keyword is a logical operator, and is used to combine conditional statements:

A = 10
B = 5
C = 8
#Nested If-You can have if statements inside if statements, this is called nested if statements.
if A > B or B == C:
    if A > B:
        print("A is greater than B")
    elif B == C:
        print("B and C are equal")
else:
    if not B > C:
        print("C is smaller than B")
    else:
        print("B is greater than C")



