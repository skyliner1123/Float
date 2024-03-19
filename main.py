import random
import string
import requests
import os
import discord
import time
from discord import SyncWebhook
from colorama import *
from colorama import init
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

init()


def install_dependencies():
    try:
        # Run pip install command
        subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
        print("All dependencies have been successfully installed.")
    except subprocess.CalledProcessError:
        print("Failed to install dependencies. Please check your internet connection and try again.")

# Check if this is the first launch
# You can use a flag or a configuration file to determine this
# For simplicity, I'll assume it's the first launch every time
first_launch = True

if first_launch:
    install_dependencies()

os.system("cls")

def float_menu():
    return f'''{Fore.RED + Style.NORMAL}

                                        $$$$$$$$\ $$\                       $$\     
                                        $$  _____|$$ |                      $$ |    
                                        $$ |      $$ | $$$$$$\   $$$$$$\  $$$$$$\   
                                        $$$$$\    $$ |$$  __$$\  \____$$\ \_$$  _|  
                                        $$  __|   $$ |$$ /  $$ | $$$$$$$ |  $$ |    
                                        $$ |      $$ |$$ |  $$ |$$  __$$ |  $$ |$$\ 
                                        $$ |      $$ |\$$$$$$  |\$$$$$$$ |  \$$$$  |
                                        \__|      \__| \______/  \_______|   \____/ 
    
{Fore.RED + Style.NORMAL}____________________________________________________________________________________________________________________{Fore.RESET}
    
                            {Fore.RED + Style.NORMAL}[0]{Fore.RESET} Exit                   {Fore.RED + Style.NORMAL}[3]{Fore.RESET} Coming Soon       {Fore.RED + Style.NORMAL}[6]{Fore.RESET} Coming Soon 
                            {Fore.RED + Style.NORMAL}[1]{Fore.RESET} SnapChat BruteForcer   {Fore.RED + Style.NORMAL}[4]{Fore.RESET} Coming Soon       {Fore.RED + Style.NORMAL}[7]{Fore.RESET} Coming Soon
                            {Fore.RED + Style.NORMAL}[2]{Fore.RESET} Coming Soon            {Fore.RED + Style.NORMAL}[5]{Fore.RESET} Coming Soon       {Fore.RED + Style.NORMAL}[8]{Fore.RESET} Update
    
                                              {Fore.RED + Style.NORMAL}Made By RustyCMD and FOID{Fore.RESET}
    
{Fore.RED + Style.NORMAL}____________________________________________________________________________________________________________________{Fore.RESET}
    '''

def open_window(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show the message box
    messagebox.showinfo("Float Multi-Purpose Tool", message)

    # Close the window after showing the message
    root.destroy()

repo_owner = "skyliner1123"
repo_name = "Float"

def check_for_update():
    try:
        # Fetch latest version from version.txt file
        with open("version.txt", "r") as file:
            latest_version = file.read().strip()

        return latest_version
    except FileNotFoundError:
        print("Version file not found. Unable to check for updates.")
        return None

def update_script(latest_version):
    try:
        # Update version.txt file with the latest version
        with open("version.txt", "w") as file:
            file.write(latest_version)
    except Exception as e:
        print("An error occurred while updating the version file:", e)

def check_password(username, password):
    with open("passwords.txt", "r") as file:
        for line in file:
            if line.count(":") == 1:
                stored_username, stored_password = line.strip().split(":")
                if username == stored_username:
                    if password == stored_password:
                        return True
                    else:
                        print(f"Password ({stored_password}) Failed Trying The Next One")
                        time.sleep(0.5)  # Add a 0.5-second delay
            else:
                print(f"Password ({line.strip()}) Failed, Trying The Next One")
                time.sleep(0.5)  # Add a 0.5-second delay
        print("Username not found")
        return False

import os
from colorama import Fore

import os
from colorama import Fore

def main():
    print(float_menu())
    choice = input(f"{Fore.RED}root@float{Fore.RESET} Enter your choice: ")
    if choice == "1":
        username = input("Enter Snapchat Username: ")
        if check_password(username, ""):
            print("Login Successful")
        else:
            print("Login Failed")
    elif choice == "0":
        print("Exiting...")
    elif choice == "8":
        latest_version = check_for_update()
        if latest_version and latest_version != "v1.0":  # Replace "v1.0" with the current version of your script
            print("A new version is available! Do you want to update? (yes/no)")
            update_choice = input().lower()
            if update_choice == "yes":
                print("Updating script...")
                update_script(latest_version)  # Update version.txt with the latest version
                current_version = check_for_update()  # Read the updated version from version.txt
                print("Current version after update:", current_version)
                if current_version == latest_version:
                    print("Script is already up to date.")
                else:
                    update_script(latest_version)  # Perform the script update with the latest version
                    print("Update successful. Please restart the script.")
                    exit()
            else:
                print("Skipping update.")
        else:
            print("No update available.")

    else:
        open_window("That's Not An Option!")
        os.system("cls")
        main()

os.system('title Float Multi-Purpose Tool')

main()
