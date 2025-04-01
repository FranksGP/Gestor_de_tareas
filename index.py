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
        
def tareaCompletada(index):
    tasks = cargarTask()
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        cargarTask(tasks)
        print("Tarea marcada como completada.")
    else:
        print("Índice inválido.")

def delete_task(index):
    tasks = cargarTask()
    if 0 < index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        cargarTask(tasks)
        print(f"Tarea '{deleted_task['titulo']}' eliminada.")
    else:
        print("Índice inválido.")