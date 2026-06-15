import os
import json
import glob

class FrameworkManager:
    def __init__(self, lib_path="../subconscious_lib"):
        self.lib_path = os.path.abspath(os.path.join(os.path.dirname(__file__), lib_path))
        
    def get_available_frameworks(self):
        search_pattern = os.path.join(self.lib_path, "*.json")
        files = glob.glob(search_pattern)
        return [os.path.basename(f) for f in files]

    def load_framework(self, filename):
        filepath = os.path.join(self.lib_path, filename)
        with open(filepath, "r") as f:
            return json.load(f)
