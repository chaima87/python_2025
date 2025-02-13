# Variable Declaration
num1 = 42  # Primitive - Number (Integer)
num2 = 2.3  # Primitive - Number (Float)
boolean = True  # Primitive - Boolean
string = 'Hello World'  # Primitive - String

# Composite Data Types

# List - Initialize
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# Dictionary - Initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# Tuple - Initialize
fruit = ('blueberry', 'strawberry', 'banana')

# Type Check
print(type(fruit))  # Log statement

# List - Access Value
print(pizza_toppings[1])  # Logs 'Sausage'

# List - Add Value
pizza_toppings.append('Mushrooms')

# Dictionary - Access Value
print(person['name'])  # Logs 'John'

# Dictionary - Change Value
person['name'] = 'George'

# Dictionary - Add Value
person['eye_color'] = 'blue'

# Tuple - Access Value
print(fruit[2])  # Logs 'banana'

# Conditional - If/Else
if num1 > 45:  # If condition
    print("It's greater")  
else:  # Else condition
    print("It's lower")  

# Length Check
if len(string) < 5:
    print("It's a short word!")  
elif len(string) > 15:  # Else If condition
    print("It's a long word!")  
else:
    print("Just right!")  

# For Loop - Start, Stop, Increment
for x in range(5):  # Start at 0, Stop at 4 (implicit increment of 1)
    print(x)  

for x in range(2, 5):  # Start at 2, Stop at 4
    print(x)  

for x in range(2, 10, 3):  # Start at 2, Stop at 10, Increment by 3
    print(x)  

# While Loop - Start, Stop, Increment
x = 0  # Start
while x < 5:  # Stop Condition
    print(x)  
    x += 1  # Increment

# List - Delete Value
pizza_toppings.pop()  # Removes last element
pizza_toppings.pop(1)  # Removes element at index 1

# Dictionary - Delete Value
print(person)
person.pop('eye_color')  
print(person)

# For Loop - Continue & Break
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue  # Skips 'Pepperoni'
    print('After 1st if statement')
    if topping == 'Olives':
        break  # Stops loop when 'Olives' is found

# Function - No Parameters
def print_hello_ten_times():
    for num in range(10):  # Sequence in for loop
        print('Hello')

print_hello_ten_times()  # Function Call

# Function - Parameter & Argument
def print_hello_x_times(x):  # Parameter
    for num in range(x):
        print('Hello')

print_hello_x_times(4)  # Argument

# Function - Default Parameter Value
def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()  # Uses default value (10)
print_hello_x_or_ten_times(4)  # Overrides default value with argument (4)

"""
Bonus Section
"""

# NameError: name 'num3' is not defined
# print(num3)  
# num3 = 72  

# TypeError: 'tuple' object does not support item assignment
# fruit[0] = 'cranberry'  

# KeyError: 'favorite_team'
# print(person['favorite_team'])  

# IndexError: list index out of range
