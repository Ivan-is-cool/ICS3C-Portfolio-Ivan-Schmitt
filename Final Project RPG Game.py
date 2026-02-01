import random

# -------------------------
# Player setup
# -------------------------
player = {
    "name": "",
    "hp": 100,
    "max_hp": 100,
    "attack": 15,
    "level": 1,
    "gold": 0
}

enemies = [
    {"name": "Goblin", "hp": 40, "attack": 8, "gold": 10},
    {"name": "Skeleton", "hp": 50, "attack": 10, "gold": 15},
    {"name": "Orc", "hp": 70, "attack": 12, "gold": 25},
]

# -------------------------
# Helper functions
# -------------------------
def print_stats():
    print(f"\n{player['name']} - HP: {player['hp']}/{player['max_hp']} | "
          f"Level: {player['level']} | Attack: {player['attack']} | Gold: {player['gold']}")

def heal():
    if player["gold"] >= 10:
        heal_amount = 30
        player["hp"] = min(player["max_hp"], player["hp"] + heal_amount)
        player["gold"] -= 10
        print(f"You healed for {heal_amount} HP!")
    else:
        print("Not enough gold to heal.")

def level_up():
    player["level"] += 1
    player["max_hp"] += 20
    player["attack"] += 5
    player["hp"] = player["max_hp"]
    print("\n*** LEVEL UP! ***")
    print("Your strength has increased!")

def fight():
    enemy = random.choice(enemies).copy()
    print(f"\nA wild {enemy['name']} appears!")

    while enemy["hp"] > 0 and player["hp"] > 0:
        print(f"\n{enemy['name']} HP: {enemy['hp']}")
        print_stats()
        choice = input("\n(F)ight  (R)un: ").lower()

        if choice == "r":
            if random.random() < 0.5:
                print("You successfully escaped!")
                return
            else:
                print("You failed to escape!")

        # Player attack
        damage = random.randint(player["attack"] - 5, player["attack"] + 5)
        enemy["hp"] -= damage
        print(f"You hit the {enemy['name']} for {damage} damage!")

        if enemy["hp"] <= 0:
            print(f"You defeated the {enemy['name']}!")
            player["gold"] += enemy["gold"]
            print(f"You found {enemy['gold']} gold!")
            if random.random() < 0.3:
                level_up()
            return

        # Enemy attack
        enemy_damage = random.randint(enemy["attack"] - 3, enemy["attack"] + 3)
        player["hp"] -= enemy_damage
        print(f"The {enemy['name']} hits you for {enemy_damage} damage!")

    if player["hp"] <= 0:
        print("\nYou have been defeated...")
        exit()

# -------------------------
# Game loop
# -------------------------
def main():
    print("=== TEXT Based RPG ===")
    player["name"] = input("Enter your hero's name: ")

    while True:
        print_stats()
        print("\nWhat do you want to do?")
        print("1. Explore")
        print("2. Heal (10 gold)")
        print("3. Quit")

        choice = input("> ")

        if choice == "1":
            fight()
        elif choice == "2":
            heal()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
