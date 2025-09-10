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



ejer2()