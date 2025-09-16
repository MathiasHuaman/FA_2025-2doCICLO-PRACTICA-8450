def ejer1():
    edad = int(input("INGRESE UNA EDAD: "))
    
    if edad < 18:
        print("MENOR DE EDAD")
    else:
        if edad >= 18 and edad <=64:
            print("ADULTO")
        else:
            print("ADULTO MAYOR")

def ejer2():

    año= int(input("INGRESE UN AÑO: "))

    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        es_bisiento = True
    else:
        es_bisiento = False

    es_par= año % 2 == 0

    if es_bisiento:
       print(f"El año {año} es bisiesto")
    else:
       print(f"El año {año} no es bisiesto")
    if es_par:
       print(f"El año {año} es par")
    else:
       print(f"El año {año} es impar")

def ejer3():
     monto = float(input("INGRESE EL MONTO EN SOLES: "))

     print("\n1. DOLARES\n2. EUROS")

     opcion = int(input("\nIngrese una opcion: "))

     match opcion:
         case 1: print("DOLARES: " ,(monto/3.75))
         case 2: print("EUROS: " ,(monto/4.05))  
         case _: print("OPCION INCORRECTA")

import math

def ejer4():
    print("BIENVENIDO AL SISTEMA DE CALCULOS DE AREAS\n")
    print("1. Cuadrado")
    print("2. Rectangulo")
    print("3. Triangulo")
    print("4. Circulo\n")

    opcion = int(input("INGRESE UNA OPCION: "))

    match opcion:
        case 1: 
            lado=int(input("INGRESE LADO: "))
            print("ÁREA: ", lado*lado)
        case 2:
            bse=int(input("INGRESE LA BASE: "))
            alt=int(input("INGRESE LA ALTURA: "))
            print("ÁREA RECTANGULO: " , (bse*alt))
        case 3:
             bse2=int(input("INGRESE LA BASE: "))
             alt2=int(input("INGRESE LA ALTURA: "))
             print("ÁREA TRIÁNGULO: " , (bse2*alt2)/2)
        case 4:
            radio=int(input("INGRESA EL RADIO: "))
            print("ÁREA DEL CIRCULO: ", (round(math.pi * radio**2),2))

        case _: print("OPCIÓN INCORRECTA")





ejer4()