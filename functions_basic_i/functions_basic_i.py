#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

#Predict:
# The function number_of_food_groups() returns the integer 5.
# When we call print(number_of_food_groups()), it prints:5

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

#Predict:
#The function number_of_military_branches() is defined and returns 5.
# However, the code attempts to call number_of_days_in_a_week_silicon_or_triangle_sides(), which does not exist.
# Since Python does not find this function, it raises a NameError.

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

#Predict:
# the function number_of_books_on_hold() is defined.
# Inside the function, the first return statement returns 5 and immediately exits the function.
# The second return 10 is never reached because a return statement stops further execution of the function.
# When print(number_of_books_on_hold()) is executed, it prints the returned value, which is 5.

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

#Predict:
# The function number_of_books_on_hold() is defined with two return statements.
# The first return 5 executes, and since a return statement immediately exits the function, the second return 10 is never reached.
# When print(number_of_books_on_hold()) is called, it prints the returned value, which is 5.

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

#Predict:
# The function number_of_great_lakes() is defined to print 5, but it does not return a value.
# When x = number_of_great_lakes() is executed:
# The function prints 5.
# Since there is no return statement, the function implicitly returns None.
# x is assigned the value None.
# When print(x) is executed, it prints None.

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

#Predict:
# The function add(b, c) is defined to print b + c, but it does not return a value.
# When add(1,2) is called:
# It prints 3 but does not return anything (implicitly returns None).
# When add(2,3) is called:
# It prints 5 but does not return anything (implicitly returns None).
# The expression add(1,2) + add(2,3) tries to add None + None, which is not allowed in Python, causing a TypeError.

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

#Predict:
# The function concatenate(b, c) takes two arguments and converts them to strings.
# It concatenates (joins) the string versions of b and c using + and returns the result.
# concatenate(2,5) converts 2 to "2" and 5 to "5", then joins them as "25".
# The print() function prints "25" (a string, not a number).

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

#Predict:
#The function number_of_oceans_or_fingers_or_continents() is defined.
# Inside the function:
# b is assigned the value 100.
# print(b) prints 100.
# The if condition b < 10 is False since 100 is not less than 10.
# The else block executes, returning 10.
# The function exits before reaching return 7, so that line never runs.
# When print(number_of_oceans_or_fingers_or_continents()) is called:
# First, 100 is printed inside the function.
# Then, the function returns 10, which is printed by the print() statement.

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

#Predict:
#The function number_of_days_in_a_week_silicon_or_triangle_sides(b, c) takes two arguments, b and c.
# It checks whether b < c:
# If True, it returns 7.
# If False, it returns 14.
# The return 3 statement is never reached because the function always returns before it.
# Function Calls:
# number_of_days_in_a_week_silicon_or_triangle_sides(2,3)

# 2 < 3 is True, so it returns 7.
# Output: 7
# number_of_days_in_a_week_silicon_or_triangle_sides(5,3)

# 5 < 3 is False, so it returns 14.
# Output: 14
# number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)

# 7 + 14 = 21
# Output: 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

#Predict:
#The function addition(b, c) takes two arguments and returns their sum (b + c).
# The return b + c executes first, and the function exits after returning the sum.
# The second return 10 is never reached because the function has already returned a value and exited.
# When print(addition(3,5)) is executed, it prints the sum of 3 and 5, which is 8.

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)

#Predict:
#First print(b):
# The global variable b is set to 500, so 500 is printed.

# Second print(b):
# The global variable b is printed again, so 500 is printed again.

# Inside foobar() function:

# Inside the function foobar(), a new local variable b is assigned the value 300.
# The print(b) inside the function prints this local b, which is 300.
# After foobar():

# After the function foobar() finishes execution, the global variable b is still 500, so the third print(b) prints 500

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

#Predict:
#First print(b):
# The global variable b is set to 500, so 500 is printed.

# Second print(b):
# The global variable b is printed again, so 500 is printed again.

# Inside foobar() function:

# Inside the function foobar(), a new local variable b is assigned the value 300.
# The print(b) inside the function prints this local b, which is 300.
# The return b inside foobar() returns the local b, but this returned value is not used or printed.
# After foobar():

# After the function foobar() finishes execution, the global variable b remains unchanged, still 500, so the third print(b) prints 500.

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

#Predict:
#First print(b):
# The global variable b is set to 500, so 500 is printed.

# Second print(b):
# The global variable b is printed again, so 500 is printed again.

# Inside foobar() function:

# Inside the function foobar(), a local variable b is assigned the value 300.
# The print(b) inside the function prints this local b, which is 300.
# The return b inside foobar() returns the local b (which is 300), and this value is assigned to the global b in the statement b = foobar().
# After foobar() execution:

# Since the returned value (300) is assigned to b, the global b is now 300.
# The third print(b) prints the updated value of b, which is 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

#Predict:
#The function foo() is called:
# It first prints 1.
# Then, it calls the function bar().
# Inside bar():

# bar() prints 3.
# After bar() finishes execution, control returns to foo().
# Back in foo():

# After bar() completes, foo() prints 2.

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

#Predict:
# The function foo() is called
# It first prints 1
# Then, it calls bar() and assigns the result of bar() to x
# Inside bar():

# bar() prints 3.
# Then, bar() returns 5 to the variable x in foo()
# Back in foo():

# The value 5 (returned from bar()) is assigned to x, and foo() prints 5
# Finally, foo() returns 10
# The value returned by foo() (which is 10) is assigned to the variable y, and print(y) prints 10.