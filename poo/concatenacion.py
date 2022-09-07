from traceback import print_tb


def concatenarLista(texto1,texto2):
    textoFinal = texto1 + " " + texto2
    print("<----------texto concatenado (txt1+''+txt2)---------->")
    print(textoFinal)
    print()
    print("<----------Impresion con comodines---------->")
    print("El saludo es: %s %s" % (texto1, texto2))
    print()
    print("<----------Impresion con .format---------->")
    saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
    print(saludoFinal)
    print()
    print("<----------Impresion con .format segunda forma---------->")
    saludoFinal2 = "Saludo: {y} {x}".format(x=texto2, y=texto1)
    print(saludoFinal2)