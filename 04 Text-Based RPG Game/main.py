import random 
import pandas as pd
import openpyxl as oxl

login_status = False

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
    def __init__(self, username, password, stage=1, coins=0):
        self.username = username
        self.password = password
        self.stage = stage
        self.coins = coins
        self.file = f"{username}_data.xlsx"
        
    def save_data(self):
        user_data = pd.DataFrame({'Username': [self.username], 'Password': [self.password], 'Stage' : [self.stage], 'Coins' : [self.coins]})
        user_data.to_excel(self.file, index=False)
    
def login(username, password):
    new_old = input("Are you a new user? (yes/no): ").strip().lower()
    if new_old == 'yes':
        user_data = pd.DataFrame({'Username': [username], 'Password': [password], 'Stage' : [1], 'Coins' : [0]})
        user_data.to_excel(f"{username}_data.xlsx", index=False)
        print("User registered successfully.")
        global login_status
        login_status = True
        return True
    elif new_old != 'no':
        print("Invalid input. Please enter 'yes' or 'no'.")
        return login(username, password)
    try:
        with pd.read_excel(f"{username}_data.xlsx") as df:
            stored_password = df.at[0, 'Password']
            if stored_password == password:
                print("Login successful.")
                global login_status
                login_status = True
                return True
            else:
                print("Incorrect password.")
                return False
    except FileNotFoundError:
        print("User not found.")
        return False
    
def logout():
    pass

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
    
class game_info:
    @staticmethod
    def about_game():
        print("This is a Text-Based RPG Game where you can choose heroes, fight monsters, and progress through stages.")
        print("Each hero has unique stats and abilities. Defeat monsters to earn coins and advance.")
        print("Use items wisely to enhance your hero's performance in battles.")
        print("Good luck on your adventure!")
        print("---------------------------")
        print("Game Info Menu:")
        print("1. Return to main menu")
        print("2. How to Play")
        print("3. Game Rules")
        print("4. Game Tips")
        print("5. Heroes Info")
        print("6. Monsters Info")
        print("7. Monster Bosses Info")
        print("---------------------------")
        info_choice = input("Choose an option: ")
        if info_choice == '1':
            return menu.main_menu()
        elif info_choice == '2':
            game_info.how_to_play()
        elif info_choice == '3':
            game_info.game_rules()
        elif info_choice == '4':
            game_info.game_tips()
        elif info_choice == '5':
            game_info.heros_info()
        elif info_choice == '6':
            game_info.monsters_info()
        elif info_choice == '7':
            game_info.monster_bosses_info()
        else:
            print("Invalid choice. Please choose a valid option.")
        return menu.menu_on_login()
    
    @staticmethod
    def how_to_play():
        print("1. Login or register as a new user.")
        print("2. Choose your hero from the available options.")
        print("3. Fight monsters to earn coins and progress through stages.")
        print("4. Use items to heal, boost defense, or increase attack power.")
        print("5. Advance through stages by defeating monsters and bosses.")
        print("6. Enjoy the game and have fun!")
        print("---------------------------")
    
    @staticmethod
    def game_rules():
        print("1. Each hero has unique stats: health, attack, and defense.")
        print("2. Monsters have their own stats and can be defeated to earn coins.")
        print("3. Use items strategically to enhance your hero's abilities.")
        print("4. Progress through stages by defeating monsters and bosses.")
        print("5. Save your progress by logging in with your username and password.")
        print("---------------------------")
    
    @staticmethod
    def game_tips():
        print("1. Choose a hero that suits your playstyle.")
        print("2. Use items wisely to maximize their benefits.")
        print("3. Pay attention to monster stats and plan your attacks accordingly.")
        print("4. Save your progress frequently by logging in.")
        print("5. Experiment with different strategies to defeat tougher monsters.")
        print("---------------------------")
        
    @staticmethod
    def heros_info():
        print("Hero Information:")
        for hero_name, hero_stats in heroes.items():
            print(f"{hero_name} - {hero_stats['summary']}\n  Health: {hero_stats['health']}, Attack: {hero_stats['attack']}, Defense: {hero_stats['defense']}\n")
        print("---------------------------")

    @staticmethod
    def monsters_info():
        print("Monster Information:")
        for monster_name, monster_stats in monsters.items():
            print(f"{monster_name}\n  Health: {monster_stats['health']}, Attack: {monster_stats['attack']}, Defense: {monster_stats['defense']}\n")
        print("---------------------------")
        
    @staticmethod
    def monster_bosses_info():
        print("Monster Bosses Information:")
        for boss_name, boss_stats in monster_bosses.items():
            print(f"{boss_name}\n  Health: {boss_stats['health']}, Attack: {boss_stats['attack']}, Defense: {boss_stats['defense']}\n")
        print("---------------------------")
        
class menu:
    @staticmethod
    def main_menu():
        if login_status:
            return menu.menu_on_login()
        else:
            print("Welcome to the Text-Based RPG Game!")
            print("1. Login")
            print("2. Learn about game")
            print("3. Exit")
            print("---------------------------")
            choice = input("Choose an option: ")
            if choice == '1':
                return login(input("Enter your username: "), input("Enter your password: "))
            elif choice == '2':
                game_info.about_game()
            elif choice == '3':
                print("Exiting the game. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please choose a valid option.")
                return menu.main_menu()
    
    @staticmethod
    def menu_on_login():
        if not login_status:
            print("You need to login first.")
            return menu.main_menu()
        print("Main Menu:")
        print("1. Start Game")
        print("2. Game Info")
        print("3. Your Stats")
        print("4. Logout")
        print("---------------------------")
        choice = input("Choose an option: ")
        if choice == '1':
            return start_game()
        elif choice == '2':
            return game_info.about_game()
        elif choice == '3':
            print("Your Stats feature is under development.")
            return menu.menu_on_login()
        elif choice == '4':
            logout()
            print("You have been logged out.")
            return menu.main_menu()
        else :
            print("Invalid choice. Please choose a valid option.")
            return menu.menu_on_login()

def start_game():
    print("Game started!")
    chosen_hero_index = choose_hero()
    hero_name = list(heroes.keys())[chosen_hero_index]
    hero_stats = heroes[hero_name]
    player_hero = hero(hero_name, hero_stats['health'], hero_stats['attack'], hero_stats['defense'])
    player_hero.display_stats()
    # Add more game logic here
    return menu.menu_on_login()

def fight():
    pass

def main():
    menu.main_menu()

    
if __name__ == "__main__":
    main()