import time
import os
import sys
print(sys.executable)
from colorama import Fore, Style, init
init(autoreset=True) 


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
    while True:
        print("\n=== Options Menu ===")
        print(f"{BLUE}1. Volume:{RESET} {settings['volume']}")
        print(f"{BLUE}2. Graphics:{RESET} {settings['graphics']}")
        print(f"{BLUE}3. Controls: {RESET}{settings['controls']}")
        print(F"{BLUE}4. Back to Main Menu{RESET}")

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

        # -------- Controls Settings -------- #
        elif choice == "3":
            if settings["controls"] == "Keyboard":
                settings["controls"] = "Gamepad" if settings ["controls"] == "Keyboard" else "Keyboard"
            else:
                settings["controls"] = "Keyboard"

            print(f"Controls switched to {settings['controls']}!")

        # -------- Back to Menu -------- #
        elif choice == "4":
            print(YELLOW + "Returning to Main Menu..." + RESET)
            break

        else:
            error("Invalid choice. Please select a valid option.")


# ---------------- Main Menu ---------------- #
def main_menu():
    running = True

    while running:
        print(Fore.CYAN + "\n=== Main Menu ===")
        print(Fore.YELLOW + "1. Start Game")
        print(Fore.YELLOW + "2. Load Game")
        print(Fore.YELLOW + "3. Settings")
        print(Fore.YELLOW + "4. Credits")
        print(Fore.YELLOW + "5. Quit")

        choice = input(Fore.GREEN + "Choose an option: ")

        if choice == "1":
            print(Fore.MAGENTA + "Starting Game...")
        elif choice == "2":
            print(Fore.MAGENTA + "Loading game (not implemented yet)...")
        elif choice == "3":
            print(Fore.MAGENTA + "Opening Settings...")
        elif choice == "4":
            print(Fore.MAGENTA + "This game was developed by Brandon Herrera. Thanks for playing!")
        elif choice == "5":
            print(Fore.RED + "Quitting game. Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please select a valid option.")


# Start program
main_menu()

