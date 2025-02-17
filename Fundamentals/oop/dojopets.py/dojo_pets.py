class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    def walk(self):
        print(f"{self.first_name} is walking {self.pet.name}.")
        self.pet.play()
    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name}.")
        self.pet.eat()
    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}.")
        self.pet.noise()
class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
    def sleep(self):
        self.energy += 25
        print(f"{self.name} is sleeping. Energy increased to {self.energy}.")
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating. Energy: {self.energy}, health:{self.health}.")
    def play(self):
        self.health += 5
        print(f"{self.name} is playing. health increased to {self.health}.")
    def noise(self):
        print(f"{self.name} makes a noise!")
class Dog(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Dog", tricks)
    def noise(self):
        print(f"{self.name} barks!")

class Cat(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Cat", tricks)
    def noise(self):
        print(f"{self.name} meows!")

class Bird(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Bird", tricks)
    
    def noise(self):
        print(f"{self.name} chirps!")

class Rabbit(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Rabbit", tricks)
    
    def noise(self):
        print(f"{self.name} thumps!")

dog = Dog("Tessy", ["sit", "roll over"])
cat = Cat("Whiskers", ["Jump", "Scratch"])
bird = Bird("Tweety", ["Sing", "Fly"])
rabbit = Rabbit("Thumper", ["Hop", "Spin"])
Ninja = Ninja("Alice", "Doe", dog, "Biscuits", "kibble")
Ninja.walk()
Ninja.feed()
Ninja.bathe()
