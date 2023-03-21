"""establecemos una operacion para realizar la multiplicacion de dos nuemros
a partir de sacar los modulos de ambos numeors y rescatado y residuo de manera
que este sera la suma de los nuemros ya multiplicados"""
def multplicacionbinaria(num1, num2):
    i = 0#el pivote nos ayudara para multiplicar cada parte de la cadena de bits
    residuo = 0  # el residuo es la suma al final de la multiplicacion
    sum = [] #es establece una matriz para guardar los numeros
    productobinario = 0 #resultado final de la multiplicacion
  #aplicamos las reglas de la multiplicacion binaria 
    #1. 0*0=0; 2. 1*0=0; 3.0*1=0; 4.1*1=1
    #entoces si ambos numeros no iguales a cero,
    #creamos un while donde a la funcion suma se le inserta
    
    while num1 != 0 or num2 != 0:
        sum.insert(i, (((num1 % 10) + (num2 % 10) + residuo) % 2))
        residuo = int(((num1 % 10) + (num2 % 10) + residuo) / 2)
        num1 = int(num1/10)
        num2 = int(num2/10)
        i = i+1
  #si el residuo no contiene un numero cerro que cumpla las cuatro reglas,
  #entoces se insertara en una matriz de sumas
    if residuo != 0:
        sum.insert(i, residuo)
        i = i+1
    i = i-1
    while i >= 0:
        productobinario = (productobinario * 10) + sum[i]
        i = i-1
    return productobinario
  
multiplicacion = 0
factor = 1
binario1 = 11
binario2 = 0
#antes de llamar la funcion multiplicacion de binarios hay que verificar si el multiplicador es diferente de cero ya que de lo contrario el resultado sera cero.
#pasando ese primer paso se debe de multiplicar cada digito del multiplicando con el multiplicador demanera que se respecte las regalas de la multiplicacion binaria
#por ultimo se debe de pasar todos los numeros de derecha a izquierda hasta terminar todos los digitos de ser multiplicados

while binario2 != 0:
    digito = binario2 % 10
    if digito == 1:
        binario1 = binario1 * factor
        multiplicacion = multplicacionbinaria(binario1, multiplicacion)
    else:
        binario1 = binario1 * factor
    binario2 = int(binario2/10)
    factor = 10
print("\nMultiplication Result = " + str(multiplicacion))




