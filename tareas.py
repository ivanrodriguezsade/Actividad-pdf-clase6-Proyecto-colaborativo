# Realizando codigo inicial sencillo
tareas = []

def agregar_tarea(tarea):
    tareas.append({"Descripción": tarea, "completada": False})
    print(f"Tarea '{tarea}' agregada.")

def mostrar_tareas():
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes: ")
        for i, tarea in enumerate(tareas):
            estado = "[X]" if tarea["completada"] else "[ ]"
            print(f"{i + 1}. {estado} {tarea["descripción"]}")

def marcar_completada(indice):
    if 1 <= indice <= len(tareas):
        tareas[indice - 1]["completada"] = True
        print(f"Tarea {indice} marcada como completada.")
    else:
        print("Indice de tarea inválido.")

if __name__ == "__main__":
    print("App de lista de tareas")
    agregar_tarea("comprar leche")
    agregar_tarea("comprar azucar")
    agregar_tarea("estudiar para programacion II")
    mostrar_tareas()
    marcar_completada(1)
    mostrar_tareas()

