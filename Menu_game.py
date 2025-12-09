import time 
import os

# ------------- Settings Dictionary ------------- #
settings = {
"volume": 50,
"graphics": "Medium",
"controls": "Keyboard"
}

print("=== Main Menu ===") 
print("1. Start Game")
print("2. Options")
print("3. Quit")

choice = input("Select an option: ")

if choice == "1":
    print("Starting game...")
elif choice == "2":
    print("Opening options...") 
elif choice == "3":
    print("Quitting game...")   
else:
    print("Invalid choice. Please select a valid option.")

running = True 

while running: 
    print("\n=== Main Menu ===")
    print("1. Start Game")
    print("2. Options")
    print("3. Quit")

    choice = input("Select an option: ")

def start_game():
    print("You selected to start the game. Starting game...")

    # loading animation
for i in range(5):
    print("Loading" + "." * (i % 4))
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Game Loaded! (Pretend game is running...)")

    # ---------------- Options Menu ---------------- #

def options_menu():
    while True:
        print("\n=== Options Menu ===")
        print(f"1. Volume {settings['volume']}")
        print(f"2. Graphics {settings[ 'graphics']}")
        print(f"3. Controls: {settings[ 'controls']}")
        print("4. Back to Main Menu")

        choice = input("Select an option: ")

#---------------- Volume Settings ---------------- #
    if choice == "1":
        try:
            new_volume = int(input("Enter new volume (0-100): "))
            if 0 <= new_volume <= 100:
                settings["volume"] = new_volume
                print(f"Volume updated to {new_volume}!")
            else:
                print("Volume must be between 0 and 100.")
        except:
            print("Invalid Input. Please enter a number between 0 and 100.")    

#---------------- Graphics Settings ---------------- #
    elif choice == "2":
       options = ["low", "medium", "high", "ultra"]
       print("Available Graphics Settings:")
       for o in options:
           print("-",o)

    new_graphics = input("Select graphics setting: ").capitalize() 

    if new_graphics in options:
        settings["graphics"] = new_graphics
        print("Graphics updated!")
    else:
        print("Invalid graphics setting.")

       

#---------------- Controls Settings ---------------- #
elif choice == "3":
if settings["controls"] == "Keyboard":
    settings["controls"] = "Gamepad"
else:
    settings["controls"] = "Keyboard"

    print(f"Controls switched to {settings['controls']}!")


 #---------------- Back to Main Menu ---------------- #           
elif choice == "4":
print("Returning to Main Menu...")
break 

else:
print("Invalid choice. Please select a valid option.") 


#---------------- Main Menu Loop ---------------- # 

def main_menu():
    running = True

    while running:
        print("\n=== Main Menu ===")
        print("1. Start Game")
        print("2. Options")
        print("3. Quit")

        choice = input("Select an option: ")

        if choice == "1":
            start_game()
        elif choice == "2":
            options_menu()
        elif choice == "3":
            print("Quitting game...")
            running = False
        else:
            print("Invalid choice. Please select a valid option.")


# Start the program
main_menu()
