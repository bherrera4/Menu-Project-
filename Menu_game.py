print("PROGRAM STARTED")

import time
import os
import sys
print(sys.executable)
from colorama import Fore, Style, init
init(autoreset=True) 

from enum import Enum, auto

class MenuState(Enum):
    MAIN = auto()
    SETTINGS = auto()
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
        os.system('cls' if os.name == 'nt' else 'clear')

    success("Game Loaded! (Pretend game is running...)")


# ---------------- Options Menu ---------------- #
def options_menu():
        print("\n" * 50)

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
            return MenuState.MAIN

        else:
            error("Invalid choice. Please select a valid option.")
            return MenuState.SETTINGS


# ---------------- Main Menu ---------------- #
def main_menu():
    
        print(Fore.CYAN + "\n=== Main Menu ===")
        print(Fore.YELLOW + "1. Start Game")
        print(Fore.YELLOW + "2. Load Game")
        print(Fore.YELLOW + "3. Settings")
        print(Fore.YELLOW + "4. Credits")
        print(Fore.YELLOW + "5. Quit")

        choice = input(Fore.GREEN + "Choose an option: ")

        if choice == "1":
            start_game()
            return MenuState.MAIN
        
        elif choice == "2":
            print("Loading game... (Feature not implemented)")
            return MenuState.MAIN
        
        elif choice == "3":
            return MenuState.SETTINGS
        
        elif choice == "4":
            print("This game was developed by Brandon Herrera. Thanks so much for playing!")
            return MenuState.MAIN

        elif choice == "5":
            return MenuState.QUIT
        
        else:
            error("Invalid choice. Please select a valid option.")
            return MenuState.MAIN


# Start program

current_state = MenuState.MAIN

while current_state != MenuState.QUIT:

    if current_state == MenuState.MAIN:
        current_state = main_menu()

    elif current_state == MenuState.MAIN:
        current_state = options_menu()

        print("Exiting game. Goodbye!")


