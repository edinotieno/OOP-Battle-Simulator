from enemy import Enemy 
import random

class Boss(Enemy):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type 
        self.health = 300

    def special_attack(self):
        self.attack_power = random.randint(10,20)
        return self.attack_power

    def special_abilities(self):
        roll = random.randint(1,3)

        if self.type == "Magic":
            self.attack_power = 30
            print(f"{self.name} uses a magic spell ∋(。・”・)_†:*.;”.*・;・")

        elif self.type == "Normal":
            self.attack_power = 30'
            print(f"{self.name} throws a powerfull punch /( .□.) ︵╰(゜益゜)╯︵ /(.□. /)")

        elif self.type == "Dragon":
            self.attack_power = 30
            print(f"{self.name} launches a fireball ")

# TODO: Finish type abilities  