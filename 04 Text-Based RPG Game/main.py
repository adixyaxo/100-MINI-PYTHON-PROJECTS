import random 
import pandas as pd
import keyboard as kb
import openpyxl as oxl

global login_status
login_status = False

heroes_dict = {
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

monsters_dict = {
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

monster_bosses_dict = {
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

stage_dict = {
    1: {"monsters": monsters_dict["Goblin"], "boss": monster_bosses_dict["Goblin King"]},
    2: {"monsters": monsters_dict["Orc"], "boss": monster_bosses_dict["Orc King"]},
    3: {"monsters": monsters_dict["Dragon"], "boss": monster_bosses_dict["Dragon King"]}
}

waves_dict = {
    1: 3,
    2: 4,
    3: 5
}

items_dict = {
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
    def __init__(self, name, health, attack, defense, items_show=None):
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
        print(f"\n{'█'*60}")
        print(f"║ {'HERO STATS'.center(56)} ║")
        print(f"{'█'*60}")
        print(f"║ Hero Name:  {self.name.ljust(44)} ║")
        print(f"║ Health:     {str(self.health).ljust(44)} ║")
        print(f"║ Attack:     {str(self.attack).ljust(44)} ║")
        print(f"║ Defense:    {str(self.defense).ljust(44)} ║")
        print(f"{'█'*60}\n")
  
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
        df = pd.read_excel(f"{username}_data.xlsx")
        stored_password = df.at[0, 'Password']
        if stored_password == password:
            print("\n✓ Login successful.\n")
            login_status = True
            global current_user
            try:
                current_user = user(username, password, df.at[0, 'Stage'], df.at[0, 'Coins'])
            except KeyError:
                current_user = user(username, password)
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
    print(f"\n{'█'*60}")
    print(f"║ {'CHOOSE YOUR HERO'.center(56)} ║")
    print(f"{'█'*60}\n")
    
    for i, (hero_name, hero_stats) in enumerate(heroes_dict.items(), start=1):
        print(f"   {i}. {hero_name}")
        print(f"      {hero_stats['summary']}")
        print(f"      ├─ Health:  {hero_stats['health']}")
        print(f"      ├─ Attack:  {hero_stats['attack']}")
        print(f"      └─ Defense: {hero_stats['defense']}\n")
    
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
        print(f"\n{'█'*60}")
        print(f"║ {'ABOUT THE GAME'.center(56)} ║")
        print(f"{'█'*60}\n")
        print("This is a Text-Based RPG Game where you can:")
        print("  • Choose from unique heroes")
        print("  • Fight monsters and earn coins")
        print("  • Progress through challenging stages")
        print("  • Use items to enhance your abilities\n")
        print("Each hero has unique stats and abilities.")
        print("Use items wisely to maximize your potential!\n")
        print(f"{'═'*60}")
        print(f"║ {'GAME INFO MENU'.center(56)} ║")
        print(f"{'═'*60}")
        print("║                                                            ║")
        print("║  1. Return to main menu                                    ║")
        print("║  2. How to Play                                            ║")
        print("║  3. Game Rules                                             ║")
        print("║  4. Game Tips                                              ║")
        print("║  5. Heroes Info                                            ║")
        print("║  6. Monsters Info                                          ║")
        print("║  7. Monster Bosses Info                                    ║")
        print("║                                                            ║")
        print(f"{'═'*60}\n")
        
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
        print(f"\n{'█'*60}")
        print(f"║ {'HOW TO PLAY'.center(56)} ║")
        print(f"{'█'*60}\n")
        print("  1. Login or register as a new user")
        print("  2. Choose your hero from the available options")
        print("  3. Fight monsters to earn coins and progress through stages")
        print("  4. Use items to heal, boost defense, or increase attack power")
        print("  5. Advance through stages by defeating monsters and bosses")
        print("  6. Enjoy the game and have fun!\n")
        print(f"{'═'*60}\n")
    
    @staticmethod
    def game_rules():
        print(f"\n{'█'*60}")
        print(f"║ {'GAME RULES'.center(56)} ║")
        print(f"{'█'*60}\n")
        print("  1. Each hero has unique stats: health, attack, and defense")
        print("  2. Monsters have their own stats and can be defeated to earn coins")
        print("  3. Use items strategically to enhance your hero's abilities")
        print("  4. Progress through stages by defeating monsters and bosses")
        print("  5. Save your progress by logging in with your username and password\n")
        print(f"{'═'*60}\n")
    
    @staticmethod
    def game_tips():
        print(f"\n{'█'*60}")
        print(f"║ {'GAME TIPS'.center(56)} ║")
        print(f"{'█'*60}\n")
        print("  1. Choose a hero that suits your playstyle")
        print("  2. Use items wisely to maximize their benefits")
        print("  3. Pay attention to monster stats and plan your attacks accordingly")
        print("  4. Save your progress frequently by logging in")
        print("  5. Experiment with different strategies to defeat tougher monsters\n")
        print(f"{'═'*60}\n")
        
    @staticmethod
    def heros_info():
        print(f"\n{'█'*60}")
        print(f"║ {'HERO INFORMATION'.center(56)} ║")
        print(f"{'█'*60}\n")
        
        for hero_name, hero_stats in heroes_dict.items():
            print(f"   {hero_name}")
            print(f"   {hero_stats['summary']}")
            print(f"   ├─ Health:  {hero_stats['health']}")
            print(f"   ├─ Attack:  {hero_stats['attack']}")
            print(f"   └─ Defense: {hero_stats['defense']}\n")
        
        print(f"{'═'*60}\n")

    @staticmethod
    def monsters_info():
        print(f"\n{'█'*60}")
        print(f"║ {'MONSTER INFORMATION'.center(56)} ║")
        print(f"{'█'*60}\n")
        
        for monster_name, monster_stats in monsters_dict.items():
            print(f"   {monster_name}")
            print(f"   ├─ Health:  {monster_stats['health']}")
            print(f"   ├─ Attack:  {monster_stats['attack']}")
            print(f"   └─ Defense: {monster_stats['defense']}\n")
        
        print(f"{'═'*60}\n")
        
    @staticmethod
    def monster_bosses_info():
        print(f"\n{'█'*60}")
        print(f"║ {'MONSTER BOSSES INFORMATION'.center(56)} ║")
        print(f"{'█'*60}\n")
        
        for boss_name, boss_stats in monster_bosses_dict.items():
            print(f"   {boss_name}")
            print(f"   ├─ Health:  {boss_stats['health']}")
            print(f"   ├─ Attack:  {boss_stats['attack']}")
            print(f"   └─ Defense: {boss_stats['defense']}\n")
        
        print(f"{'═'*60}\n")
        
class menu:
    @staticmethod
    def main_menu():
        global login_status
        
        if login_status == True:
            return menu.menu_on_login()
        else:
            print(f"\n{'█'*60}")
            print(f"║ {'WELCOME TO TEXT-BASED RPG GAME'.center(56)} ║")
            print(f"{'█'*60}")
            print("║                                                            ║")
            print("║  1. Login                                                  ║")
            print("║  2. Learn about game                                       ║")
            print("║  3. Exit                                                   ║")
            print("║                                                            ║")
            print(f"{'═'*60}\n")
            
            choice = input("Choose an option: ").strip()
            
            if choice == '1':
                login(input("\nEnter your username: "), input("Enter your password: "))
                menu.main_menu()
            elif choice == '2':
                game_info.about_game()
            elif choice == '3':
                print("\n✓ Exiting the game. Goodbye!\n")
                exit()
            else:
                print("\n✗ Invalid choice. Please choose a valid option.\n")
                return menu.main_menu()
    
    @staticmethod
    def menu_on_login():
        if not login_status:
            print("You need to login first.")
            return menu.main_menu()
        
        print(f"\n{'█'*60}")
        print(f"║ {'MAIN MENU'.center(56)} ║")
        print(f"{'█'*60}")
        print("║                                                            ║")
        print("║  1. Start Game                                             ║")
        print("║  2. Game Info                                              ║")
        print("║  3. Your Stats                                             ║")
        print("║  4. Logout                                                 ║")
        print("║                                                            ║")
        print(f"{'═'*60}\n")
        
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
    print(f"\n{'█'*60}")
    print(f"║ {'GAME STARTED!'.center(56)} ║")
    print(f"{'█'*60}\n")
    
    user_stage = current_user.stage
    print(f"✓ Your Stage: {user_stage}\n")
    
    chosen_hero_index = choose_hero()
    hero_name = list(heroes_dict.keys())[chosen_hero_index]
    hero_stats = heroes_dict[hero_name]
    player_hero = hero(hero_name,int(hero_stats['health'])*user_stage, int(hero_stats['attack'])*user_stage, int(hero_stats['defense'])*user_stage)
    player_hero.display_stats()
    stage_game()
    return menu.menu_on_login()

def stage_game():
    global user_stage
    for stage_no, stage_data in stage_dict.items():
        if stage_no < user_stage:
            continue
        print(f"\n{'═'*60}")
        print(f"║ {'STAGE ' + str(stage_no)}.center(56) ║")
        print(f"{'═'*60}\n")
        for i in range(1,4):
            print(f"┌ WAVE {i} ─────────────────────────────────────────────────┐")
            print(f"└─────────────────────────────────────────────────────────┘\n")
            waves_game(i, stage_no)
            print(f"\n{'─'*60}\n")
        bossfight(stage_no)
        print(f"\n{'█'*60}\n")
    user_stage += 1
    current_user.stage = user_stage

def waves_game(wave_number, stage_no):
    global player_hero
    monster_info = stage_dict[stage_no]["monsters"]
    monster_instance = monster(list(monsters_dict.keys())[list(monsters_dict.values()).index(monster_info)], monster_info["health"], monster_info["attack"], monster_info["defense"])
    no_of_monsters = waves_dict[wave_number]*stage_no
    multi_fight(monster_instance, no_of_monsters)
    
def multi_fight(_monster, no_of_monsters):
    global player_hero
    print(f"⚔️  {no_of_monsters} {_monster.name}(s) appear!\n")
    
    monsters_defeated = 0
    current_monster_health = monsters_dict[_monster.name]["health"]
    
    while no_of_monsters > 0 and player_hero.health > 0:
        print(f"{'─'*60}")
        print(f"│ Remaining: {str(no_of_monsters).ljust(5)} │ Defeated: {str(monsters_defeated).ljust(5)} │ Your HP: {str(player_hero.health).ljust(8)} │")
        print(f"│ Monster HP: {str(current_monster_health).ljust(47)} │")
        print(f"{'─'*60}\n")
        
        user_input = input("Enter to attack | H to heal | S to shield | R to rage | E to exit\n\nYour choice: ").strip().lower()
        
        if user_input == 'e':
            print("\n✗ Exiting to main menu...\n")
            return menu.main_menu()
        
        elif user_input == '' or user_input == 'enter':
            # Normal attack
            damage_to_monster = player_hero.attack - monsters_dict[_monster.name]["defense"]
            current_monster_health -= damage_to_monster
            print(f"\n⚡ You attacked! Dealt {damage_to_monster} damage to {_monster.name}.")
            
        elif user_input == 'h':
            # Heal
            if items_dict["Health Potion"]["available"] > 0:
                items_dict["Health Potion"]["available"] -= 1
                player_hero.item_use(items_dict["Health Potion"])
                print(f"\n💊 You used Health Potion! Health restored by 20. Current HP: {player_hero.health}")
            else:
                print("\n✗ No health potions available!")
                continue
        
        elif user_input == 's':
            # Shield
            if items_dict["Shield"]["available"] > 0:
                items_dict["Shield"]["available"] -= 1
                player_hero.item_use(items_dict["Shield"])
                print(f"\n🛡️  You used Shield! Defense increased by 20. Current DEF: {player_hero.defense}")
            else:
                print("\n✗ No shields available!")
                continue
        
        elif user_input == 'r':
            # Rage
            if items_dict["Rage"]["available"] > 0:
                items_dict["Rage"]["available"] -= 1
                player_hero.item_use(items_dict["Rage"])
                print(f"\n🔥 You used Rage! Attack increased by 20. Current ATK: {player_hero.attack}")
            else:
                print("\n✗ No rage potions available!")
                continue
        else:
            print("\n✗ Invalid input. Please try again.")
            continue
        
        # Check if monster defeated with damage carryover
        if current_monster_health <= 0:
            overflow_damage = abs(current_monster_health)
            while overflow_damage > 0 and no_of_monsters > 0:
                monsters_defeated += 1
                no_of_monsters -= 1
                overflow_damage -= monsters_dict[_monster.name]["health"]
            
            if no_of_monsters > 0:
                current_monster_health = monsters_dict[_monster.name]["health"] - overflow_damage
                print(f"\n✓ Defeated a {_monster.name}! Next monster appears with {current_monster_health} HP!\n")
            else:
                print(f"\n✓ All {monsters_defeated} {_monster.name}(s) defeated!\n")
            continue
        
        # Monster counter attack
        damage_to_hero = monsters_dict[_monster.name]["attack"] - player_hero.defense
        player_hero.health -= damage_to_hero
        print(f"\n💥 {_monster.name} dealt {damage_to_hero} damage to you!\n")
        
        if player_hero.health <= 0:
            print(f"{'█'*60}")
            print(f"║ {'GAME OVER!'.center(56)} ║")
            print(f"{'█'*60}")
            print(f"Monsters defeated: {monsters_defeated}/{monsters_defeated + no_of_monsters}\n")
            return menu.main_menu()
    
    print(f"\n✓ Wave complete! {monsters_defeated} {_monster.name}(s) defeated!\n")
    return monsters_defeated

def bossfight(stage_no):
    global player_hero
    boss_name = list(monster_bosses_dict.keys())[stage_no-1]
    boss_stats = monster_bosses_dict[boss_name]
    boss = monster_boss(boss_name, boss_stats["health"], boss_stats["attack"], boss_stats["defense"])
    print(f"\n{'█'*60}")
    print(f"║ {'BOSS FIGHT!'.center(56)} ║")
    print(f"{'█'*60}\n")
    fight(boss)
    print(f"\n{'█'*60}")
    print(f"║ {'STAGE ' + str(stage_no) + ' CLEARED!'.center(56)} ║")
    print(f"{'█'*60}\n")

def fight(_monster):
    global player_hero
    print(f"⚔️  {_monster.name} appears!\n")
    while _monster.health > 0 and player_hero.health > 0:
        print(f"{'─'*60}")
        print(f"│ {_monster.name} HP: {str(_monster.health).ljust(46)} │")
        print(f"│ Your HP: {str(player_hero.health).ljust(49)} │")
        print(f"{'─'*60}\n")
        print("Press Enter to attack or ESC to return to main menu...")
        event = kb.read_event()
        if event.event_type == kb.KEY_DOWN and event.name == 'esc':
            print("\n✗ Returning to main menu...\n")
            return menu.main_menu()
        damage_to_monster = player_hero.attack - _monster.defense
        _monster.health -= damage_to_monster
        print(f"\n⚡ You dealt {damage_to_monster} damage to {_monster.name}. {_monster.name}'s HP is now {_monster.health}.")
        if _monster.health <= 0:
            print(f"\n✓ You have defeated {_monster.name}!\n")
            return 1

        damage_to_hero =  _monster.attack - player_hero.defense
        player_hero.health -= damage_to_hero
        print(f"\n💥 {_monster.name} dealt {damage_to_hero} damage to you. Your HP is now {player_hero.health}.\n")

        if player_hero.health <= 0:
            print(f"{'█'*60}")
            print(f"║ {'GAME OVER!'.center(56)} ║")
            print(f"{'█'*60}\n")
            return menu.main_menu()

def main():
    menu.main_menu()

    
if __name__ == "__main__":
    main()