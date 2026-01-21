import random 
import pandas as pd
import openpyxl as oxl

heroes = {
    "Knight King": {
        "health": 100,
        "attack": 20,
        "defense": 10,
        "summary": "A brave knight with balanced stats."
    },
    "Archer King": {
        "health": 80,
        "attack": 25,
        "defense": 5,
        "summary": "A skilled archer with high attack and low defense."
    },
    "Bomber King": {
        "health": 50,
        "attack": 30,
        "defense": 8,
        "summary": "An explosive expert with high attack power."
    }
}

monsters = {
    "Goblin": {
        "health": 50,
        "attack": 10,
        "defense": 3
    },
    "Orc": {
        "health": 70,
        "attack": 15,
        "defense": 5
    },
    "Dragon": {
        "health": 200,
        "attack": 40,
        "defense": 15
    }
}

monster_bosses = {
    "Goblin King": {
        "health": 150,
        "attack": 25,
        "defense": 10
    },
    "Orc King": {
        "health": 180,
        "attack": 30,
        "defense": 12
    },
    "Dragon King": {
        "health": 300,
        "attack": 50,
        "defense": 20
    }
}

items = {
    "Health Potion": {
        "effect": "heal",
        "value": 20,
        "available": 5
    },
    "Shield": {
        "effect": "defense",
        "value": 20,
        "available": 5
    },
    "Rage": {
        "effect": "strength",
        "value": 20,
        "available": 5
    }
}

class hero:
    def __init__(self, name, health, attack, defense, items_show={}):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.items_show = items_show or {"Health Potion": 0, "Shield": 0, "Rage": 0}
        
    def item_use(self, item):
        if item["available"] <= 0:
            print("Item not available")
            return
        if item["effect"] == "heal":
            self.health += item["value"]
        elif item["effect"] == "defense":
            self.defense += item["value"]
        elif item["effect"] == "strength":
            self.attack += item["value"]
    
    def display_stats(self):
        print(f"Hero: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Items: {self.items_show}")
  
class monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense 
        
class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.file = f"{username}_data.xlsx"
    
def login(username, password):
    new_old = input("Are you a new user? (yes/no): ").strip().lower()
    if new_old == 'yes':
        user_data = pd.DataFrame({'Username': [username], 'Password': [password]})
        user_data.to_excel(f"{username}_data.xlsx", index=False)
        print("User registered successfully.")
        return True
    try:
        with pd.read_excel(f"{username}_data.xlsx") as df:
            stored_password = df.at[0, 'Password']
            if stored_password == password:
                print("Login successful.")
                return True
            else:
                print("Incorrect password.")
                return False
    except FileNotFoundError:
        print("User not found.")
        return False

def choose_hero():
    print("Choose your hero:")
    for i, (hero_name, hero_stats) in enumerate(heroes.items(), start=1):
        print(f"{i}. {hero_name} - {hero_stats['summary']}\n  Health: {hero_stats['health']}, Attack: {hero_stats['attack']}, Defense: {hero_stats['defense']}\n")
    
    choice = input("Choose your hero : ")
    choice = choice.strip()
    choice = choice.lower()

    if choice == '1' or choice == "knight king" or choice == "knight" or choice == "knightking":
        print("You have chosen Knight King!\nTip : Knights have balanced stats, making them versatile in battle.")
        return 0
    elif choice == '2' or choice == "archer king" or choice == "archer" or choice == "archerking":
        print("You have chosen Archer King!\nTip : Archers have high attack power and low defense.")
        return 1
    elif choice == '3' or choice == "bomber king" or choice == "bomber" or choice == "bomberking":
        print("You have chosen Bomber King!\nTip : Bombers have high attack power and moderate defense.")
        return 2
    else:
        print("Invalid choice. Please choose a valid hero number.")
        return choose_hero()

def main():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    login(username, password)
    hero_choosed = choose_hero()
    hero_name = list(heroes.keys())[hero_choosed]
    hero_stats = heroes[hero_name]
    player_hero = hero(hero_name, hero_stats["health"], hero_stats["attack"], hero_stats["defense"])
    player_hero.display_stats()

    
if __name__ == "__main__":
    main()