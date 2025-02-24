import json
import os
from typing import Dict, Any

class JSONDatabase:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def load_data(self, filename: str) -> Dict[str, Any]:
        filepath = os.path.join(self.data_dir, f"{filename}.json")
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self, filename: str, data: Dict[str, Any]) -> None:
        filepath = os.path.join(self.data_dir, f"{filename}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def clear(self) -> None:
        """Clears all JSON files in the data directory by creating empty JSON files."""
        for filename in os.listdir(self.data_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(self.data_dir, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    json.dump({}, f, indent=4)
