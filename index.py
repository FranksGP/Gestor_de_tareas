import json
import os

TASKS_FILE = "Tareas.json"

def cargarTask():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)  
        return []

def cargarTask(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def agregarTask(titulo, descripcion):
    tasks = cargarTask()
    tasks.append({"titulo": titulo, "descripcion": descripcion, "completed": False})
    cargarTask(tasks)
    print("Tarea agregada exitosamente.")

def listarTask():
    tasks = cargarTask()
    if not tasks:
        print("No hay tareas disponibles.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✔ Completada" if task["completed"] else "✘ Pendiente"
        print(f"{index}. {task['titulo']} - {task['descripcion']} [{status}]")