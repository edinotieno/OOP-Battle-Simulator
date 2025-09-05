import random
from enemy import Enemy

class Goblin(Enemy):
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """

    def __init__(self, name, color):
        super().__init__(name) # Super takes all the atributes from the parent class
        self.color = color