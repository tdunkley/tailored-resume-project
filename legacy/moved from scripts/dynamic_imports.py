import importlib
import os

# ...existing code...

def dynamic_import(module_name, class_name):
    """Dynamically import a class from a module."""
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

# ...existing code...
