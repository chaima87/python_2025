# Challenge yourself!
person = {"first_name": "Ada", "last_name": "Lovelace", "age": 42, "is_organ_donor": True}
#print(person)
# Create a another person dictionary called person_2 and print it to the terminal
person2 = {"first_name": "chaima", "last_name": "Louhichi", "age": 37, "is_organ_donor": False}
person2["email"]="chaimalouhichi87@gmail.com"
person2["age"]=23
#print(person2)
#capitals = {
# "svk":"Bratislava",
# "deu": "Berlin",
# "dnk": "Copenhagen",
# "Fr":"Paris",
# "USA":"America",
# }

# capitals["svk"] = "Bratislava"
# capitals["deu"] = "Berlin"
# capitals["dnk"] = "Copenhagen"
# capitals["Fr"]= "Paris"
# capitals["USA"]= "America"
#print(capitals)
# Add 2 key-value pairs to this dictionary.
# print the capitals dictionary to see how it changed!

countries_so_far = {"Mexico": 1, "Morocco": 1}
new_visits = ["Albania", "Mexico", "Togo", "Morocco"]
    
# To add Albania to the list
countries_so_far["Albania"] = 1
#print(countries_so_far)
# To add 1 to the Mexico tally
countries_so_far["Mexico"] += 1 # Changes Mexico tally to 2!
#print(countries_so_far)
# your code here to finish updating your travel log!

#print(person["first_name"])
full_name = person["first_name"] + " " + person["last_name"]

# value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
# del capitals['dnk'] # will delete the key, and not return anything
#print(capitals)

my_dict = { "name": "Noelle", "language": "Python" }
#for each_key in my_dict:
    #print(each_key)
# output: name, language

my_dict = { "name": "Noelle", "language": "Python" }
#for each_key in my_dict:
    #print(my_dict[each_key])
# output: Noelle, Python

# capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# # another way to iterate through the keys
# for key in capitals.keys():
#     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
# for val in capitals.values():
#      print(val)
# # output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# #to iterate through both keys and values
# for key, val in capitals.items():
#     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}

print(resume_data["skills"][1])
print(users[2]["first"])


