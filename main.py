# init stage:

# required packages
required_packages = ['colorama', 'tqdm', 'requests', 'bs4']

for package in required_packages:
    try:
        # Try to import the package. __import__() is used for dynamic imports.
        __import__(package)
    except ImportError:
        print(f"Error: Required package '{package}' is not installed.")
        print(f"Please install it using: pip install {package}")
        exit(1) # Exit with an error code

print("All packages are installed. Proceeding...")

import os 
import webbrowser
import threading 
import sys 
import time
import colorama
from colorama import Fore, Style
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup

# Initialize Colorama for colored text on Windows
colorama.init()

# Function to display the logo
def display_logo():
    file_path = "logo.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(colorama.Fore.LIGHTMAGENTA_EX + content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the logo: {e}")

# Utility function for header
def print_header():
    print(Fore.LIGHTMAGENTA_EX + "="*40)
    print(Fore.LIGHTMAGENTA_EX + "   Project SLVL Game Launcher")
    print(Fore.LIGHTMAGENTA_EX + "="*40 + Style.RESET_ALL)

# Clear screen utility function
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

logs = []

def log(message):
    logs.append(message)

def view_logs_menu():
    clear_screen()
    print_header()
    print(Fore.YELLOW + "REAL-TIME LOGS" + Style.RESET_ALL)
    if not logs:
        print(Fore.WHITE + "No logs yet." + Style.RESET_ALL)
    else:
        for entry in logs[-50:]:  # Show last 50 logs
            print(Fore.WHITE + entry + Style.RESET_ALL)
    input(Fore.YELLOW + "\nPress Enter to return to menu..." + Style.RESET_ALL)

# Function to download and install games
def download_and_install(url, game_name):
    clear_screen()
    print_header()
    local_filename = url.split('/')[-1]
    installers_dir = r"C:\Games\Installers"
    installer_path = os.path.join(installers_dir, local_filename)
    # Game shortcut paths
    shortcut_paths = {
        "Half-Life 1.0.0.5": r"C:\Games\Half-Life 1.0.0.5\Half-Life.lnk",
        "Counter-Strike 1.6": r"C:\Games\Counter-Strike 1.6\Counter-Strike.lnk",
        "Day of Defeat": r"C:\Games\Day of Defeat\Day of Defeat.lnk"
    }
    shortcut_path = shortcut_paths.get(game_name)
    log(f"Checking for shortcut: {shortcut_path}")
    if shortcut_path and os.path.exists(shortcut_path):
        log(f"{game_name} shortcut found at {shortcut_path}")
        print(Fore.YELLOW + f"{game_name} shortcut already exists at {shortcut_path}" + Style.RESET_ALL)
        launch = input(Fore.WHITE + "Do you want to launch the game? (y/n): " + Style.RESET_ALL)
        if launch.lower() == 'y':
            log(f"Launching shortcut: {shortcut_path}")
            os.startfile(shortcut_path) if os.name == 'nt' else os.system(f'xdg-open "{shortcut_path}"')
        input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
        return
    # Check if installer already exists in Installers folder
    if not os.path.exists(installers_dir):
        os.makedirs(installers_dir)
        log(f"Created installers directory: {installers_dir}")
    log(f"Checking for installer: {installer_path}")
    if os.path.exists(installer_path):
        log(f"{game_name} installer found at {installer_path}")
        print(Fore.YELLOW + f"{game_name} installer already exists at {installer_path}" + Style.RESET_ALL)
        launch = input(Fore.WHITE + "Do you want to launch the installer? (y/n): " + Style.RESET_ALL)
        if launch.lower() == 'y':
            log(f"Launching installer: {installer_path}")
            os.startfile(installer_path) if os.name == 'nt' else os.system(f'xdg-open "{installer_path}"')
        input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
        return
    print(Fore.CYAN + f"Downloading {game_name} installer..." + Style.RESET_ALL)
    log(f"Downloading {game_name} from {url}")
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(installer_path, 'wb') as f:
                for chunk in tqdm(r.iter_content(chunk_size=8192), desc="Downloading", unit="B", unit_scale=True):
                    if chunk:
                        f.write(chunk)
        log(f"Download complete: {installer_path}")
        print(Fore.GREEN + f"Download complete: {installer_path}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"Launching installer for {game_name}..." + Style.RESET_ALL)
        log(f"Launching installer: {installer_path}")
        os.startfile(installer_path) if os.name == 'nt' else os.system(f'xdg-open "{installer_path}"')
    except Exception as e:
        log(f"Error downloading or launching installer: {e}")
        print(Fore.RED + f"Error downloading or launching installer: {e}" + Style.RESET_ALL)
    input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

# Main Launcher Function
def main():
    # Clear the screen
    clear_screen()
    
    # Display the logo
    display_logo()
    
    # Your main launcher logic would go here
    print(colorama.Fore.WHITE + "Launcher initialized successfully!")
    print(colorama.Fore.WHITE + "Ready to load game options...")
    
    # Example: Simulate loading with a progress bar
    for i in tqdm(range(100), desc="Loading launcher", unit="%"):
        time.sleep(0.05)

# Clear the screen
    clear_screen()    

# INSTALL MENU:

def install_menu():
    clear_screen()
    print_header()
    print(Fore.GREEN + "INSTALL GAMES" + Style.RESET_ALL)
    print("1. Half-Life 1.0.0.5")
    print("2. Counter-Strike 1.6")
    print("3. Day of Defeat")
    print("4. " + Fore.YELLOW + "Back to Main Menu")
    choice = input(Fore.WHITE + "\nChoose a game to install: " + Style.RESET_ALL)
    if choice == '1':
        download_and_install("https://dllx.down-cs.su/downloads/half_life.exe", "Half-Life 1.0.0.5")
    elif choice == '2':
        download_and_install("https://dllx.down-cs.su/downloads/cs_16_clean_eng.exe", "Counter-Strike 1.6")
    elif choice == '3':
        download_and_install("https://dllx.down-cs.su/downloads/day_of_defeat.exe", "Day of Defeat")
    elif choice == '4':
        return  # Return to main menu
    else:
        print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)
        input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

