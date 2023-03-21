import subprocess
import sys
import decimal_a_binario



def export_pdf(bits, numero1, numero2, binario1, binario2, r, pasos, config, decimal_a_binario):

    file = open("beamer.tex" , "w")

# -----------------------------------------------------
#------------------------------------------------ Primera Diapo. Portada y configuración del documento latex
# -----------------------------------------------------

  
    file.write(r"\documentclass[11pt]{beamer}")
    file.write("\n")
    file.write(r"\usetheme{Warsaw}")
    file.write("\n")
    file.write(r"\usepackage[utf8]{inputenc}")
    file.write("\n")
    file.write(r"\usepackage[spanish]{babel}")
    file.write("\n")
    file.write(r"\usepackage{amsmath}")
    file.write("\n")
    file.write(r"\usepackage{amsfonts}")
    file.write("\n")
    file.write(r"\title{Implementacion con Multiplicador combinacional}")
    file.write("\n")
    file.write(r"\begin{document}")
    file.write("\n")

    file.write(r"    \begin{frame}")
    file.write("\n")
    file.write(r"        \maketitle")
    file.write("\n")
    file.write(r"    \end{frame}")
    file.write("\n")

# -----------------------------------------------------
#------------------------------------------------ Segunda Diapo
# En la segunda diapositiva debe indicar los valores que se leyeron en la entrada de usuario (operandos,cantidad de bits, nombre del archivo de configuración)
# -----------------------------------------------------

    config_pres=("Su archivo de configuracion es: ")

    if (config==""):
           
        file.write(r"    \section{Grupo 20}")
        file.write("\n")
        file.write(r"    \begin{frame}{Valores de entrada de usuario}")
        file.write("\n")
        file.write(r"        \begin{itemize}")
        file.write("\n")
        file.write(r"        \item Cantidad de bits de los factores a multiplicar es : ")
        file.write(bits)
        file.write("\n")
        file.write(r"        \item Factor 1: ")
        file.write(numero1)
        file.write("\n")
        file.write(r"        \item Factor 2: ")
        file.write(numero2)
        file.write("\n")
        file.write(r"        \item ")
        file.write(config_pres)
        file.write(config)
        file.write("\n")
        file.write(r"        \end{itemize}")
        file.write("\n")
        file.write(r"    \end{frame}")
        file.write("\n")

# -----------------------------------------------------
#------------------------------------------------ Tercera Diapo.
#  Las siguientes diapositivas deben demostrar el desarrollo completo de la multiplicación binaria y el resultado final.
# -----------------------------------------------------
   
    file.write(r"    \section{Desarrollo de la multiplicacion binaria}")
    file.write("\n")
    file.write(r"    \begin{frame}{Desarrollo de la multiplicacion binaria}")
    file.write("\n")
    file.write(r"        \begin{itemize}")
    file.write("\n")
    file.write(r"        \item Paso 1: conversion a binario de cada factor:")
    file.write("\n")
    file.write(r"        \item    Factor 1 -> ")
    file.write(binario1)
    file.write("\n")
    file.write(r"        \item    Factor 2 -> ")
    file.write(binario2)
    file.write("\n")
    file.write(r"        \item Desarrollo ")
    file.write("\n")
    file.write(r"        \newline")
    file.write("\n")
    file.write(r"      \hphantom{123456789101112}")
    file.write(binario1)
    file.write("\n")
    file.write(r"        \newline")
    file.write(r"      \hphantom{12345678910111}x")
    file.write(binario2)
    file.write("\n")

