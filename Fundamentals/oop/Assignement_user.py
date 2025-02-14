class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.email= email
        self.is_rewards_member= False
        self.gold_card_points = 0
# Method to enroll the user in the rewards program
    def enroll(self):
            if not self.is_rewards_member:  # Prevents re-enrollment
                self.is_rewards_member = True
                self.gold_card_points = 200
            else:
                print (f"{self.first_name} is already enrolled.")
    #Method to spend points
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points -= amount
            print(f"{self.first_name} spent {amount} points.")
        else:
            print(f"Not enough points! {self.first_name} has only {self.gold_card_points} points.")

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")

user1= User("Chaima","Louhichi","chaimalouhichi@codingdojo.com",37)
user2 = User("Alice", "Smith", "alicesmith@example.com", 25)
user3 = User("Bob", "Johnson", "bobjohnson@example.com", 40)

# Calling display_info method
user1.display_info()
user2.display_info()
user3.display_info()

# Enrolling the user
user2.enroll()
user3.enroll()
#Displaying info before spending points
print("Before spending points:")
user1.display_info()
user2.display_info()
user3.display_info()

#Spending points
user1.spend_points(50)
user2.spend_points(50)
user3.spend_points(80)

# Displaying info after spending points
print("After spending points:")
user1.display_info()
user2.display_info()
user3.display_info()
