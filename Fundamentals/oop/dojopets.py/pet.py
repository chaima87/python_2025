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
        print(f"{self.name} is eating. Energy: {self.energy}, Health: {self.health}.")
    
    def play(self):
        self.health += 5
        print(f"{self.name} is playing. Health increased to {self.health}.")
    
    def noise(self):
        print(f"{self.name} makes a noise!")
