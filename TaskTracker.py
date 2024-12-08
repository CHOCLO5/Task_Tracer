"""
print("---------MENU---------")
print("Seleccione una opción:")
print("1. Listar Tareas")
print("2. Agregar Tareas")
print("3. Actualizar Tareas")
print("4. Eliminar Tareas")

respuesta = input()
"""

def agregar_tareas(tareas):
    cantidad_tareas = input("¿Cuántas tareas deseas agregar? ")
    contador = 0
    while contador < int(cantidad_tareas):
        contador += 1
        descripcion = input("Descripción: ")
        # Agregar la descripción de la tarea
        tareas[contador] = {"descripcion": descripcion}
        print("Define el estado de la tarea:")
        print("1. To do")
        print("2. In progress")
        status = input("Estado: ")
        # Actualizar el estado de la tarea
        if int(status) == 1:
            tareas[contador]["status"] = "todo"
        else:
            tareas[contador]["status"] = "in-progress"
    print("Tareas cargadas\n")

tareas = {}
agregar_tareas(tareas)
print("Listado de tareas:")
print(tareas[1])
for id_tarea, detalles in tareas.items():
    print(f"Tarea {id_tarea}: Descripción: {detalles['descripcion']}, Estado: {detalles['status']}")
