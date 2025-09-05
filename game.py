import random
from goblin import Goblin
from hero import Hero
from time import sleep 

def main():
    print("Welcome to the Battle Arena!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")

    # Create a hero
    hero = Hero("Aether")

    # Makes a list of 3 goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Goblin(f"Goblin {i+1}") for i in range(3)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    
    # For whenever an enemy's attack is stopped
    cannot_play = False

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!") # \n prints whatever is infront of it on a new line

        # Special ability!
        if hero.health <= 20:
            question = input(f"Oh no! Your hero is at {hero.health} hp! Would you like to use a special ability? y/n ")
            if question == "y":
                if hero.special_abilities():
                    cannot_play += len(goblins)

        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"Hero attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                if cannot_play > 0:
                    damage = 0
                    print("Goblin cannot give your hero damage! Mwahaha!")
                    hero.receive_damage(damage)
                    cannot_play -= 1
                else:
                    damage = goblin.attack()
                    print(f"{goblin.name} attacks hero for {damage} damage!")
                    hero.receive_damage(damage)
        sleep(2)

    # Determine outcome
    if hero.is_alive():
        print(f"\nThe hero has defeated all the goblins! ༼ ᕤ◕◡◕ ༽ᕤ")
    else:
        print(f"\nThe hero has been defeated. Game Over. (｡•́︿•̀｡)")

    # Final tally of goblins defeated
    print(f"\nTotal goblins defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()
