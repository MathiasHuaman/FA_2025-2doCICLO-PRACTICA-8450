def ejer1():
    edad=int(input("INGRESE SU EDAD: "))

    if edad >=18:
        print ("TU PUEDES VOTAR :D")

        if edad >= 25:
            print("CANDIDATO PARA UN CARGO POLITICO :D")
        else:
            print ("NO ES CANDIDATO PARA EJERCER UN CARGO POLITICO D:")
    else:
        print("TU NO PUEDES VOTAR D:")
        print("TU NO PUEDES EJERCER UN CARGO POLITICO D:")

def ejer2():
    lado1 = int(input("INGRESE LADO1: "))
    lado2 = int(input("INGRESE LADO2: "))
    lado3 = int(input("INGRESE LADO3: "))

    if (lado1==lado2==lado3):
        print("EQUILATERO")
    elif lado1 == lado2 or lado1==lado3:
        print("ISOSCELES")
    else:
        print("ESCALENO")

ejer2()
     


