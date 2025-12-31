print("PROGRAM STARTED")

import time
import os
import sys
import json
import random

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

audio_system = {
    "state": "normal",
    "recovery_timer": 0.0
}

# ============ Game State ==========
game_data = {
    "ticks": 0,
    "running": True
}

# ========== Debug Flagging section ===========
debug_overlay_enabled = False

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

settings_return_state = MenuState.MAIN

GRAPHICS_FPS = {
    "Low": 60,
    "Medium" : 45,
    "High": 30, 
    "Ultra": 20
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
        global settings_return_state

        print("\n=== Options Menu ===")
        print(f"{BLUE}1. Volume: {settings['volume']}")
        print(f"{BLUE}2. Graphics: {settings['graphics']}")
        print(f"{BLUE}3. Controls: {settings['controls']}")
        print(f"{BLUE}4. Back to Main Menu")

        choice = input("Select an option: ")

        print("(In-Game Settings)" if settings_return_state == MenuState.PAUSE else "(Main Menu Settings)")

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
                apply_settings()
                return MenuState.SETTINGS
            else:
                error("Invalid graphics setting.")
                return MenuState.SETTINGS

        # -------- Controls Settings -------- #
        elif choice == "3":
            settings["controls"] = "Gamepad" if settings["controls"] == "Keyboard" else "Keyboard"

            print(f"Controls switched to {settings['controls']}!")
            settings_return_state = MenuState.MAIN
            return MenuState.SETTINGS

        # -------- Back to Menu -------- #
        elif choice == "4":
            print(YELLOW + "Returning to Main Menu..." + RESET)
            save_settings()
            return settings_return_state

        else:
            error("Invalid choice. Please select a valid option.")
            return MenuState.SETTINGS

# ---------------- Apply settings function ---------------- #
GRAPHICS_FPS = {
    "Low": 60,
    "Medium": 45,
    "High": 30,
    "Ultra": 20
}

SPIKE_CHANCE = {
    "Low": 0.05,
    "Medium": 0.15,
    "High": 0.30,
    "Ultra": 0.45
}

GRAPHICS_STRESS = {
    "Low":{
        "base_jitter": 0.0,
        "spike_chance": 0.01,
        "spike_penalty": 0.0,
    },
    "Medium": {
        "base_jitter": 0.005,
        "spike_chance": 0.05,
        "spike_penalty": 0.01,
    },
    "High": {
        "base_jitter": 0.01,
        "spike_chance": 0.05,
        "spike_penalty": 0.01,
    },
    "Ultra": {
        "base_jitter": 0.02,
        "spike_chance": 0.2,
        "spike_penalty": 0.06,
    },
}

def apply_settings():
    graphics = settings["graphics"].strip().capitalize()
    fps = GRAPHICS_FPS.get(settings["graphics"], 30)

    print(MAGENTA + f"[Graphics] Quality: {settings['graphics']}" + RESET)
    print(CYAN + f"[Performance] Target FPS: {fps}" + RESET)

    return fps

def get_volume_description():

    if settings["volume"] >= 75:
        volume_desc = "LOUD"
    elif settings["volume"] >= 40:
        volume_desc = "NORMAL"
    else:
        volume_desc = "QUIET"

    graphics_level = settings["graphics"]

    return volume_desc, graphics_level

def maybe_apply_fps_spike(base_fps):
    spike_chance = {
        "Low": 0.05,
        "Medium": 0.15,
        "High": 0.30,
        "Ultra": 0.45
    }.get(settings["graphics"], 0.2)


    # 20% chance to spike
    if random.random() < spike_chance:
        spike_amount = random.randint(10, 20)
        spiked_fps = max(5, fps - spike_amount)
        return spiked_fps, True

        print(
            RED +
            f"[Performance Warning] FPS spike! ({fps} → {spiked_fps})"
            + RESET
        )

        return spiked_fps

    return base_fps, False


# ------------------ Audio Section ---------------- #
def get_audio_state(current_fps, base_fps, delta_time):
    stress_ratio = current_fps / base_fps
    volume = settings["volume"]

    # Volume override
    if volume == 0:
        audio_system["state"] = "normal"
        audio_system["recovery_timer"] = 0.0
        return "🔇 VOLUME MUTED"

    # --- Severe degradation ---
    if stress_ratio < 0.6:
        audio_system["state"] = "crackle"
        audio_system["recovery_timer"] = 0.0

        if stress_ratio < 0.4:
            return "📢📢📢 SEVERE AUDIO CRACKLE (Buffer collapse)"
        else:
            return "📢📢 HEAVY AUDIO CRACKLE"

    # --- Begin recovery ---
    if audio_system["state"] == "crackle":
        audio_system["state"] = "recovering"
        audio_system["recovery_timer"] = 0.0
        return "🟡 Audio stabilizing..."

    # --- Recovering ---
    if audio_system["state"] == "recovering":
        audio_system["recovery_timer"] += delta_time

        if audio_system["recovery_timer"] >= 2.0:
            audio_system["state"] = "normal"
            return "🟢 Audio fully recovered"

        return "🟡 Audio recovering..."

    # --- Normal ---
    if volume < 30:
        return "🔈 Audio muffled"

    if volume < 70:
        return "🔊 Normal audio"

    return "🔊 LOUD & CLEAR"

# ---------------- Debug Overlay Function --------------
def draw_debug_overlay(current_fps, base_fps):
    stress_ratio = current_fps / base_fps

    if stress_ratio < 0.6:
        gpu_state = "HIGH"
    elif stress_ratio < 0.8:
        gpu_state = "MEDIUM"
    else:
        gpu_state = "LOW"

    print(MAGENTA + "\n [DEBUG] " + RESET)
    print(f"Graphics Preset: {settings['graphics']}")
    print(f"Target FPS: {base_fps}")
    print(f"Current FPS: {current_fps}")
    print(f"GPU Stress: {gpu_state}")
    print(f"Audio State: {audio_system['state'].upper()}")
    print(MAGENTA + "====================\n" + RESET)



  # ---------------- Game Loop ---------------- #
fps = apply_settings()
frame_time = 1 / fps

def game_loop():
    
    volume_desc = get_volume_description()
    graphics_level = settings["graphics"]
    global debug_overlay_enabled 

    game_data["ticks"] += 1

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\n=== GAME IS NOW RUNNING ===")

    print(
        GREEN +
        f"Resumed with {settings['graphics']} graphics ({fps} FPS)"
        +RESET
    )

    if graphics_level in ("High", "Ultra"):
        print(YELLOW + f"Tick: {game_data['ticks']}" + RESET)
        print(CYAN + " Fancy Hud Enabled" + RESET)

    print(GREEN + f"Volume Level: {volume_desc}" +RESET)
    print(WHITE + "At this point, prentend that the game is running." + RESET)


    print( YELLOW + "[P] Pause Game" + RESET)
    print(CYAN + "[Q] Quit Game" + RESET)

    for frame in range(20):
        current_fps, spiked = maybe_apply_fps_spike(fps)
        frame_time = 1 / current_fps
        delta_time = frame_time

        audio_state = get_audio_state(current_fps, fps, delta_time)

        print(
            YELLOW +
            f"Rendering frame {frame + 1} at {current_fps} FPS..."
            + ("GPU SPIKE!" if spiked else "")
            + RESET
        )

        if debug_overlay_enabled:
            draw_debug_overlay(current_fps, fps)

            time.sleep(frame_time)


        if "SEVERE" in audio_state:
            print(RED + f"Audio: {audio_state}" + RESET)
        elif "HEAVY" in audio_state:
            print(YELLOW + f"Audio: {audio_state}" + RESET)
        elif "LIGHT" in audio_state:
            print(CYAN + f"Audio: {audio_state}" + RESET)
        else:
            print(GREEN + f"Audio: {audio_state}" + RESET)
        time.sleep(frame_time)

    choice = input(BLUE + "> " + RESET).lower()

    if choice == "d":
        debug_overlay_enabled = not debug_overlay_enabled
        print(WHITE + "[D] Toggle Debug Overlay" + RESET)
        return MenuState.GAME 

    if choice == "p":
        print("Returning to Main Menu...")
        return MenuState.PAUSE
    
    elif choice == "q":
        return MenuState.CONFIRM_QUIT
    
    elif choice == "1":
        game_data["ticks"] = 0
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
    global settings_return_state

    print("\n=== GAME IS PAUSED ===")
    print(GREEN + "1. Resume Game" + RESET)
    print(CYAN + "2. Settings" + RESET)
    print(MAGENTA + "3. Return to main Menu" + RESET)
    print(RED + "4. Quit Game" + RESET)

    choice = input(BLUE + "Choose an option: " + RESET)

    if choice == "1":
        print(GREEN + "Resuming game..." + RESET)
        return MenuState.GAME
    
    elif choice == "2":
        print(MAGENTA + "Returning to Main Menu..." + RESET)
        settings_return_state = MenuState.PAUSE
        return MenuState.SETTINGS
    
    elif choice == "3":
        return MenuState.MAIN
    
    elif choice == "4":
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
    MenuState.CONFIRM_QUIT: confirm_quit_menu,
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