# -----------------------------------------------------
# ----------------------------------------------------- rango
# -----------------------------------------------------
 
    i=len(pasos)
    k=0   

    if k<i:
        file.write(r"        \newline")
        file.write(r"      \hphantom{123456789101112}")
        file.write(pasos[0])
        file.write("\n")
        k=k+1
        if k < i:
            file.write(r"        \newline")
            file.write(r"      \hphantom{12345678910111}")
            file.write(pasos[1])
            file.write("\n")
            k=k+1
            if k < i:     
                file.write(r"        \newline")
                file.write(r"      \hphantom{1234567891011}")
                file.write(pasos[2])
                file.write("\n")
                k=k+1
                if k < i: 
                    file.write(r"        \newline")
                    file.write(r"      \hphantom{123456789101}")
                    file.write(pasos[3])
                    file.write("\n")
                    k=k+1
                    if k < i: 
                        file.write(r"        \newline")
                        file.write(r"      \hphantom{12345678910}")
                        file.write(pasos[4])
                        file.write("\n")
                        k=k+1
                        if k < i: 
                            file.write(r"        \newline")
                            file.write(r"      \hphantom{1234567891}")
                            file.write(pasos[5])
                            file.write("\n")
                            k=k+1
                            if k < i: 
                                file.write(r"        \newline")
                                file.write(r"      \hphantom{123456789}")
                                file.write(pasos[6])
                                file.write("\n")
                                k=k+1
                                if k < i:
                                    file.write(r"        \newline")
                                    file.write(r"      \hphantom{12345678}")
                                    file.write(pasos[7])
                                    file.write("\n")
                                    


                                
    file.write(r"        \item Resultado de la multiplicacion total: ")
    file.write(r)
    file.write("\n")
    file.write(r"        \end{itemize}")
    file.write("\n")
    file.write(r"    \end{frame}")
    file.write("\n")

    if int(bits) == 9:
        file.write(r"        \newline")
        file.write(r"      \hphantom{12345678910111213}")
        file.write(pasos[7])
        file.write("\n")
        file.write(r"        \newline")
        file.write(r"      \hphantom{123456789101112}")
        file.write(pasos[6])
        file.write("\n")
        file.write(r"        \newline")
        file.write(r"      \hphantom{123456789101112}")
        file.write(pasos[5])
        file.write("\n")
        file.write(r"        \newline")
        file.write(r"      \hphantom{123456789101112}")
        file.write(pasos[4])
        file.write("\n")
        file.write(r"        \newline")
        file.write(r"      \hphantom{123456789101112}")
        file.write(pasos[3])
        file.write("\n")
        file.write(r"        \newline")
        file.write(r"      \hphantom{12345678910111}")
        file.write(pasos[2])
        file.write("\n")
        file.write(r"        \newline")
        file.write(r"      \hphantom{1234567891011}")
        file.write(pasos[1])
        file.write("\n")
        file.write(r"        \newline")
        file.write(r"      \hphantom{123456789101}")
        file.write(pasos[0])
        file.write("\n")
        file.write(r"        \item Resultado de la multiplicacion total: ")
        file.write(r)
        file.write("\n")
        file.write(r"        \end{itemize}")
        file.write("\n")
        file.write(r"    \end{frame}")
        file.write("\n")



# -----------------------------------------------------
#------------------------------------------------ Ultima Diapositiva
# -----------------------------------------------------  
    #Título 
    file.write(r"    \section{Proyecto 1}")
    file.write("\n")
    #Subtitulo
    file.write(r"    \section{Implementación de un Multiplicador Combinacional}")
    file.write("\n")
    #Universidad
    file.write(r"    \section{Instituto Tecnologico de Costa Rica}")
    file.write("\n")
    file.write(r"    \begin{frame}{Instituto Tecnologico de Costa Rica}")
    #Sede
    file.write(r"    \section{Centro Academico de Alajuela}")
    #Curso    
    file.write(r"        Curso Diseno Logico ")
    file.write("\n")
    file.write(r"        \newline")
    file.write("\n")
    file.write("\n")
    #Participantes    
    file.write(r"        Alumnos:")
    file.write("\n")
    file.write(r"        \begin{itemize}")
    file.write("\n")
    file.write(r"        \item Laura Elena Brenes Espinoza")
    file.write("\n")
    file.write(r"        \item Francisco Javier Suarez ")
    file.write("\n")
    file.write(r"        \item Austin Johan Moya Vargas")
    file.write("\n")
    file.write(r"        \item Samuel Montenegro")
    file.write("\n")
    file.write(r"        \end{itemize}")
    file.write("\n")
    #Semestre y Año
    file.write("\n")
    file.write(r"        I Semestre 2023")
    file.write("\n")
    file.write(r"    \end{frame}")
    file.write("\n")
    file.close()

    subprocess.call(["texmaker", "beamer.tex"])


#función para leer un archivo de texto, no recibe nada y retorna 3 strings
def leer_texto():
    print('ingrese el nombre del archivo de configuracion')
    a = input()
    archivo=(a+'.f')

    with open(archivo,'r') as documento:
        cont = documento.readline()
        palabras = cont.split()
        lista = []
        for palabra in palabras:
            lista.append(palabra)
            
        numero1 = lista[3]
        numero2 = lista[5]
        bits = lista[1]
        
        print("cantidad de bits: ", bits)
        print("el factor 1 es: ",  numero1)
        print("el factor 2 es: ", numero2)

    return bits, numero1, numero2, archivo    

## funciones

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
            binario1=str(input("Ingrese el numero_1: "))
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


