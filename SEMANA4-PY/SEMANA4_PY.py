def ejer1():
    edad = int(input("INGRESE UNA EDAD: "))
    
    if edad < 18:
        print("MENOR DE EDAD")
    else:
        if edad >= 18 and edad <=64:
            print("ADULTO")
        else:
            print("ADULTO MAYOR")


ejer1()