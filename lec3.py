#For loop & While Loop 
#forloop- A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
hello=[1,2,3,4,5,6,7,8,9,10] #suppose we have 10 values n we need to print in a loop
for i in hello:
    print(i)
#even no problem #printing only even
#An even number is an integer that is divisible by 2 with no remainder.(-6, -4, 0, 2, 4, 6, 8, 10)
for i in l1:
    if i%2==0:
        print(i)
    else:
      print("odd")

#else 


# Print even numbers
print("Even numbers:")
for number in range(1, 21):
    if number % 2 == 0:  # Check if the number is even
        print(number)






#odd no:- An odd number is an integer that is not divisible by 2 evenly, meaning it leaves a remainder of 1(-5, -3, -1, 1, 3, 5, 7, 9).
# Print odd numbers
print("Odd numbers:")
for number in range(1, 21):
    if number % 2 != 0:  # Check if the number is odd
        print(number)
#What is range?
#range is a built-in Python function that generates a sequence of numbers, which can be used to iterate over a loop.
# parts of range(start, stop, step)


#while loops
#it repeated execute single statement
i = 1
while i < 20:
  print(i)
  i += 1  # Increment i by 1 in each iteration

#while Loop
#With the while loop we can execute a set of statements as long as a condition is true.
# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 15:
  print(i)
  if (i == 9):
    break
  i += 1

#What is a User Defined Function?
#A User Defined Function is a block of code that can be called multiple times 
#from different parts of your program. 
#It's a way to reuse code, make your program more modular, and reduce repetition.

def function_name(parameters):
    # code to be executed

#1. def: Keyword to define a function
#2. function_name: Name given to the function
#3. parameters: Input values passed to the function (optional)
#4. code to be executed: Indented block of code that runs when the function is called
def greet(name):
    print("Hello, " + name + "!")

greet("Dina")
greet("John")
greet("Alice")
greet("Bob")
#asking user 
def greet(name):
    print("Hello, " + name + "!")

# Ask the user for their name
user_name = input("Please enter your name: ") #input(): This is a built-in Python function that allows the program to read user input.

# Call the greet function with the user's name
greet(user_name)


#What is Recursion?
#Recursion is a programming technique where a function calls itself repeatedly until it reaches a base case that stops the recursion.
How does Recursion work?

1. A function calls itself with a smaller input or a modified version of the original input.
2. The function solves the smaller problem and returns the result.
3. The result is used to solve the next smaller problem, and so on.
4. The process continues until the base case is reached, stopping the recursion.

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:
        return n * factorial(n-1)  # Recursive call


#Modules in python :
Python has a vast collection of built-in modules that provide various functionalities, including:

1. Math: Mathematical functions like sin, cos, tan, etc.
2. Statistics: Statistical functions like mean, median, mode, etc.
3. Time: Time-related functions like current time, sleep, etc.
4. Random: Random number generation.
5. Os: Operating system interactions like file operations, environment variables, etc.
6. Sys: System-specific functions like exit, stdin, stdout, etc.
7. Re: Regular expressions for pattern matching.
8. Json: JSON data parsing and generation.
9. Csv: CSV file reading and writing.
10. Xml: XML parsing and generation.
11. Http: HTTP client and server functionality.
12. Urllib: URL parsing and retrieval.
13. Socket: Network socket programming.
14. Select: I/O multiplexing for network sockets.
15. Threading: Thread-based parallelism.
16. Multiprocessing: Process-based parallelism.
17. Logging: Logging framework for error tracking.
18. Argparse: Command-line argument parsing.
19. Configparser: Configuration file parsing.
20. Pathlib= ('Path manipulation and file system interactions')

#go to cmd install lib - pip install 

#OOPS
#Class 
 #- I added an __init__ method to the Person class. This is a special method that gets called when an object is created from the class.
 #I defined the attributes name, occupation, and networth inside the __init__ method using self.attribute_name.
# I created an object a from the Person class, passing in the values for name, occupation, and networth.

class Person:
    def __init__(self, name, occupation, networth):
        self.name = name
        self.occupation = occupation
        self.networth = networth

a = Person("Dina", "Software dev", 5)

print(a.name)  # Output: Dina
print(a.occupation)  # Output: Software dev
print(a.networth)  # Output: 5
#user input class n obj 
-------------------------------------------------------
name = input("Enter your name: ")
occupation = input("Enter your occupation: ")
networth = int(input("Enter your networth: "))

a = Person(name, occupation, networth)

print(a.name)
print(a.occupation)
print(a.networth)
#--------------------
Parent Class (Animal)


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("The animal makes a sound.")


Child Class (Dog)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("The dog barks.")


#In this example:

- Animal is the parent class.
- Dog is the child class that inherits from Animal.
- Dog has its own __init__ method, which calls the parent's __init__ method using super().__init__(name).
- Dog overrides the sound method to provide its own implementation.

#Now, let's create a Dog object:


my_dog = Dog("Max", "Golden Retriever")
print(my_dog.name)  # Output: Max
print(my_dog.breed)  # Output: Golden Retriever
my_dog.sound()  # Output: The dog barks.


#In this example, Dog inherits the name attribute and the sound method from Animal, but also adds its own breed attribute and overrides the sound method. 
#This is a simple demonstration of inheritance in action!