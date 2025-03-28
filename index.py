import json
import os

TASKS_FILE = "Tareas.json"

def cargarTask():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


