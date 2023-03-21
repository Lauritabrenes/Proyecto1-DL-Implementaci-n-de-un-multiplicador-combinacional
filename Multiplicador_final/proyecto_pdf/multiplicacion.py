def multplicacionbinaria(num1, num2):
    i = 0
    residuo = 0 
    sum = [] 
    productobinario = 0 
    while num1 != 0 or num2 != 0:
        sum.insert(i, (((num1 % 10) + (num2 % 10) + residuo) % 2))
        residuo = int(((num1 % 10) + (num2 % 10) + residuo) / 2)
        num1 = int(num1/10)
        num2 = int(num2/10)
        i = i+1
    if residuo != 0:
        sum.insert(i, residuo)
        i = i+1
    i = i-1
    while i >= 0:
        productobinario = (productobinario * 10) + sum[i]
        i = i-1
    return productobinario


def multiplicacion(numero1,numero2):
    multiplicacion = 0
    factor = 1
    bin1 =int(numero1) 
    bin2 = int(numero2)
    while bin2 != 0:
        digito = bin2 % 10
        if digito == 1:
            bin1 = bin1 * factor
            multiplicacion = multplicacionbinaria(bin1, multiplicacion)
        else:
            bin1 = bin1 * factor
        bin2 = int(bin2/10)
        factor = 10
    return multiplicacion