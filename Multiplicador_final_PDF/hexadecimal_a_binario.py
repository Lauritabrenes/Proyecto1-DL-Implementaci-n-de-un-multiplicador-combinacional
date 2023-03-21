from decimal_a_binario import decimal_a_binario
def hexadecimal_a_decimal(hexa):
    decimal = 0
    potencia=(len(hexa)-1)
    for x in hexa:
        valor=x*((16)**potencia)
        decimal += valor
        potencia=potencia-1
    return decimal
        

def hexadecimal_a_binario(lista):
    for x in range(len(lista)):
        if lista[x]=="a":
            lista[x]="10"
        if lista[x]=="b":
            lista[x]="11"
        if lista[x]=="c":
            lista[x]="12"
        if lista[x]=="d":
            lista[x]="13"
        if lista[x]=="e":
            lista[x]="14"
        if lista[x]=="f":
            lista[x]="15"
        else:
             lista=lista
    nuevalista=[int(x) for x in lista]
    numerodecimal=hexadecimal_a_decimal(nuevalista)
    numerobinario=decimal_a_binario(numerodecimal)
    return numerobinario
