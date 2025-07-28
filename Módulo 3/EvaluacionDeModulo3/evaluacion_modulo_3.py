import os  # Importa el módulo os para manejar operaciones del sistema operativo

# Nota: abrir desde el repositorio principal (trabajosModulos)

def show_menu():
    print("\n---Gestor de Tareas---")  # Muestra el título del menú
    print("1. Agregar tarea")  # Opción para agregar una nueva tarea
    print("2. Ver tareas")  # Opción para ver las tareas existentes
    print("3. Marcar tarea como completada")  # Opción para marcar tarea como completada
    print("4. Eliminar tarea")  # Opción para eliminar una tarea
    print("5. Salir")  # Opción para salir del programa

def load_tasks():
    tasks = []  # Inicializa una lista vacía para almacenar las tareas
    file_path = "Módulo 3/EvaluacionDeModulo3/evaluación_de_modulo_3.txt"  # Ruta del archivo
    if os.path.exists(file_path):  # Verifica si el archivo existe en la ruta especificada
        with open(file_path, "r", encoding='utf-8') as file:  # Abre el archivo en modo lectura
            for line in file:  # Itera sobre cada línea del archivo
                title, status = line.strip().split(",")  # Separa el título y el estado
                completed = status == "1"  # Verifica si la tarea está completada
                tasks.append({"título": title,  # Agrega la tarea a la lista
                            "completada": completed})  
    return tasks  # Devuelve la lista de tareas cargadas

def add_tasks(tasks):
    title = input("Ingrese el título de la tarea: ")  # Solicita el título de la nueva tarea
    task = {"título": title,  # Crea un diccionario para la tarea
            "completada": False}  
    tasks.append(task)  # Agrega la nueva tarea a la lista
    print("Tarea agregada.\n")  # Mensaje de confirmación al agregar la tarea

def see_tasks(tasks):
    if not tasks:  # Verifica si la lista de tareas está vacía
        print("No hay tareas.")  # Mensaje si no hay tareas
        return  # Sale de la función
    for i, task in enumerate(tasks):  # Itera sobre las tareas con índice
        status = "completada" if task["completada"] else "pendiente"  # Define el estado
        print(f"{i + 1}. {task['título']} - {status}")  # Muestra la tarea con su estado

def mark_completed(tasks):
    see_tasks(tasks)  # Muestra las tareas antes de marcar
    index = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1  # Solicita el índice
    if 0 <= index < len(tasks):  # Verifica si el índice es válido
        tasks[index]["completada"] = True  # Marca la tarea como completada
        print("Tarea marcada como completada.")  # Mensaje de confirmación
    else:
        print("Número de tarea no válido.")  # Mensaje de error si el índice no es válido

def delete_task(tasks):
    see_tasks(tasks)  # Muestra las tareas antes de eliminar
    index = int(input("Ingrese el número de la tarea a eliminar: ")) - 1  # Solicita el índice
    if 0 <= index < len(tasks):  # Verifica si el índice es válido
        tasks.pop(index)  # Elimina la tarea de la lista
        print("Tarea eliminada.")  # Mensaje de confirmación
    else:
        print("Número de tarea no válido.")  # Mensaje de error si el índice no es válido

def save_tasks(tasks):
    file_path = "Módulo 3/EvaluacionDeModulo3/evaluación_de_modulo_3.txt"  # Ruta del archivo
    with open(file_path, "w", encoding='utf-8') as file:  # Abre el archivo en modo escritura
        for task in tasks:  # Itera sobre cada tarea en la lista
            status = "1" if task["completada"] else "0"  # Define el estado como '1' o '0'
            file.write(f"{task['título']},{status}\n")  # Escribe la tarea en el archivo
    print(f"Tareas guardadas en '{file_path}'.")  # Mensaje de confirmación al guardar

def main():
    tasks = load_tasks()  # Carga tareas desde el archivo
    while True:  # Inicia un bucle infinito para el menú
        show_menu()  # Muestra el menú de opciones
        option = input("Selecciona una opción: ")  # Solicita al usuario que seleccione una opción
        if option == "1":
            add_tasks(tasks)  # Llama a la función para agregar una tarea
        elif option == "2":
            see_tasks(tasks)  # Llama a la función para ver las tareas
        elif option == "3":
            mark_completed(tasks)  # Llama a la función para marcar tarea como completada
        elif option == "4":
            delete_task(tasks)  # Llama a la función para eliminar una tarea
        elif option == "5":
            save_tasks(tasks)  # Llama a la función para guardar las tareas
            print("\nSaliendo del programa...\n")  # Mensaje al salir del programa
            break  # Sale del bucle
        else:
            print("Opción no válida. Intenta de nuevo.\n")  # Mensaje de error para opción inválida

if __name__ == "__main__":
    main()  # Llama a la función principal al ejecutar el script