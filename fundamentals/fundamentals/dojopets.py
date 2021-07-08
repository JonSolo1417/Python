class ninja:
    def __init__(self, first_name ,last_name ,treats ,pet_food ,pet):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet = pet

    def walk(self):
        print("It's thursday, we're walking")
        self.pet.play()
        return self

    def feed(self):
        print("time for crunchies!")
        self.pet.eat()
        return self

    def bathe(self):
        print("you stink!")
        self.pet.bark()
        return self
class pet:
    def __init__(self,name, type, tricks, health, energy,noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.noise = noise
    def sleep(self):
        self.energy += 25
        return self

    def bark(self):
        print(self.name + " says " + self.noise)
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.name + "'s energy increased to: " + str(self.energy) + " and health increased to: " + str(self.health))
        return self

    def play(self):
        self.health += 5
        self.energy -= 25
        print(self.name + "'s health increased to: " + str(self.health) + " energy decreased to: " + str(self.energy))
        return self
parker = pet('parker','husky', 'pound it',100, 1000, "awrawrawr")
jon = ninja('Jonathon','smith','jerky','orijen',parker)

jon.walk().bathe().feed()