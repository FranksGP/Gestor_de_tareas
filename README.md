# 📌 Gestor de Tareas en Python

Este es un gestor de tareas basado en línea de comandos desarrollado en Python. Permite gestionar tareas pendientes, almacenarlas en un archivo JSON y modificarlas según sea necesario.

## 📋 Requisitos
- Python 3.x instalado en tu sistema.

## 🚀 Instalación y Ejecución

1. **Clonar el repositorio (opcional)**
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. **Ejecutar el script**
   ```sh
   python gestor_tareas.py
   ```

## 🛠️ Funcionalidades

El programa ofrece las siguientes opciones:

1. **Agregar tarea** 📝
   - Permite añadir una nueva tarea proporcionando un título y una descripción.
   - La tarea se almacena con el estado inicial "Pendiente".

2. **Listar tareas** 📄
   - Muestra todas las tareas almacenadas en `Tareas.json`.
   - Indica el estado de cada tarea: `✔ Completada` o `✘ Pendiente`.

3. **Marcar tarea como completada** ✅
   - Permite cambiar el estado de una tarea de "Pendiente" a "Completada".
   - Se selecciona ingresando el número de la tarea en la lista.

4. **Eliminar tarea** 🗑️
   - Permite eliminar una tarea de la lista ingresando su número.
   - Se actualiza automáticamente el archivo `Tareas.json`.

5. **Salir del programa** 🔚
   - Cierra la aplicación.

## 📂 Estructura del Archivo JSON
El archivo `Tareas.json` almacena las tareas en el siguiente formato:

```json
[
    {
        "titulo": "Ejemplo de tarea",
        "descripcion": "Descripción de la tarea",
        "completed": false
    }
]
```

## 🏗️ Futuras Mejoras
Algunas posibles mejoras para versiones futuras incluyen:
- Implementación de una interfaz gráfica (GUI).
- Soporte para fechas de vencimiento.
- Categorías o etiquetas para organizar tareas.
- Sincronización con bases de datos remotas.

## 👨‍💻 Autor
Desarrollado por Jorge Hernadez, Dissel Leal y Frank Garzón.

¡Disfruta organizando tus tareas de manera eficiente! 🎯

