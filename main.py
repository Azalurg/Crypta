# Author: Azalurg
# Project: Crypta
# Repository: www.github.com/Azalurg/crypta
# Version: 0.1
# Date: 2023-04-01

import os
import importlib

# Get a list of all the file names in the "src" directory
src_files = os.listdir("src")
function_names = {}

# Dynamically import each file and get the function name
for file_name in src_files:
    if file_name.endswith(".py") and file_name != "__init__.py":
        module_name = file_name[:-3]  # Remove the ".py" extension
        module = importlib.import_module("src." + module_name)
        function_name = module_name
        if hasattr(module, module_name):
            function_name = getattr(module, module_name).__name__
        function_names[file_name] = (function_name, module_name)

# Generate the menu
print("Welcome to Crypta!")
for i, file_name in enumerate(sorted(function_names)):
    function_name, module_name = function_names[file_name]
    print(f"{i+1}. {function_name}")

# Prompt the user to choose an action
while True:
    choice = input("\nChoose an action (enter a number or 'q' to quit): ")
    if choice == "q":
        break
    try:
        choice = int(choice)
        if 1 <= choice <= len(function_names):
            file_name = sorted(function_names)[choice - 1]
            module_name = function_names[file_name][1]
            module = importlib.import_module("src." + module_name)
            getattr(module, module_name)()
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid choice.")
