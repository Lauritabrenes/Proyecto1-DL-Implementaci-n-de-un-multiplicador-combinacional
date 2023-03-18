from funciones import menu1,menu2
from multiplicacion import multiplicacion

def multiplicador_binario():
    print("Bases de los numeros: decimal=d, hexadecimal=h, binario=b")
    print("Digite 1 si sus numeros posee la misma base: ")
    print("Digite 2 si sus numeros posee bases diferentes: ")
    id=int(input())
    if id == 1:
        identificador=str(input("Digite la base de los numeros:" ))
        nuevovalor=menu1(identificador)
        num1,num2=nuevovalor
        numero1=int(num1)
        numero2=int(num2)
        nuevovalor=multiplicacion(numero1,numero2)
        print("\nMultiplication Result = " + str(nuevovalor))
    if id==2:
        nuevovalor=menu2()
        num1,num2=nuevovalor
        numero1=int(num1)
        numero2=int(num2)
        nuevovalor=multiplicacion(numero1,numero2)
        print("\nMultiplication Result = " + str(nuevovalor))
    else:
        print("no valido")

if __name__=="__main__":
    multiplicador_binario()