import os

def show_menu():
    print("\n---Gestor de Tareas---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def load_tasks():
    tasks = []
    file_path = "Módulo 3/EvaluacionDeModulo3/evaluación_de_modulo_3.txt"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding='utf-8') as file:
            for line in file:
                title, status = line.strip().split(",")
                completed = status == "1"
                tasks.append({"título": title, "completada": completed})
    return tasks

def add_tasks(tasks):
    title = input("Ingrese el título de la tarea: ")
    task = {"título": title, "completada": False}
    tasks.append(task)
    print("Tarea agregada.\n")

def see_tasks(tasks):
    if not tasks:
        print("No hay tareas.")
        return
    for i, task in enumerate(tasks):
        status = "completada" if task["completada"] else "pendiente"
        print(f"{i + 1}. {task['título']} - {status}")

def mark_completed(tasks):
    see_tasks(tasks)
    index = int(input("Ingrese el número de la tarea a marcar como completada: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completada"] = True
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea no válido.")

def delete_task(tasks):
    see_tasks(tasks)
    index = int(input("Ingrese el número de la tarea a eliminar: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Tarea eliminada.")
    else:
        print("Número de tarea no válido.")

def save_tasks(tasks):
    file_path = "Módulo 3/EvaluacionDeModulo3/evaluación_de_modulo_3.txt"
    with open(file_path, "w", encoding='utf-8') as file:
        for task in tasks:
            status = "1" if task["completada"] else "0"
            file.write(f"{task['título']},{status}\n")
    print(f"Tareas guardadas en '{file_path}'.")

def main():
    tasks = load_tasks()  # Cargar tareas desde el archivo
    while True:
        show_menu()
        option = input("Selecciona una opción: ")
        if option == "1":
            add_tasks(tasks)
        elif option == "2":
            see_tasks(tasks)
        elif option == "3":
            mark_completed(tasks)
        elif option == "4":
            delete_task(tasks)
        elif option == "5":
            save_tasks(tasks)
            print("\nSaliendo del programa...\n")
            break
        else:
            print("Opción no válida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
