print("PROGRAM STARTED")

import time
import os
import sys
import json

SETTINGS_FILE = "settings.json"

def load_settings():
    global settings
    try:
        with open(SETTINGS_FILE, "r") as f:
            settings = json.load(f)
            success("Settings loaded successfully.")
    except FileNotFoundError:
        success("No settings file found. Using default settings.")
    except json.JSONDecodeError:
        error("Settings file is corrupted. Using default settings.")
def save_settings():
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

from colorama import Fore, Style, init
init(autoreset=True) 

from enum import Enum, auto

class MenuState(Enum):
    MAIN = auto()
    SETTINGS = auto()
    CONFIRM_QUIT = auto()
    GAME = auto()
    PAUSE = auto()
    QUIT = auto()


# ============= Colors =============
RESET = "\033[0m"

RED = "\033[31m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"

#========= Color Message Helpers =========#
def error(text):
    print(f"{RED}Error: {text}{RESET}")

def success(text):
    print(f"{GREEN}{text}{RESET}")

def title(text):
    print(f"{CYAN}{text}{RESET}")

    def error(text):
        print(f"{RED}Error: {text}{RESET}")

    def success(text):
        print(f"{GREEN}{text}{RESET}")
 

# ------------- Settings Dictionary ------------- #
settings = {
    "volume": 50,
    "graphics": "Medium",
    "controls": "Keyboard"
}

# ---------------- Start Game ---------------- #
def start_game():
    print("You selected to start the game. Starting game...")

    # loading animation
    for i in range(5):
        print(YELLOW + "Loading" + "." * (i % 4) + RESET)
        time.sleep(0.4)
        # os.system('cls' if os.name == 'nt' else 'clear')

    success("Game Loaded! (Pretend game is running...)")


# ---------------- Options Menu ---------------- #
def options_menu():
        print("\n" + "=" * 40)

        print("\n=== Options Menu ===")
        print(f"{BLUE}1. Volume: {settings['volume']}")
        print(f"{BLUE}2. Graphics: {settings['graphics']}")
        print(f"{BLUE}3. Controls: {settings['controls']}")
        print(f"{BLUE}4. Back to Main Menu")

        choice = input("Select an option: ")

        # -------- Volume Settings -------- #
        if choice == "1":
            try:
                new_volume = int(input("Enter new volume (0-100): "))
                if 0 <= new_volume <= 100: 
                    settings["volume"] = new_volume
                    success(f"Volume updated to {new_volume}!")
                    return MenuState.SETTINGS
                else:
                    error("Volume must be between 0 and 100.")
            except:
                error("Invalid Input. Please enter a number.")
                return MenuState.SETTINGS

        # -------- Graphics Settings -------- #
        elif choice == "2":
            options = ["Low", "Medium", "High", "Ultra"]
            print(YELLOW + "Available Graphics Settings:" + RESET)
            for o in options:
                print("-", o)

            new_graphics = input("Select graphics setting: ").capitalize()

            if new_graphics in options:
                settings["graphics"] = new_graphics
                success("Graphics updated!")
            else:
                error("Invalid graphics setting.")
                return MenuState.SETTINGS

        # -------- Controls Settings -------- #
        elif choice == "3":
            settings["controls"] = "Gamepad" if settings["controls"] == "Keyboard" else "Keyboard"

            print(f"Controls switched to {settings['controls']}!")
            return MenuState.SETTINGS

        # -------- Back to Menu -------- #
        elif choice == "4":
            print(YELLOW + "Returning to Main Menu..." + RESET)
            save_settings()
            return MenuState.MAIN

        else:
            error("Invalid choice. Please select a valid option.")
            return MenuState.SETTINGS

  # ---------------- Game Loop ---------------- #

def game_loop():
    print("\n=== GAME IS NOW RUNNING ===")
    print(GREEN + "At this point, prentend that the game is running." + RESET)
    print(MAGENTA + "[P] Pause Game" + RESET)
    print(CYAN + "[Q] Quit Game" + RESET)

    choice = input(BLUE + "> " + RESET)

    if choice == "p":
        print("Returning to Main Menu...")
        return MenuState.PAUSE
    
    elif choice == "q":
        return MenuState.CONFIRM_QUIT
    
    elif choice == "1":
        return MenuState.GAME
    
    else:
        error(RED + "Invalid choice. Please select a valid option." + RESET)
        return MenuState.GAME

# ---------------- Confirm Quit Menu ---------------- #

def confirm_quit_menu():
    print("\n=== Confirm Quit ===")
    print(BLUE +"Are you sure you want to quit?" + RESET)
    print(BLUE +"1. Yes, I'm sure I want to quit." + RESET)
    print(CYAN +"2. No, I want to stay in the game." + RESET)

    choice = input(YELLOW + "Choose an option: " + RESET)

    if choice == "1":
        save_settings()
        print(GREEN + "Settings have been saved. Goodbye!" )
        return MenuState.QUIT
    
    elif choice == "2":
        print("Returning to Main Menu...")
        return MenuState.MAIN
    
    else:
        error("Invalid choice. Please select a valid option.")
        return MenuState.CONFIRM_QUIT
# ---------------- Main Menu ---------------- #
def main_menu():

        print("\n" + "=" * 40)    
        print(Fore.CYAN + "=== Main Menu ===")
        print(Fore.YELLOW + "1. Start Game")
        print(Fore.YELLOW + "2. Load Game")
        print(Fore.YELLOW + "3. Settings")
        print(Fore.YELLOW + "4. Credits")
        print(Fore.YELLOW + "5. Quit")

        choice = input(Fore.GREEN + "Choose an option: ")

        if choice == "1":
            start_game()
            return MenuState.GAME
        
        elif choice == "2":
            print("Loading game... (Feature not implemented)")
            return MenuState.MAIN
        
        elif choice == "3":
            return MenuState.SETTINGS
        
        elif choice == "4":
            print("This game was developed by Brandon Herrera. Thanks so much for playing!")
            return MenuState.MAIN

        elif choice == "5":
            return MenuState.CONFIRM_QUIT
        
        else:
            error("Invalid choice. Please select a valid option.")
            return MenuState.MAIN
        
# ============= Pause Menu ============= #
def pause_menu():
    print("\n=== GAME IS PAUSED ===")
    print(GREEN + "1. Resume Game" + RESET)
    print(MAGENTA + "2. Return to Main Menu" + RESET)
    print(CYAN + "3. Quit Game" + RESET)

    choice = input(BLUE + "Choose an option: " + RESET)

    if choice == "1":
        print(GREEN + "Resuming game..." + RESET)
        return MenuState.GAME
    
    elif choice == "2":
        print(MAGENTA + "Returning to Main Menu..." + RESET)
        return MenuState.MAIN
    
    elif choice == "3":
        return MenuState.CONFIRM_QUIT
    
    else:
        error(RED + "Invalid choice. Please select a valid option." + RESET)
        return MenuState.PAUSE

# Start program

STATE_HANDLERS = {
    MenuState.MAIN: main_menu,
    MenuState.SETTINGS: options_menu,
    MenuState.CONFIRM_QUIT: confirm_quit_menu,
    MenuState.GAME: game_loop,
    MenuState.PAUSE: pause_menu,
}
load_settings()

current_state = MenuState.MAIN

print("Entering main loop with state:", current_state)

while current_state != MenuState.QUIT:
    try:
        current_state = STATE_HANDLERS[current_state]()
    except KeyError:
        raise RuntimeError(f"No handler for state: {current_state}")

print("Exiting game. Goodbye!")




