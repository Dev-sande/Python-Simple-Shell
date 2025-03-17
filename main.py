# Connect with me on Linkedin - https://www.linkedin.com/in/tapiwa-sande/

import os
import time

# Function to get user input for a command
def get_command():
    command = input("Input>> ")
    return command

# Function to list files in the current directory
def list_file():
    files = os.listdir('.')
    if files:
        print("\nFiles in the current directory:")
        for file in files:
            print(file)
    else:
        print("No files found in the current directory.")

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Screen cleared.")

# Function to print the current working directory
def print_pwd():
    current_directory = os.getcwd()
    print(f"Current Directory: {current_directory}")

# Function to create a new file with some content
def create_file():
    filename = input("Enter the filename to create: ")
    try:
        with open(filename, 'w') as file:
            file.write("This is a new file created by the SimpleShell.")
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")  # Handle any errors that may occur during file creation

# Function to read a file's contents
def read_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of {filename}:\n{content}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")  # Handle other errors

# Main loop
while True:
    user_command = get_command()  # Get user command

    if user_command == "ls":  # List files in the current directory
        list_file()

    elif user_command == "clear":  # Clear the terminal screen
        clear_screen()

    elif user_command == "pwd":  # Print the current working directory
        print_pwd()

    elif user_command == "create":  # Create a new file
        create_file()

    elif user_command == "read":  # Read the content of a file
        read_file()

    elif user_command == "exit":  # Exit the program
        print("Goodbye")
        time.sleep(1)  # Add a slight delay before exit
        break  # Break out of the loop to exit the program

    else:  # Handle unknown commands
        print("You typed an unknown command. Please try again.")
