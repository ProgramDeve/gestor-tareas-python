import agregar
import mostrar
import eliminar

mis_tareas = []

while True:
    print("\n--- BIENVENIDO AL GESTOR DE TAREAS ---")
    print("Menú de Opciones:")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción (1/2/3/4): ")

    if opcion == "1":
        mostrar.mostrar_tareas(mis_tareas)
    elif opcion == "2":
        tarea = input("Escribe la nueva tarea: ")
        agregar.agregar_tarea(mis_tareas, tarea)
    elif opcion == "3":
        mostrar.mostrar_tareas(mis_tareas)
        try:
            indice = int(input("Ingresa el número de la tarea a eliminar: "))
            eliminar.eliminar_tarea(mis_tareas, indice)
        except ValueError:
            print("❌ Por favor, ingresa un número válido.")
    elif opcion == "4":
        print("Saliendo del gestor... ¡Hasta luego!")
        break
    else:
        print("❌ Opción no válida. Intenta de nuevo.")