# INPUT URLS MENU:

def input_urls_menu():
    clear_screen()
    print_header()
    print(Fore.BLUE + "INPUT CUSTOM GAME URL" + Style.RESET_ALL)
    url = input(Fore.WHITE + "Enter the direct download URL for the game installer: " + Style.RESET_ALL)
    if url.strip():
        game_name = input(Fore.WHITE + "Enter a name for this game: " + Style.RESET_ALL)
        download_and_install(url, game_name)
    else:
        print(Fore.RED + "No URL entered." + Style.RESET_ALL)
        input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

# LAUNCH GAMES MENU:

def launch_game_menu():
    clear_screen()
    print_header()
    print(Fore.MAGENTA + "LAUNCH INSTALLED GAMES" + Style.RESET_ALL)
    print("1. Half-Life 1.0.0.5")
    print("2. Counter-Strike 1.6")
    print("3. Day of Defeat")
    print("4. " + Fore.YELLOW + "Back to Main Menu")
    choice = input(Fore.WHITE + "\nChoose a game to launch: " + Style.RESET_ALL)
    shortcut_paths = {
        '1': r"C:\Games\Half-Life 1.0.0.5\Half-Life.lnk",
        '2': r"C:\Games\Counter-Strike 1.6\Counter-Strike.lnk",
        '3': r"C:\Games\Day of Defeat\Day of Defeat.lnk"
    }
    if choice in shortcut_paths:
        shortcut = shortcut_paths[choice]
        log(f"User selected to launch shortcut: {shortcut}")
        if os.path.exists(shortcut):
            print(Fore.GREEN + f"Launching {shortcut}..." + Style.RESET_ALL)
            log(f"Launching {shortcut}")
            os.startfile(shortcut) if os.name == 'nt' else os.system(f'xdg-open "{shortcut}"')
        else:
            print(Fore.RED + f"{shortcut} not found. Please install the game first." + Style.RESET_ALL)
            log(f"Shortcut not found: {shortcut}")
        input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
    elif choice == '4':
        return
    else:
        print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)
        log("Invalid game launch choice")
        input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)

