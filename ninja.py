class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10

    def play(self):
        self.health += 5

    def noise(self):
        if self.type == "dog":
            print("Woof!")
        elif self.type == "cat":
            print("Meow!")

class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

# Example usage:
pet1 = Pet("Buddy", "dog", ["sit", "roll over"])
ninja1 = Ninja("John", "Doe", 2, 3, pet1)

print(f"{ninja1.first_name} is taking care of {pet1.name} the {pet1.type}.")
ninja1.walk()
ninja1.feed()
ninja1.bathe()
