# Ejercicio 11: Comparar tercer elemento de dos listas

def check_lists(lista1, lista2):
    """
    Verifica si ambas listas tienen el mismo elemento en la tercera posición.
    Si alguna de las listas no tiene un tercer elemento, retorna False.

    Args:
        lista1: Primera lista
        lista2: Segunda lista

    Returns:
        True si ambas listas tienen el mismo tercer elemento, False en caso contrario
    """
    if len(lista1) < 3 or len(lista2) < 3:
        return False
    elemento1 = lista1[2]
    elemento2 = lista2[2]
    if elemento1 == elemento2:
        return True
    else:
        return False

