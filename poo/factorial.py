def Factorial():
    numero = int(input("Ingrese un número: "))

    factorial = 1
    for n in range(1, (numero + 1)):
        factorial = factorial * n

    print("El factorial de {0} es: {1}".format(numero, factorial))
