import os
from Generadores import generadorMultiplos7
from Generadores2 import devuelveLenguajes
from Operador_while import Operadorwhile
from POO.Cuenta import Cuenta
from POO.Curso import Curso
from POO.Herencia import Estudiante
from POO.HerenciaMultiple import ClaseX
from POO.Persona import Persona
from POO.Polimorfismo import Trabajador, describirPersona
from POO.RelacionesClases import Ciudad, Pais, Urbanizacion
from break_continue_pass import breakContinue, continuee, pass1
from cadenas import cadenas
from concatenacion import concatenarLista
from diccionarios import dicc
from excepciones import exepcion
from factorial import Factorial
from funciones import evaluarSueldoMinimo, saludar
from if_else import If_Else
from if_in import If_in
from ingreso_datos import Ingreso
from modulos.funciones_matematicas import multiplicar
from modulos.modulo import Modulo
from operador_for import operadorFor
from operador_ternario import operadorTernario
from operadores_aritmeticos import division, divisionexacta, matematicas, multiplicacion, petencia, resta, suma
from operadores_logicos import operadorLogico
from paquete1.funciones_cadena import contar_letras
from raise1 import Raise
from range import Rango
from tuplas import tupla
from variables import *
from conversiones import *
from holamundo import Imprimir
from Listas import ReLista
class Menu:
    def __init__(self, titulo, opciones=[]):
        self.titulo=titulo
        self.opciones= opciones
    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        opc = input("Elija la opción [1...{}]:".format(len(self.opciones)))
        return opc
