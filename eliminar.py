def eliminar_tarea(lista_tareas, indice):
    try:
        tarea_eliminada = lista_tareas.pop(indice)
        print(f"🗑️ Tarea eliminada: '{tarea_eliminada}'")
    except IndexError:
        print(" Error: El índice no existe.")