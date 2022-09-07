
# def generaMultiplos7(limite):
#     numero = 1
#     listaNumeros = []

#     while numero <= limite:
#         listaNumeros.append(numero * 7)
#         numero = numero + 1
#     return listaNumeros  # Retorna toda la lista creada.

# print(generaMultiplos7(10))


def generadorMultiplos7(limite):
    numero = 1
    while numero <= limite:
        yield numero * 7  # Ceder. La instrucción "yield" genera un objeto iterable.
        numero = numero + 1




    # """ 
    # # print(obtieneMultiplos7)
    # for n in obtieneMultiplos7:
    #     print(n)
    # """

    # next(): Retorna el siguiente elemento de un objeto iterable:



    # Son más eficiente que las funciones tradicionales.
    # Muy útiles con listas de valores infinitos.
    # Entre llamada y llamada, el objeto iterable entra en un estado de pausa (suspensión).