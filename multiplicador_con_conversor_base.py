def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % 2)
        # E ir dividiendo el decimal
        decimal = int(decimal / 2)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
    return binario
    
##colocar funcion para convertir de hexadecimal a binario pp

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
  

identificador=input()
binario1=str(input())
binario2=str(input())

numero1=0
numero2=0
if identificador=="d":
	numero1=decimal_a_binario(int(binario1))
	numero2=decimal_a_binario(int(binario2))
if identificador=="b":
	numero1=int(binario1)
	numero2=int(binario2)
if identificador=="h":
	numero1=10
	numero2=11
else:
	print("\n Los numeros digitados no corresponde a ninguna de las expresiones: decimal, hexadecimal o binaria")


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
    
print(f"el numero final es:{numero1} y {numero2}")
print("\nMultiplication Result = " + str(multiplicacion))

