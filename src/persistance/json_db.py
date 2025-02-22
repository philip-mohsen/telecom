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
            with open(filepath, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_data(self, filename: str, data: Dict[str, Any]) -> None:
        filepath = os.path.join(self.data_dir, f"{filename}.json")
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
