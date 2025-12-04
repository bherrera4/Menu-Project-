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

    if choice == "1":
        print("You selected to star the game. Loading level...")
        # Here you would add the code to start the game
    elif choice == "2":
        print("Options: Volume, Graphics, Controls")
        # Here you would add the code to display and modify options
    elif choice == "3":
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice. Please select a valid option.")
