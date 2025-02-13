#1.Countdown
for i in range (5,-1,-1):
    print (i)

#2.Print and Return 
def print_and_return (num1,num2):
        print(num1)
        return(num2)
print_and_return(1,2)

#First Plus Length
def sum_first_and_length(numbers):
    return numbers[0] + len(numbers)  # First value + length of the list

result = sum_first_and_length([5, 2, 3, 4])  
print(result)

#Values Greater than Second
def values_greater_than_second(lst):
    if len(lst) < 2:  # Check if the list has at least 2 elements
        return False
    
    second_value = lst[1]  # Get the second value
    new_list = [num for num in lst if num > second_value]  # Filter values greater than the second
    
    print(len(new_list))  # Print the count of values greater than the second
    return new_list  # Return the new list

print(values_greater_than_second([5, 3, 8, 10, 2]))
print(values_greater_than_second([3]))

#This Length, That Value
def this_length_that_value(size, value):
    return [value] * size

print(this_length_that_value(4, 9))
print(this_length_that_value(3, 5))

