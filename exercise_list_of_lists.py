# Ejercicio 12: Manipular lista de listas

def list_of_lists(lista_de_listas):
    """
    Modifica una lista de 3 listas internas:
    - Primera lista: solo los primeros 2 elementos
    - Segunda lista: elementos entre el segundo y cuarto
    - Tercera lista: solo los últimos 2 elementos

    Args:
        lista_de_listas: Una lista que contiene 3 listas

    Returns:
        La lista de listas modificada según las reglas
    """
    lista1 = lista_de_listas[0]
    lista2 = lista_de_listas[1]
    lista3 = lista_de_listas[2]
    if len(lista1) == 0:
        lista1_nueva = lista1
    if len(lista1) >= 3:
        lista1_nueva = lista1[:2]
    if len(lista1) != 0 < 3:
        lista1_nueva = lista1[:2]

    if len(lista2) > 3:
        lista2_nueva = lista2[1:4]
    if len(lista2) > 0 and len(lista2) <= 3:
        lista2_nueva = lista2[1:4]
    if len(lista2) == 0:
        lista2_nueva = lista2

    if len(lista3) >= 2:
        lista3_nueva = lista3[-2:]
    if len(lista3) < 2:
        lista3_nueva = lista3
    lista4 = [lista1_nueva, lista2_nueva, lista3_nueva]
    return lista4


