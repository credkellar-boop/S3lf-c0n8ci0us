import importlib
import os

def load_dynamic_plugins(plugin_dir="plugins"):
    plugins = {}
    for filename in os.listdir(plugin_dir):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            plugins[module_name] = importlib.import_module(f"{plugin_dir}.{module_name}")
    return plugins
