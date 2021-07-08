
class NinjaTurtle:
    sensei = "Master Splinter"
    def __init__(self, name, health = 100, energy = 50, color = "green"):
        self.name = name
        self.health = health
        self.energy = energy
        self.headband = color

    def attack(self, enemy):
        # check to see if this instance has enough energy to attack
        if NinjaTurtle.can_attack(self.energy):
            #check to see if the enemy has enough health left, or is it a killing blow!
            if NinjaTurtle.is_killing_blow(self.energy, enemy.health):
                self.energy -= 5
                enemy.energy -= 5
                enemy.health = 0
            else:
                print(f"{self.name} attacked {enemy.name} and reduced their health by 20")
                self.energy -= 5
                enemy.health -= 20
        return self

    def eat_pizza(self): 
        self.energy += 10
        return self

    def get_stats(self):
        print(f"Chowabunga! My name's {self.name} and here's How I'm doin'! Health = {self.health} and Energy = {self.energy}")
        return self

    # what if someone doesn't have the ability to attack because their energy is too low?
    # we can check it with a static method!
    @staticmethod
    def can_attack(energy):
        if energy < 20:
            print("Cannot attack! energy levels are too low!")
            return False
        else:
            return True

    # if the enemy's health is below the attackers energy level, it's a killing blow!
    @staticmethod
    def is_killing_blow(energy, enemy_health):
        if enemy_health < energy:
            print("Enemy too weak! It's a killing blow!")
            return True
        else:
            return False

leonardo = NinjaTurtle("Leonardo", color = "blue")
raphael = NinjaTurtle("Raphael", color = "red")
michelangelo = NinjaTurtle("Michelangelo", color = "orange")
donatello = NinjaTurtle("Donatello", color = "purple")

donatello.attack(leonardo).attack(leonardo).attack(leonardo).attack(leonardo).attack(leonardo)
donatello.get_stats()
leonardo.get_stats()