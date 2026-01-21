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
    "Strength Potion": {
        "effect": "strength",
        "value": 20,
        "available": 5
    }
}

class hero:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        
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
    hero_choosed = choose_hero()
    hero_names = list(heroes.keys())

    
if __name__ == "__main__":
    choose_hero()
    main()