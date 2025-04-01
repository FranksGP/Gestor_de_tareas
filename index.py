import json
import os

TASKS_FILE = "Tareas.json"

def cargarTask():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []  # Retorna una lista vacía si hay un error en el JSON
    return []

def guardarTask(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def agregarTask(titulo, descripcion):
    tasks = cargarTask()
    tasks.append({"titulo": titulo, "descripcion": descripcion, "completed": False})
    guardarTask(tasks)
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
        guardarTask(tasks)
        print("Tarea marcada como completada.")
    else:
        print("Índice inválido.")

def delete_task(index):
    tasks = cargarTask()
    if 0 < index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        guardarTask(tasks)
        print(f"Tarea '{deleted_task['titulo']}' eliminada.")
    else:
        print("Índice inválido.")

def main():
    while True:
        print("\nGestor de Tareas")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            agregarTask(titulo, descripcion)
        elif opcion == "2":
            listarTask()
        elif opcion == "3":
            listarTask()
            try:
                index = int(input("Ingrese el número de la tarea a completar: "))
                tareaCompletada(index)
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
        elif opcion == "4":
            listarTask()
            try:
                index = int(input("Ingrese el número de la tarea a eliminar: "))
                delete_task(index)
            except ValueError:
                print("Entrada inválida. Debe ingresar un número.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
