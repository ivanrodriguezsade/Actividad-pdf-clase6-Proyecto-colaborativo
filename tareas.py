# Realizando codigo inicial sencillo
tareas = []

def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def mostrar_tarea():
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes: ")
        for i, tarea in enumerate(tareas):
            print(f"{i + 1}. {tarea}")

if __name__ == "__main__":
    print("App de lista de tareas")
