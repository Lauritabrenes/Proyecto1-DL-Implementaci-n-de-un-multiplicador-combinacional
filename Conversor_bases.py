def decimal_2_binary(decimal1,deciamal2):
    if decimal1 & decimal2 <= 0:
        return "0"
    # variable que almacena el resultado
    binario_numero1 = ""
    binario_numero2 = ""
    # Mientras los decimales no sean 0
    while decimal1 >0 | decimal2 >0:
        # Es 1 o 0, el residuo lo indica
        residuo1 = int(decimal1 % 2)
        residuo2 = int(decimal2 % 2)
        # E ir dividiendo el decimal
        decimal1 = int(decimal1 / 2)
        decimal2 = int(decimal2 / 2)
        # Se refleja la conversion construyendo el binario
        binario_numero1 = str(residuo1) + binario_numero1
        binario_numero2 = str(residuo2) + binario_numero2
    return (binario_numero1, binario_numero2)


def hexadecimal_a_decimal(hexadecimal):
    # Convertir a minúsculas por simplicidad
    hexadecimal = hexadecimal.lower()
    # La debemos recorrer del final al principio, así que la invertimos
    hexadecimal = hexadecimal[::-1]
    decimal = 0
    posicion = 0
    for digito in hexadecimal:
        # 10 para la A, 9 para el 9, 11 para la B, etc..
        valor = obtener_valor_real(digito)
        elevado = 16 ** posicion
        equivalencia = elevado * valor
        decimal += equivalencia
        posicion += 1
    return decimal

def entradas_del_multiplicador():
    bases_soportadas = ["binario", "decimal", "hexadecimal", ]

    base_origen_numeroA = input("""Digite la base del número que usará para numeroA: [b, d, h]: """)
    base_origen_numeroB = input("""Digite la base del número que usará para numeroB: [b, d, h]: """)
    print ("Solo se pueden usar numeros con una cantidad máxima de 8 bits")


    if base_origen_numeroA | base_origen_numeroB not in bases_soportadas:
        print("La base que ingreso para alguno de los numeros no está disponible, solo se trabaja binario,decimal,hexadecimal")
        return
    if base_origen_numeroA!=base_origen_numeroB:
        print ("Ambos numeros deben tener la misma base")
        return
    numeroA = input(
        f"Esta usando base {base_origen_numeroA}. Ingrese el número A que utilizara: ")
    numeroB = input(
        f"Esta usando base {base_origen_numeroB}. Ingrese el número B que utilizara: ")

    base_destino = input("""
b - Binario
d - Decimal
h - Hexadecimal
Elige la base a la que conviertes: [2, 8, 10, 16]: """)
    return (base_origen, numeroA,numeroB, base_destino)