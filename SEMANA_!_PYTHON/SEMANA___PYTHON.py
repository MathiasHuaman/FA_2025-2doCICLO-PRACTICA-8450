def ejer1():
    #ASIGNAR VARIABLES

    nombre = input("INGRESA TU NOMBREP: ")
    carrera = input("INGRESA TU CARRERAP: ")

    #IMPRIMIR O ESCRIBIR EN LA CONSOLA

    print(f"\n{nombre}. Bienvenido a FA de {carrera}")
def ejer2():
    print("\"\"MATHIAS\"\"")
def ejer3():
    x = int(input("INGRESE EL VALOR DE X: "))
    y = int(input("INGRESE EL VALOR DE Y: "))

    print("SUMA: ", (x+y))
    print("RESTA: ", (x-y))
    print("MULTIPLICACION: ", (x*y))
    print("DIVISION: ", (x/y))


import math #IMPORTANTE LA LIBRERIA MATH
def ejer4():
    num = float(input("INGRESE UN NUMERO DECIMAL: "))

    print("RAIZ 2: ", math.sqrt(num))
    print("REDONDEADO: " , round(num,0))
    print("AL CUBO: ", math.pow(num,3))
    print("RAIZ 3: ", num ** (1/3))

def ejer5():
    num = input("INGRESE NUMERO: ")

    entero = int(num)
    deci = float(num)

    print("RESTA: ", (entero%2))
    print("DIVISION: ", (deci/3)) 
ejer5()
