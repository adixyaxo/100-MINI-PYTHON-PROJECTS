import random 
import pandas as pd
import openpyxl as oxl

global login_status
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


# Defining stages with help of monsters and bosses 

stage = {
    1: {"monsters": monsters["Goblin"], "boss": monster_bosses["Goblin King"]},
    2: {"monsters": monsters["Orc"], "boss": monster_bosses["Orc King"]},
    3: {"monsters": monsters["Dragon"], "boss": monster_bosses["Dragon King"]}
}

waves = {
    1: 3,
    2: 4,
    3: 5
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
    def __init__(self, name, health, attack, defense, items_show=None): # used none instead of default {} to avoid mutable default argument issue . The Problem: In Python, if you use {} as a default argument, every single hero you create will share the exact same inventory. If the Knight drinks a potion, the Archer loses one too!
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
        print(f"\n{'='*50}")
        print(f"Hero: {self.name}")
        print(f"{'='*50}")
        print(f"Health:  {self.health}")
        print(f"Attack:  {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Items:   {self.items_show}")
        print(f"{'='*50}\n")
  
class monster:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense 
        
class monster_boss:
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
    global login_status
    new_old = input("Are you a new user? (yes/no): ").strip().lower()
    
    if new_old == 'yes':
        user_data = pd.DataFrame({'Username': [username], 'Password': [password], 'Stage' : [1], 'Coins' : [0]})
        user_data.to_excel(f"{username}_data.xlsx", index=False)
        print("\n✓ User registered successfully.\n")
        login_status = True
        return True
    elif new_old != 'no':
        print("Invalid input. Please enter 'yes' or 'no'.")
        return login(username, password)
    
    try:
        df = pd.read_excel(f"{username}_data.xlsx") # TypeError: 'pandas.core.frame.DataFrame' object does not support the context manager protocol (missed __exit__ method)
        stored_password = df.at[0, 'Password']
        if stored_password == password:
            print("\n✓ Login successful.\n")
            login_status = True
            global current_user
            current_user = user(username, password, df.at[0, 'Stage'], df.at[0, 'Coins'])
            return True
        else:
            print("\n✗ Incorrect password.\n")
            return False
    except FileNotFoundError:
        print("\n✗ User not found.\n")
        return False
    
def logout():
    global login_status
    login_status = False

def choose_hero():
    print(f"\n{'='*60}")
    print("CHOOSE YOUR HERO")
    print(f"{'='*60}\n")
    
    for i, (hero_name, hero_stats) in enumerate(heroes.items(), start=1):
        print(f"{i}. {hero_name}")
        print(f"   {hero_stats['summary']}")
        print(f"   ├─ Health: {hero_stats['health']}")
        print(f"   ├─ Attack: {hero_stats['attack']}")
        print(f"   └─ Defense: {hero_stats['defense']}\n")
    
    choice = input("Choose your hero (number or name): ").strip().lower()

    if choice == '1' or choice == "knight king" or choice == "knight" or choice == "knightking":
        print("\n✓ You have chosen Knight King!")
        print("   Tip: Knights have balanced stats, making them versatile in battle.\n")
        return 0
    elif choice == '2' or choice == "archer king" or choice == "archer" or choice == "archerking":
        print("\n✓ You have chosen Archer King!")
        print("   Tip: Archers have high attack power and low defense.\n")
        return 1
    elif choice == '3' or choice == "bomber king" or choice == "bomber" or choice == "bomberking":
        print("\n✓ You have chosen Bomber King!")
        print("   Tip: Bombers have high attack power and moderate defense.\n")
        return 2
    else:
        print("\n✗ Invalid choice. Please choose a valid hero number.\n")
        return choose_hero()
    
class game_info:
    @staticmethod
    def about_game():
        print(f"\n{'='*60}")
        print("ABOUT THE GAME")
        print(f"{'='*60}\n")
        print("This is a Text-Based RPG Game where you can:")
        print("  • Choose from unique heroes")
        print("  • Fight monsters and earn coins")
        print("  • Progress through challenging stages")
        print("  • Use items to enhance your abilities\n")
        print("Each hero has unique stats and abilities.")
        print("Use items wisely to maximize your potential!\n")
        print(f"{'-'*60}")
        print("GAME INFO MENU:")
        print(f"{'-'*60}")
        print("1. Return to main menu")
        print("2. How to Play")
        print("3. Game Rules")
        print("4. Game Tips")
        print("5. Heroes Info")
        print("6. Monsters Info")
        print("7. Monster Bosses Info")
        print(f"{'-'*60}\n")
        
        info_choice = input("Choose an option: ").strip()
        
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
        print(f"\n{'='*60}")
        print("HOW TO PLAY")
        print(f"{'='*60}\n")
        print("1. Login or register as a new user")
        print("2. Choose your hero from the available options")
        print("3. Fight monsters to earn coins and progress through stages")
        print("4. Use items to heal, boost defense, or increase attack power")
        print("5. Advance through stages by defeating monsters and bosses")
        print("6. Enjoy the game and have fun!\n")
        print(f"{'-'*60}\n")
    
    @staticmethod
    def game_rules():
        print(f"\n{'='*60}")
        print("GAME RULES")
        print(f"{'='*60}\n")
        print("1. Each hero has unique stats: health, attack, and defense")
        print("2. Monsters have their own stats and can be defeated to earn coins")
        print("3. Use items strategically to enhance your hero's abilities")
        print("4. Progress through stages by defeating monsters and bosses")
        print("5. Save your progress by logging in with your username and password\n")
        print(f"{'-'*60}\n")
    
    @staticmethod
    def game_tips():
        print(f"\n{'='*60}")
        print("GAME TIPS")
        print(f"{'='*60}\n")
        print("1. Choose a hero that suits your playstyle")
        print("2. Use items wisely to maximize their benefits")
        print("3. Pay attention to monster stats and plan your attacks accordingly")
        print("4. Save your progress frequently by logging in")
        print("5. Experiment with different strategies to defeat tougher monsters\n")
        print(f"{'-'*60}\n")
        
    @staticmethod
    def heros_info():
        print(f"\n{'='*60}")
        print("HERO INFORMATION")
        print(f"{'='*60}\n")
        
        for hero_name, hero_stats in heroes.items():
            print(f"{hero_name}")
            print(f"  {hero_stats['summary']}")
            print(f"  ├─ Health: {hero_stats['health']}")
            print(f"  ├─ Attack: {hero_stats['attack']}")
            print(f"  └─ Defense: {hero_stats['defense']}\n")
        
        print(f"{'-'*60}\n")

    @staticmethod
    def monsters_info():
        print(f"\n{'='*60}")
        print("MONSTER INFORMATION")
        print(f"{'='*60}\n")
        
        for monster_name, monster_stats in monsters.items():
            print(f"{monster_name}")
            print(f"  ├─ Health: {monster_stats['health']}")
            print(f"  ├─ Attack: {monster_stats['attack']}")
            print(f"  └─ Defense: {monster_stats['defense']}\n")
        
        print(f"{'-'*60}\n")
        
    @staticmethod
    def monster_bosses_info():
        print(f"\n{'='*60}")
        print("MONSTER BOSSES INFORMATION")
        print(f"{'='*60}\n")
        
        for boss_name, boss_stats in monster_bosses.items():
            print(f"{boss_name}")
            print(f"  ├─ Health: {boss_stats['health']}")
            print(f"  ├─ Attack: {boss_stats['attack']}")
            print(f"  └─ Defense: {boss_stats['defense']}\n")
        
        print(f"{'-'*60}\n")
        
class menu:
    @staticmethod
    def main_menu():
        global login_status
        
        if login_status == True:
            return menu.menu_on_login()
        else:
            print(f"\n{'='*60}")
            print("WELCOME TO THE TEXT-BASED RPG GAME")
            print(f"{'='*60}\n")
            print("1. Login")
            print("2. Learn about game")
            print("3. Exit")
            print(f"{'-'*60}\n")
            
            choice = input("Choose an option: ").strip()
            
            if choice == '1':
                login(input("\nEnter your username: "), input("Enter your password: "))
                menu.main_menu()
            elif choice == '2':
                game_info.about_game()
            elif choice == '3':
                print("\nExiting the game. Goodbye!\n")
                exit()
            else:
                print("\n✗ Invalid choice. Please choose a valid option.\n")
                return menu.main_menu()
    
    @staticmethod
    def menu_on_login():
        if not login_status:
            print("You need to login first.")
            return menu.main_menu()
        
        print(f"\n{'='*60}")
        print("MAIN MENU")
        print(f"{'='*60}\n")
        print("1. Start Game")
        print("2. Game Info")
        print("3. Your Stats")
        print("4. Logout")
        print(f"{'-'*60}\n")
        
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            return start_game()
        elif choice == '2':
            return game_info.about_game()
        elif choice == '3':
            print("\nYour Stats feature is under development.\n")
            return menu.menu_on_login()
        elif choice == '4':
            logout()
            print("✓ You have been logged out.\n")
            return menu.main_menu()
        else:
            print("\n✗ Invalid choice. Please choose a valid option.\n")
            return menu.menu_on_login()

player_hero = None
user_stage = 1

def start_game():
    global player_hero
    global user_stage
    print("\n" + "="*60)
    print("GAME STARTED!")
    print("="*60 + "\n")
    
    user_stage = current_user.stage
    print(f"✓ Your Stage {user_stage}.\n")
    
    chosen_hero_index = choose_hero()
    hero_name = list(heroes.keys())[chosen_hero_index]
    hero_stats = heroes[hero_name]
    player_hero = hero(hero_name,int(hero_stats['health'])*user_stage, int(hero_stats['attack'])*user_stage, int(hero_stats['defense'])*user_stage)
    player_hero.display_stats()
    

    return menu.menu_on_login()

def stage():
    global user_stage
    for stage_no,dict in stage.items():
        if stage_no < user_stage:
            continue
        print(f"--- Stage {stage_no} ---\n")
        for i in range(1,4): # 3 waves per stage
            print(f"Wave {i}:\n")
            waves(i,stage_no)
        bossfight(stage_no)
    user_stage += 1
    current_user.stage = user_stage

def waves(wave_number,stage):
    global player_hero
    no_of_monsters = waves[wave_number]*stage
    damage = monsters["Goblin"]["attack"] - player_hero.defense
    
def bossfight(stage):
    global player_hero
    boss = monster_boss("Boss", monster_bosses[list(monster_bosses.keys())[stage-1]]["health"], monster_bosses[list(monster_bosses.keys())[stage-1]]["attack"], monster_bosses[list(monster_bosses.keys())[stage-1]]["defense"])
    fight(boss)
    print(f"\n✓ You have cleared Stage {stage}!\n")

def fight(_monster):
    global player_hero
    print(f"\n{_monster.name} appears!\n")
    while _monster.health > 0 and player_hero.health > 0:
        damage_to_monster = player_hero.attack - _monster.defense
        _monster.health -= damage_to_monster
        print(f"You dealt {damage_to_monster} damage to {_monster.name}. {_monster.name}'s health is now {_monster.health}.")
        if _monster.health <= 0:
            print(f"\n✓ You have defeated {_monster.name}!\n")
            return 1

        damage_to_hero =  _monster.attack - player_hero.defense
        player_hero.health -= damage_to_hero
        print(f"{_monster.name} dealt {damage_to_hero} damage to you. Your health is now {player_hero.health}.")

        if player_hero.health <= 0:
            print("\n✗ You have been defeated! Game Over.\n")
            return menu.main_menu()

def main():
    menu.main_menu()

    
if __name__ == "__main__":
    main()