class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42
# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!
user_ada = User()
#print(user_ada.first_name) # prints Ada

class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42
user_ada = User()
#print(user_ada.last_name)
#print(user_ada.first_name)
# Create another user called user_2!
class User2:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42
user_ada = User2()
#print(user_ada.last_name)
#print(user_ada.first_name)
# Print user_ada's last name.
# Print user_2's last name. (Yes, they should be the same)
# Run the code, pause, go back and step through one line at a time
# What do you notice about the order it runs in?
# Write down any other questions you have.
# Sensei Exercise: try just printing the variable, user_ada.
#   What prints to the terminal?

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
    	# the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
#print(skater_shoe.type)	# output: Low-top Trainers
#print(dress_shoe.type)	# output: Ballet Flats

class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
    	# we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
#print(skater_shoe.type)	# output: Low-top Trainers
#print(dress_shoe.type)	# output: Ballet Flats
# Ninja Challenges!
# Open this code on the Trace website to get a better view of all the variables and their attributes.
# Make a new instance of a shoe
# Update the in_stock attribute to False

# Creating a new shoe instance
running_shoe = Shoe("Nike", "Running Shoes", 89.99)

# Updating in_stock to False
running_shoe.in_stock = False

# Printing attributes to verify
#print(running_shoe.brand)  # Output: Nike
#print(running_shoe.type)   # Output: Running Shoes
#print(running_shoe.price)  # Output: 89.99
#print(running_shoe.in_stock)  # Output: False

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
    # adding the greeting method
    def greeting(self):
        print(f"Hello, my name is {self.name}")

adrien = User("Adrien", "adion@codingdojo.com")
cool_person = User("Sadie", "sflick@codingdojo.com")
    
#adrien.greeting()
# prints Hello, my name is Adrien
    
#cool_person.greeting()
# prints Hello, my name is Sadie

class Shoe:
    def __init__(self, brand, shoe_type, price):
        self.brand = brand
        self.type = shoe_type
        self.price = price
        self.in_stock = True
    
    # Takes a float/percent as an argument and reduces the
    # price of the item by that percentage.
    def on_sale_by_percent(self, percent_off):
        self.price = self.price * (1-percent_off)
    
    # Returns a total with tax added to the price.
    def total_with_tax(self, tax_rate):
        tax = self.price * tax_rate
        total = self.price + tax
        return total
    
    # Reduces the price by a fixed dollar amount.
    def cut_price_by(self, amount):
    	if amount < self.price:
        	self.price -= amount
    	else:
    		print("Price deduction too large.")
# Create some shoes. Call some methods on those shoes. Print your shoe's attributes..
my_shoe = Shoe("Converse", "Low-tops", 36.00)
print(my_shoe.total_with_tax(0.05))
my_shoe.cut_price_by(10)
print(my_shoe.price)