opc = ""
while opc != "34":
    os.system("cls")
    men = Menu("Menu Principal",["1)Imprimir","2)Operacion Listas","3)Variables","4)conversiones", "5)Operaciones matematicas","6)concatenar","7)Cadenas","8)Tuplas","9)Diccionario","10)Ingreso de datos","11)If Else","12)Funciones","13)If in","14)Operadores logicos","15)Operador Ternario","16)Funcion Range","17)Bucles For","18)Factorial","19)Bucle While","20)Brake_continue_pass","21)Generadores","22)Generadores 2.0","23)Exepciones","24)Raise","25)Modulos","26)Paquete","27)Persona","28)Curso","29)Cuenta","30)Herencia","31)Herencia Multiple","32)Polimorfismo","33)Relaciones Clases","34)Salir"])
    opc = men.menu()
    if opc == "1":
        opc1 = ""
        os.system("cls")
        Elementos = (input("Ingrese nombre a imprimir: "))
        if Elementos  == "":
            ele=3
        else:
            ele= Elementos
        resultados = Imprimir(ele)
        while opc1 != "2":
            os.system("cls")
            men1 = Menu("Menu imprimir ",["1)Mostrar", "2)Salir"])
            opc1 = men1.menu()
            if opc1 == "1":
                os.system("cls")
                print("<---Mostrar--->")
                res=resultados.pr()
                input("Presione una tecla para continuar...")                
    elif opc == "2":  
            opc1 = ""
            os.system("cls")
            resultados = ReLista()
            while opc1 != "9":
                os.system("cls")
                men1 = Menu("Menu Operaciones listas",["1)Mostrar Lista", "2)Mostrar un elemento de la lista", "3)Agregar elemento a la lista","4)Ver operacion de listas con posicion", "5)insertar en lista", "6)Indice de lista","7)Remover lista","8)Sacar de lista","9) Salir"])
                opc1 = men1.menu()
                if opc1 == "1":
                    os.system("cls")
                    print("<---Mostrar--->")
                    res=resultados.mostrarLis()
                    print(res)
                    input("Presione una tecla para continuar...")
                elif opc1 == "2":
                    os.system("cls")
                    print("<---Mostar Elemento--->")
                    res=resultados.mostrarLis()
                    print(res)
                    num=len(res)
                    print("<---De acuerdo a la lista escoja una posicion numero positivo y menor a {}--->".format(num))
                    r=int(input("Ingrese Posicion: "))
                    if r==6:
                        print("posicion no encontrada")
                    else:
                        res=resultados.Mostrar1(r)
                    input("Presione una tecla para continuar...")
                elif opc1 == "3":
                    os.system("cls")
                    print("<---Agregar Elemento--->")
                    opc1 = ""
                    while opc1 != "3":
                        os.system("cls")
                        men1 = Menu("Menu de elecion de tipo variable",["1)numero", "2)texto", "3)Salir"])
                        opc1 = men1.menu() 
                           
                        if opc1 =="1":
                            os.system("cls")
                            ele=input("ingrese elemento a agregar: ")
                            res=resultados.agregar(int(ele))
                            input("Presione una tecla para continuar...")
                            
                        elif opc1 == "2":
                            os.system("cls")
                            ele=input("ingrese elemento a agregar: ")
                            res=resultados.agregar(ele)
                            input("Presione una tecla para continuar...")                                 
                elif opc1 == "4":
                    os.system("cls")
                    print("<---View de listas Distintas maneras de ver elementos de lista--->")
                    res=resultados.mostrarLis()
                    print(res)
                    print("============================================ ")

                    resultados.viewlist()
                    input("Presione una tecla para continuar...")
                elif opc1 == "5":
                    os.system("cls")
                    print("<---Insertar en posicion especifica--->")             
                    pos=int(input("Ingrese Posicion a colocar: "))
                    nom=input("ingrese elemento a ingresar: ")
                    resultados.insertar(pos,nom)
                    print(resultados.mostrarLis())
                    input("Presione una tecla para continuar...")

                elif opc1 == "6":
                    os.system("cls")
                    print("<---Indice de elementos--->")             
                    print(resultados.indiceElem())
                    input("Presione una tecla para continuar...")


                elif opc1 == "7":
                    os.system("cls")
                    print("<---remover elementos de la lista--->") 
                    opc1 = ""
                    while opc1 != "3":
                        
                        os.system("cls")
                        print(resultados.mostrarLis())
                        men1 = Menu("Que desea remover ",["1)numero", "2)texto", "3)Salir"])
                        opc1 = men1.menu() 
                           
                        if opc1 =="1":
                            os.system("cls")
                            print(resultados.mostrarLis())
                            ele=input("ingrese elemento a remover: ")
                            res=resultados.remover(float(ele))
                            print(resultados.mostrarLis())
                            input("Presione una tecla para continuar...")
                            
                        elif opc1 == "2":
                            os.system("cls")
                            print(resultados.mostrarLis())
                            ele=input("ingrese elemento a remover: ")
                            res=resultados.remover(ele) 
                            print(resultados.mostrarLis())
                    input("Presione una tecla para continuar...")

                elif opc1 == "8":
                    os.system("cls")
                    print("<---Sacar elemento de la lista--->")             
                    resultados.sacar()
                    print(resultados.mostrarLis())
                    input("Presione una tecla para continuar...")             
    elif opc == "3":  

            opc1 = ""
            os.system("cls")
            
            while opc1 != "2":
                os.system("cls")
                men1 = Menu("Menu Variables",["1)ver variables", "2)Salir"])
                opc1 = men1.menu()
                if opc1 == "1":
                    os.system("cls")
                    print("<---Ver Variables--->")
                    ver()
                    input("Presione una tecla para continuar...")                                    
    elif opc == "4":
        opc1 = ""
        os.system("cls")
        print("<---Ver Conversiones--->")
        mostrarconversiones()
        input("Presione una tecla para continuar...")
    elif opc == "5":
        opc1 = ""
        os.system("cls")
        print("<---Operaciones matematicas--->")
        matematicas()
        while opc1 != "7":
                print()
                men1 = Menu("Menu Operaciones Aritmeticas",["1)Suma","2)Resta","3)Multiplicacion","4)Division","5)Divicion exacta","6)Potencia", "7)Salir"])
                opc1 = men1.menu()
                if opc1 == "1":
                    os.system("cls")
                    print("<---Suma--->")
                    num1=int(input("ingrese primer valor: "))
                    num2=int(input("ingrese segundo valor: "))
                    suma(num1,num2)                    
                    input("Presione una tecla para continuar...")
                elif opc1 == "2":
                    os.system("cls")
                    print("<---Resta--->")
                    num1=int(input("ingrese primer valor: "))
                    num2=int(input("ingrese segundo valor: "))
                    resta(num1,num2)                    
                    input("Presione una tecla para continuar...")
                elif opc1 == "3":
                    os.system("cls")
                    print("<---Multiplicacion--->")
                    num1=int(input("ingrese primer valor: "))
                    num2=int(input("ingrese segundo valor: "))
                    multiplicacion(num1,num2)                    
                    input("Presione una tecla para continuar...")
                elif opc1 == "4":
                    os.system("cls")
                    print("<---Division--->")
                    num1=int(input("ingrese primer valor: "))
                    num2=int(input("ingrese segundo valor: "))
                    division(num1,num2)                    
                    input("Presione una tecla para continuar...")
                elif opc1 == "5":
                    os.system("cls")
                    print("<---Division exacta--->")
                    num1=int(input("ingrese primer valor: "))
                    num2=int(input("ingrese segundo valor: "))
                    divisionexacta(num1,num2)                    
                    input("Presione una tecla para continuar...")
                elif opc1 == "6":
                    os.system("cls")
                    print("<---Potencia--->")
                    num1=int(input("ingrese primer valor: "))
                    num2=int(input("ingrese segundo valor: "))
                    petencia(num1,num2)                    
                    input("Presione una tecla para continuar...")
        input("Presione una tecla para continuar...")
    elif opc == "6":
        opc1 = ""
        os.system("cls")
        print("<---Concatenar Listas--->")
        text1=input("ingrese texto inicial: ")
        text2=input("ingrese texto a concatenar: ")
        print()
        concatenarLista(text1,text2)
        input("Presione una tecla para continuar...")      
    elif opc == "7":
        opc1 = ""
        os.system("cls")
        print("<---Cadenas--->")
        texto=input("ingrese texto: ")
        cadenas(texto)
        input("Presione una tecla para continuar...")     
    elif opc == "8":
        opc1 = ""
        os.system("cls")
        print("<---Tuplas--->")
        tupla()
        input("Presione una tecla para continuar...")  
    elif opc == "9":
        opc1 = ""
        os.system("cls")
        print("<---Diccionario--->")
        dicc()
        input("Presione una tecla para continuar...")     
    elif opc == "10":
        opc1 = ""
        os.system("cls")
        print("<---Ingreso de datos--->")
        Ingreso()
        input("Presione una tecla para continuar...")  
    elif opc == "11":
        opc1 = ""
        os.system("cls")
        print("<---If Else--->")
        If_Else()
        input("Presione una tecla para continuar...")      
    elif opc == "12":
        opc1 = ""
        os.system("cls")
        print("<---Funciones--->")
        while opc1 != "3":
                os.system("cls")
                men1 = Menu("Menu Variables",["1)Saludar", "2)Evaluar Sueldo Minimo","3)Salir"])
                opc1 = men1.menu()
                if opc1 == "1":
                    os.system("cls")
                    print("<---Funcion Saludar--->")
                    print(saludar())
                    input("Presione una tecla para continuar...")
                elif opc1 == "2":
                    os.system("cls")
                    print("<---Funcion Evaluar Sueldo Minimo--->")
                    sueldo=int(input("ingrese su sueldo para calcular: "))
                    evaluarSueldoMinimo(sueldo)
                    input("Presione una tecla para continuar...")   
    elif opc == "13":
        opc1 = ""
        os.system("cls")
        print("<---IF In--->")
        If_in()
        input("Presione una tecla para continuar...")       
    elif opc == "14":
        opc1 = ""
        os.system("cls")
        print("<---Operadores logicos--->")
        operadorLogico()
        input("Presione una tecla para continuar...")
    elif opc == "15":
        opc1 = ""
        os.system("cls")
        print("<---Operador Ternario--->")
        operadorTernario()
        input("Presione una tecla para continuar...")
    elif opc == "16":
        opc1 = ""
        os.system("cls")
        print("<---Funcion Range--->")
        Rango()
        input("Presione una tecla para continuar...") 
    elif opc == "17":
        opc1 = ""
        os.system("cls")
        print("<---Bucles For--->")
        operadorFor()
        input("Presione una tecla para continuar...")  
    elif opc == "18":
        opc1 = ""
        os.system("cls")
        print("<---Factorial--->")
        Factorial()
        input("Presione una tecla para continuar...")
    elif opc == "19":
        opc1 = ""
        os.system("cls")
        print("<---Bucle While--->")
        Operadorwhile()
        input("Presione una tecla para continuar...")
    elif opc == "20":
        opc1 = ""
        os.system("cls")
        print("<---Brake_continue_pass--->")
        while opc1 != "4":
                os.system("cls")
                men1 = Menu("Menu",["1)Break","2)Continue","3)Pass","4)Salir"])
                opc1 = men1.menu()
                if opc1 == "1":
                    os.system("cls")
                    print("<---Break--->")
                    breakContinue()
                    input("Presione una tecla para continuar...")
                elif opc1 == "2":
                    os.system("cls")
                    print("<---Continue--->")
                    continuee()
                    input("Presione una tecla para continuar...") 
                elif opc1 == "3":
                    os.system("cls")
                    print("<---Pass--->")
                    pass1()
                    input("Presione una tecla para continuar...")        
    elif opc == "21":
        opc1 = ""
        os.system("cls")
        print("<---Generadores--->")
        obtieneMultiplos7 = generadorMultiplos7(10)
        print(next(obtieneMultiplos7))
        print("Acá hay 300 líneas de código...")
        print(next(obtieneMultiplos7))
        print("Acá hay 1000 líneas de código...")
        print(next(obtieneMultiplos7))
        input("Presione una tecla para continuar...")
    elif opc == "22":
        opc1 = ""
        os.system("cls")
        print("<---Generadores2--->")
        lenguajesObtenidos = devuelveLenguajes("Python", "Java", "PHP", "Ruby", "JavaScript") 
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        print(next(lenguajesObtenidos))
        input("Presione una tecla para continuar...")
    elif opc == "23":
        opc1 = ""
        os.system("cls")
        print("<---Exepciones--->")
        exepcion()
        input("Presione una tecla para continuar...")
    elif opc == "24":
        opc1 = ""
        os.system("cls")
        print("<---Raise--->")
        nota=int(input("Ingrese Nota: "))
        Raise(nota)
        input("Presione una tecla para continuar...")
    elif opc == "25":
        opc1 = ""
        os.system("cls")
        print("<---Carpeta Modulos--->")
        Modulo()
        input("Presione una tecla para continuar...")
    elif opc == "26":
        opc1 = ""
        os.system("cls")
        print("<---Carpeta Paquete--->")
        while opc1 != "3":
                os.system("cls")
                men1 = Menu("Menu",["1)Multiplicacion","2)Contador de letras","3)Salir"])
                opc1 = men1.menu()
                if opc1 == "1":
                    os.system("cls")
                    print("<---Multiplicacion--->")
                    num1=int(input("ingrese numero a multiplicar: "))
                    num2=int(input("ingrese numero a multiplicar: "))
                    print(multiplicar(num1,num2))
                    input("Presione una tecla para continuar...")
                elif opc1 == "2":
                    os.system("cls")
                    print("<---Contador de Letras--->")
                    res=input("ingrese Texto a contar: ")
                    print(contar_letras(res))
                    input("Presione una tecla para continuar...")    
    elif opc == "27":
        opc1 = ""
        os.system("cls")
        print("<---Persona--->")
        persona1=Persona()
        persona1.apellidos = "García Fuentes"
        print(persona1.apellidos)
        persona1.despertar()
        print(persona1.despierta)

        persona2 = Persona()
        persona2.apellidos = "Paz Torres"
        print(persona2.apellidos)
        # persona2.despertar()
        print(persona2.despierta)
        input("Presione una tecla para continuar...")
    elif opc == "28":
        opc1 = ""
        os.system("cls")
        print("<---Curso--->")
        curso1 = Curso("Matemática", 5, "Ingeniería Civil")
        print(curso1)
        curso1.mostrarDatos()
        input("Presione una tecla para continuar...")  
    elif opc == "29":
        opc1 = ""
        os.system("cls")
        print("<---Cuenta--->")
        cuenta1 = Cuenta("Oscar García", 15000, "Soles")
        print(cuenta1.get_Saldo())
        print(cuenta1.get_Moneda())
        cuenta1.set_Moneda("Dólares")
        print(cuenta1.get_Moneda())
        input("Presione una tecla para continuar...")
    elif opc == "30":
        opc1 = ""
        os.system("cls")
        print("<---Herencia--->")
        estu1 = Estudiante("Torres", "López", "Juan", "Ingeniería Civil")
        print(estu1.mostrarNombreCompleto())
        print(estu1.profesion)
        input("Presione una tecla para continuar...")
    elif opc == "31":
        opc1 = ""
        os.system("cls")
        print("<---Herencia Multiple--->")
        cX1 = ClaseX(15, 21)
        input("Presione una tecla para continuar...")
    elif opc == "32":
        opc1 = ""
        os.system("cls")
        print("<---Polimorfismo--->")
        doc1 = Trabajador()
        describirPersona(doc1)
        input("Presione una tecla para continuar...")
    elif opc == "33":
        opc1 = ""
        os.system("cls")
        print("<---Relaciones Clases--->")
        pais1 = Pais("Perú", "Martín Vizcarra")
        print(pais1)

        ciudad1 = Ciudad("Chiclayo", 150000, pais1)
        print(ciudad1)

        urba1 = Urbanizacion("María de los Angeles", ciudad1)
        print(urba1)
        input("Presione una tecla para continuar...")
    print("Lo espermos en una proxima ocasión")    