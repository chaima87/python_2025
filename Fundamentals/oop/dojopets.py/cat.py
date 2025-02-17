from pet import Pet

class Cat(Pet):
    def __init__(self, name, tricks):
        super().__init__(name, "Cat", tricks)
    
    def noise(self):
        print(f"{self.name} meows!")
