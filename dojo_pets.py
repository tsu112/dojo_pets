class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise

    def sleep(self):
        self.energy += 25
        print(f"{self.name}'s energy is {self.energy}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s health is {self.health}")
        print(f"{self.name}'s energy is {self.energy}")
        return self

    def play(self):
        self.health += 5
        print(f"{self.name}'s health is {self.health}")
        return self

    def nousy(self):
        print(f"{self.name} goes {self.noise}")


class baby_pet(Pet):
    def __init__(self, name, type, tricks, noise, is_cute):
        self.is_cute = is_cute


class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        print(f"{self.first_name} fed {self.pet.name} {self.pet_food}")
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.nousy()
        return self

    def play(self):
        print(
            f"{self.first_name} gave {self.pet.name} a {self.treats} and {self.pet.name} {self.pet.tricks}")


bolba = Pet("Bolba", "chi", "rolled over", "wolf")
ema = Pet("Emma", "chi", "played dead", "bark")
ryko = baby_pet("Ryko", "chi", "whine", "cries", True)

ada = Ninja("Ada", "Yang", bolba, "bone", "dry food")
jayda = Ninja("Jayda", "Lee", ema, "toy", "wet food")
sue = Ninja("Sue", "Yang", ryko, "milk", "puppy milk")

# ada.bathe().feed().walk()
# jayda.bathe().feed().walk()
# ada.play()
