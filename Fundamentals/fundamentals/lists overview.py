# fruits = ['apple', 'banana', 'orange', 'strawberry']
# vegetables = ['lettuce', 'cucumber', 'carrots']
# fruits_and_vegetables = fruits + vegetables
# print(fruits_and_vegetables)
# salad = 3 * vegetables
# print(salad)

# # play around with the drawers!
# drawers = ['documents', 'envelopes', 'pens']
# # Print the second value from the list (envelopes)
# print(drawers [1])
# # Change "pens" to "useless manuals"
# drawers [2]="useless manuals"
# print(drawers)
# # Change the first value to whatever is the second value
# drawers[0]= "envelopes"
# drawers[1]=drawers[0]
# print(drawers)
# # What should the list look like now?
# # Print the list! Does it match your prediction?

# words = ["start","going","till","the","end"]
# # Sub-ranges (portions) of the list
# print(words[1:]) # prints ['going', 'till', 'the', 'end']
# print(words[:4]) # prints ['start', 'going', 'till', 'the']
# print(words[2:4]) # prints ['till', 'the']
    
# # Making a copy of a list
# copy_of_words = words[:]
# copy_of_words.append("dojo") # only appends to the copy
# print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
# print(words) # prints ['start', 'going', 'till', 'the', 'end']

# my_list = [1, 'Zen', 'hi']
# print(len(my_list))
# max_value=max(list)
# print(max_value)

# some_nums = [44,56,2,3,12,19,6]
# print("Get started by writing your own code!")
# # Some optional challenges to assess and refine your understanding:
# # Print the length of the list.
# print(len(some_nums))
# # Use antoher python built-in function and print the result.
# # Remove an item from the list.
# some_nums.pop(5)
# print(some_nums)
# # Remember to verify that it was removed.
# # Utilize a method from the documentation and print the result.

# countries = ["Uganda", "Chile", "Albania", "Saudi Arabia"]
# # Challenge 1: Fix the range!
# for integer in range(0, 7):
#     print("Index")
#     # Challenge 2: print the index here
#     print("Country[3]")
#     # Challenge 3: print the country here
#     print("Saoudi Arabia")
# # Looping over values only...
# for country in countries:
#     print("Country: ")
#     # Challenge 4: print the country here


# def add(a, b):
#     x = a + b
#     return x
# sum1 = add(4,6)
# sum2 = add(1,4)
# sum3 = sum1 + sum2
# print(sum1,sum2,sum3)


# Challenge 1:
#   Fill in the missing code for the full_name function.
#   Be sure to add the 2 parameters (and name them appropriately)
#   Return the full name to get the desired output!

# def full_name(first,last):
#     return first + "," + last
# name1 = full_name("Eddie", "Aikau")
# print(name1) # should print Eddie Aikau
# # Challenge 2: 
# #   Call the function again using your own name and print the results!

# def full_name(first,last):
#     return first + "" + last
# name1 = full_name("Louhichi", "Chaima")
# print(name1)

# # set defaults when declaring the parameters
# def be_cheerful(name='', repeat=2):
# 	print(f"good morning {name}\n" * repeat)
# be_cheerful()
# # output: good morning (repeated on 2 lines)
# be_cheerful("tim")
# # output: good morning tim (repeated on 2 lines)
# be_cheerful(name="john")
# # output: good morning john (repeated on 2 lines)
# be_cheerful(repeat=6)
# # output: good morning (repeated on 6 lines)
# be_cheerful(name="michael", repeat=5)
# # output: good morning michael (repeated on 5 lines)
# # NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# be_cheerful(repeat=3, name="kb")
# # output: good morning kb (repeated on 3 lines)

def multiply(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)


