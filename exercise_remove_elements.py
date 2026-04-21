# Ejercicio 4: Remover elementos en posiciones específicas

def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """
    if not lista:
        return None
    maximo = lista[0]
    for numero in lista[1:]:
        if numero > maximo:
            maximo = numero
    return maximo

