def remove_elements(lista):
    """
    Remueve el primer, quinto y sexto elemento de la lista.
    La función debe funcionar con listas de cualquier tamaño.

    Args:
        lista: Una lista de elementos

    Returns:
        La lista después de remover los elementos indicados
    """
    elementos_lista = len(lista)

    if elementos_lista >= 6:
        del lista[0]
        del lista[4]
        del lista[3]
        return lista

    if elementos_lista == 5:
        del lista[0]
        del lista[2]
        return lista

    if elementos_lista != 0 and elementos_lista < 5:
        del lista[0]
        return lista

    if elementos_lista == 0:
        return lista