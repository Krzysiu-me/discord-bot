# /handlers/command_handler.py
import importlib
import os

def load_commands(category_path):
    commands = []
    for filename in os.listdir(category_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"{category_path.replace('/', '.')}.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, "setup"):
                commands.append(module)
    return commands
