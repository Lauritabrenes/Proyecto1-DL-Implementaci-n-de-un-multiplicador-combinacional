from decimal_a_binario import decimal_a_binario
from hexadecimal_a_binario import hexadecimal_a_binario
def menu1(identificador):
    numero1=0
    numero2=0
    if identificador=="d":
        binario1=str(input("Ingrese el numero 1: "))
        binario2=str(input("Ingrese el numero 2: "))
        numero1=decimal_a_binario(int(binario1))
        numero2=decimal_a_binario(int(binario2))
        return numero1,numero2
    if identificador=="b":
        binario1=str(input("Ingrese el numero 1: "))
        binario2=str(input("Ingrese el numero 2: "))
        numero1=int(binario1)
        numero2=int(binario2)
        return numero1, numero2
    if identificador=="h":
        lista1=list(input("Ingrese el numero hexadecimal 1: "))
        lista2=list(input("Ingrese el numero hexadecimal 2: "))
        numero1=hexadecimal_a_binario(lista1)
        numero2=hexadecimal_a_binario(lista2)
        return numero1,numero2
    else:
        print("No valido")

def menu2():
    identificador1=str(input("Digite la base del primer numero:" ))
    identificador2=str(input("Digite la base del segundo numero:" ))
    numero1=0
    numero2=0
    if identificador1==identificador2:
        return menu1(identificador1)
    if identificador1=="d":
        if identificador2=="b":
            binario1=str(input("Ingrese el numero 1: "))
            binario2=str(input("Ingrese el numero 2: "))
            numero1=decimal_a_binario(int(binario1))
            numero2=int(binario2)
            return numero1, numero2
    if identificador1=="d":
        if identificador2=="h":
            binario1=str(input("Ingrese el numero 1: "))
            lista2=list(input("Ingrese el numero hexadecimal 2: "))
            numero1=decimal_a_binario(int(binario1))
            numero2=hexadecimal_a_binario(lista2)
            return numero1, numero2
    if identificador1=="b":
        if identificador2=="d":
            binario1=str(input("Ingrese el numero 1: "))
            binario2=str(input("Ingrese el numero 2: "))
            numero1=int(binario1)
            numero2=decimal_a_binario(int(binario2))
            return numero1,numero2
    if identificador1=="b":
        if identificador2=="h":
            binario1=str(input("Ingrese el numero 1: "))
            lista2=list(input("Ingrese el numero hexadecimal 2: "))
            numero1=int(binario1)
            numero2=hexadecimal_a_binario(lista2)
            return numero1, numero2
    if identificador1=="h":
        if identificador2=="d":
            lista1=list(input("Ingrese el numero hexadecimal 1: "))
            binario2=str(input("Ingrese el numero 2: "))
            numero1=hexadecimal_a_binario(lista1)
            numero2=decimal_a_binario(int(binario2))
            return numero1,numero2
    if identificador1=="h":
        if identificador2=="b":
            lista1=list(input("Ingrese el numero hexadecimal 1: "))
            binario2=str(input("Ingrese el numero 2: "))
            numero1=hexadecimal_a_binario(lista1)
            numero2=int(binario2)
            return numero1, numero2
    else:
        print("No valido")