# MAIN MENU:

def main_menu():
    while True:
        clear_screen()
        print_header()
        print(Fore.GREEN + "MAIN MENU" + Style.RESET_ALL)
        print("1. " + Fore.CYAN + "Install Games")
        print("2. " + Fore.MAGENTA + "Launch Games")
        print("3. " + Fore.BLUE + "Input Urls")
        print("4. " + Fore.YELLOW + "Settings")
        print("5. " + Fore.RED + "Exit")
        print("M. " + Fore.MAGENTA + "Download Modded CS 1.6" + Style.RESET_ALL)
        print("L. " + Fore.YELLOW + "View Logs" + Style.RESET_ALL)
        print("A. " + Fore.WHITE + "About The Project SLVL Game Launcher" + Style.RESET_ALL)
        
        choice = input(Fore.WHITE + "\nEnter your choice (1-5, M, L or A): " + Style.RESET_ALL)
        
        if choice == '1':
            clear_screen()
            install_menu()
        elif choice == '2':
            clear_screen()
            launch_game_menu()
        elif choice == '3':
            clear_screen()
            input_urls_menu()
        elif choice == '4':
            clear_screen()
            settings_menu()
        elif choice == '5':
            log("Exiting launcher")
            print(Fore.YELLOW + "Goodbye!" + Style.RESET_ALL)
            break
        elif choice.upper() == 'M':
            clear_screen()
            modded_cs_menu()
        elif choice.upper() == 'L':
            clear_screen()
            view_logs_menu()
        elif choice.upper() == 'A':
            clear_screen()
            About_Launcher()
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid choice! Please enter 1-5, M, L or A." + Style.RESET_ALL)
            log("Invalid main menu choice")
            input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)

def About_Launcher():
    clear_screen()
    print_header()
    print(Fore.CYAN + "Project SLVL Game Launcher v1.0")
    print(Fore.YELLOW + "Code Name: Gordon")
    print(Fore.WHITE + "Created by EmadFahim134")
    print(Fore.WHITE + "This launcher helps you install, launch, and manage classic games and mods.")
    print(Fore.WHITE + "For more info, visit: https://github.com/yourprojecturl")
    print(Style.RESET_ALL)

def launch_menu():
    clear_screen()
    print_header()
    print("Launch menu - coming soon!")
    input("Press Enter to continue...")

def mods_menu():
    clear_screen()
    print_header()
    print("Mods menu - coming soon!")
    input("Press Enter to continue...")

def settings_menu():
    clear_screen()
    print_header()
    print("Settings menu - coming soon!")
    input("Press Enter to continue...")

