def mostrar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas pendientes")
    else:
        print("\nLista de Tareas pendientes:")
        for i, tarea in enumerate(lista_tareas):
            print(f"{i}. {tarea}")