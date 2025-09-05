from enemy import Enemy

class baby_elf(Enemy):
    # A new special ability
    def cry():
        print("wahhhh (˃̣̣̥ᯅ˂̣̣̥)")

    def take_damage(self, damage): # Overides the parent class' function
        print("Why are you attacking a baby, YOU MONSTER")
        return super().take_damage(damage)