def modded_cs_menu():
    clear_screen()
    print_header()
    print(Fore.MAGENTA + "="*40)
    print(Fore.MAGENTA + "      MODDED CS 1.6 EDITIONS")
    print(Fore.MAGENTA + "="*40 + Style.RESET_ALL)
    print(Fore.WHITE + "Fetching editions from down-cs.su..." + Style.RESET_ALL)
    url = "https://down-cs.su/"
    installers_dir = r"C:\Games\Installers"
    editions = []
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        # Find popular editions (by download buttons or links)
        for a in soup.find_all("a", href=True):
            href = a["href"]
            text = a.get_text(strip=True)
            # Only show .exe installers and popular editions
            if href.endswith(".exe") and ("CS" in text or "Counter-Strike" in text):
                # Convert relative URLs to absolute
                if href.startswith("/"):
                    href = url.rstrip("/") + href
                elif not href.startswith("http"):
                    href = url.rstrip("/") + "/" + href
                # Avoid duplicates and empty names
                if text and (text, href) not in editions:
                    editions.append((text, href))
        # If nothing found, fallback to default
        if not editions:
            editions = [
                ("CS 1.6 Original", "https://down-cs.su/downloads/cs16setup.exe"),
                ("CS 1.6 WarZone", "https://down-cs.su/downloads/cs16warzone.exe"),
                ("CS 1.6 XTCS", "https://down-cs.su/downloads/cs16xtcs.exe"),
            ]
    except Exception as e:
        print(Fore.RED + f"Could not fetch editions: {e}" + Style.RESET_ALL)
        editions = [
            ("CS 1.6 Original", "https://down-cs.su/downloads/cs16setup.exe"),
            ("CS 1.6 WarZone", "https://down-cs.su/downloads/cs16warzone.exe"),
            ("CS 1.6 XTCS", "https://down-cs.su/downloads/cs16xtcs.exe"),
        ]
    print(Fore.CYAN + "\nPopular CS 1.6 Editions:" + Style.RESET_ALL)
    for idx, (name, link) in enumerate(editions, 1):
        print(Fore.YELLOW + f"{idx}. {name}" + Style.RESET_ALL)
    print(Fore.YELLOW + f"{len(editions)+1}. Back to Main Menu" + Style.RESET_ALL)
    choice = input(Fore.WHITE + "\nChoose an edition to download: " + Style.RESET_ALL)
    try:
        choice_num = int(choice)
        if 1 <= choice_num <= len(editions):
            edition_name, edition_url = editions[choice_num-1]
            installer_name = edition_url.split("/")[-1]
            installer_path = os.path.join(installers_dir, installer_name)
            log(f"Modded CS 1.6: Checking for installer at {installer_path}")
            if not os.path.exists(installers_dir):
                os.makedirs(installers_dir)
                log(f"Created installers directory: {installers_dir}")
            if os.path.exists(installer_path):
                print(Fore.YELLOW + f"{edition_name} installer already exists at {installer_path}" + Style.RESET_ALL)
                launch = input(Fore.WHITE + "Do you want to launch the installer? (y/n): " + Style.RESET_ALL)
                if launch.lower() == 'y':
                    log(f"Launching {edition_name} installer: {installer_path}")
                    os.startfile(installer_path) if os.name == 'nt' else os.system(f'xdg-open "{installer_path}"')
                input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
                return
            print(Fore.CYAN + f"Downloading {edition_name} installer..." + Style.RESET_ALL)
            log(f"Downloading {edition_name} from {edition_url}")
            try:
                with requests.get(edition_url, stream=True) as r:
                    r.raise_for_status()
                    with open(installer_path, 'wb') as f:
                        for chunk in tqdm(r.iter_content(chunk_size=8192), desc="Downloading", unit="B", unit_scale=True):
                            if chunk:
                                f.write(chunk)
                log(f"{edition_name} download complete: {installer_path}")
                print(Fore.GREEN + f"Download complete: {installer_path}" + Style.RESET_ALL)
                print(Fore.YELLOW + "Launching installer..." + Style.RESET_ALL)
                log(f"Launching {edition_name} installer: {installer_path}")
                os.startfile(installer_path) if os.name == 'nt' else os.system(f'xdg-open "{installer_path}"')
            except Exception as e:
                log(f"Error downloading or launching {edition_name} installer: {e}")
                print(Fore.RED + f"Error downloading or launching installer: {e}" + Style.RESET_ALL)
            input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
        elif choice_num == len(editions)+1:
            return
        else:
            print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)
            input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)
    except Exception:
        print(Fore.RED + "Invalid input!" + Style.RESET_ALL)
        input(Fore.WHITE + "Press Enter to continue..." + Style.RESET_ALL)



if __name__ == "__main__":
    main()        # Show logo and loading
    main_menu()   # Then show main menu