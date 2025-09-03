import random

class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        self.name = name
        self.health = 500
        self.attack_power = 20  

    def strike(self):
        crit = random.randint(1,10)
        if crit >= 8:
            return self.attack_power * 2

    def receive_damage(self, damage):
        if self.health - damage < 0:
            damage = damage - self.health
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
