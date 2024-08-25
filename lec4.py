#Exception Handling

try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

#Another example 
F = open('testfile.txt')
try :
	pass
except Exception:
	pass

#Lets erase the error 
try:
	f= open('testfile.txt')
except Exception:
	print("the file donot exis")

#Using Function 
def addNumbers(num1,num2):
	return(num1+num2)
print(addNumbers(1,2))
print(addNumbers(5,10))
print(addNumbers(7,"a"))
print(addNumbers(99,1))
print('Execution completed')

def addNumbers(num1,num2):
	try:
	    return(num1+num2)
	except TypeError:
		return("Not Valid ")
print(addNumbers(1,2))
print(addNumbers(5,10))
print(addNumbers(7,"a"))
print(addNumbers(99,1))
print('Execution completed')

#Exception handling using Forloop 
x=[1,4,5,6,0,7,5,3]
for x in x:
	try:
		print(10/x)
	except:
		pass
	
#Multiple except blocks:


try:
    # code that may raise an exception
except ValueError:
    # handle ValueError
except TypeError:
    # handle TypeError
except Exception as e:
    # handle any other exception
    print(f"An error occurred: {e}")
	
#lets do 
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type. Please enter numbers only.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test the function with different inputs
divide_numbers(10, 2)  # Normal case
divide_numbers(10, 0)  # ZeroDivisionError
divide_numbers("a", 2)  # TypeError
divide_numbers(10, None)  # TypeError

#Object-Oriented Programming (OOP) 
#single inheritance
# Parent class
class Shape:
    def __init__(self, color):
        self.color = color

# Child class inheriting from Shape
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

my_circle = Circle("Red", 5)
print(my_circle.color)  # Output: Red
print(my_circle.radius)  # Output: 5
print(my_circle.area())  # Output: 78.5
