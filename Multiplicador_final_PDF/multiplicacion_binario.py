import sys
import subprocess
from funciones import menu1,menu2
from multiplicacion import multiplicacion
from decimal_a_binario import decimal_a_binario
from hexadecimal_a_binario import hexadecimal_a_binario

def Entrada_Datos(bits, factor1,factor2):  # funcion que se encarga de leer y procesar los datos ingresados
  #verificar si los numeros son menores estan detro de los 8 bits
    largofactor1=len(factor1)
    largofactor2=len(factor2)
    if (largofactor1>bits)|(largofactor2>bits):
        print("Numero supera la cantidad de bits")
    else:
        numero1=int(factor1[1:largofactor1])
        numero2=int(factor2[1:largofactor2])
        if factor1[0]==factor2[0]:
            return menu1(factor1[0])
        if factor1[0]=="d":
            if factor2[0]=="b":
                binario1=numero1
                binario2=numero2
                numero1=decimal_a_binario(int(binario1))
                numero2=int(binario2)
                return numero1, numero2
        if factor1[0]=="d":
            if factor2[0]=="h": 
                binario1=numero1
                lista2=list(numero2)
                numero1=decimal_a_binario(int(binario1))
                numero2=hexadecimal_a_binario(lista2)
                return numero1, numero2
        if factor1[0]=="b":
            if factor2[0]=="d":
                binario1=numero1
                binario2=numero2
                numero1=int(binario1)
                numero2=decimal_a_binario(int(binario2))
                return numero1,numero2
        if factor1[0]=="b":
            if factor2[0]=="h":#problemas con el numeros en letras
                binario1=numero1
                #lista2=list(input("Ingrese el numero hexadecimal 2: "))
                numero1=int(binario1)
                #numero2=hexadecimal_a_binario(lista2)
                return numero1, numero2
        if factor1[0]=="h":
            if factor2[0]=="d":
                #lista1=list(input("Ingrese el numero hexadecimal 1: "))
                binario2=numero2
                #numero1=hexadecimal_a_binario(lista1)
                numero2=decimal_a_binario(int(binario2))
                return numero1,numero2
        if factor1[0]=="h":
            if factor2[0]=="b":
                #lista1=list(input("Ingrese el numero hexadecimal 1: "))
                binario2=numero2
                #numero1=hexadecimal_a_binario(lista1)
                numero2=int(binario2)
                return numero1, numero2
        else:
            print("No valido")
###########################################################################
def subproductos(num1, num2):
  if len(num1) > 8 or len(num2) > 8:
    return "Error: los números no pueden tener más de 8 bits"
  resultados = []
  for i in range(len(num2) - 1, -1, -1):
    resultado = int(num1, 2) * int(num2[i])
    resultado_str = format(resultado, 'b').zfill(len(num1))
    resultados.append(resultado_str)
  resultados.reverse()
  return resultados
############################################################################
############################################################################
def export_pdf(bits, factor1, factor2, num1, num2, r, config):
    
    file = open("beamer.tex", "w")

  #comandos básicos de configuración del documento latex
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
    file.write(r"\title{Multiplicador de numeros binarios}")
    file.write("\n")
    file.write(r"\begin{document}")
    file.write("\n")

    file.write(r"    \begin{frame}")
    file.write("\n")
    file.write(r"        \maketitle")
    file.write("\n")
    file.write(r"    \end{frame}")
    file.write("\n")

    config_pres = ("Su archivo de configuracion es: ")
    if (config == ""):
      config_pres = "No hay archivo de configuracion txt"
    #desarrollo
    file.write(r"    \section{Desarrollo de la multiplicacion binaria}")
    file.write("\n")
    file.write(r"    \begin{frame}{Desarrollo de la multiplicacion binaria}")
    file.write("\n")
    file.write(r"        \begin{itemize}")
    file.write("\n")
    file.write(r"        \item Paso 1: conversion a binario de cada factor:")
    file.write("\n")
    file.write(r"        \item    Factor 1 -> ")
    file.write(num1)
    file.write("\n")
    file.write(r"        \item    Factor 2 -> ")
    file.write(num2)
    file.write("\n")
    file.write(r"        \item Desarrollo ")
    file.write("\n")
    file.write(r"        \newline")
    file.write("\n")
    file.write(r"      \hphantom{123456789101112}")
    file.write(num1)
    file.write("\n")
    file.write(r"        \newline")
    file.write(r"      \hphantom{12345678910111}x")
    file.write(num2)
    file.write("\n")
    #fañta pasos
    file.write(r"        \item Resultado de la multiplicacion total: ")
    file.write(r)
    file.write("\n")
    file.write(r"        \end{itemize}")
    file.write("\n")
    file.write(r"    \end{frame}")
    file.write("\n")
    #falta pasos
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
    file.write(r"    \end{document}")
    file.write("\n")
    file.close()

    subprocess.call(["texmaker", "beamer.tex"])








############################################################################
############################################################################
def leer_texto():
  print('ingrese el nombre del archivo de configuracion')
  a = input()
  archivo = (a + '.f')
  with open(archivo, 'r') as documento:
    cont = documento.readline()
    palabras = cont.split()
    lista = []
    for palabra in palabras:
      lista.append(palabra)
      factor1 = lista[3]
      factor2 = lista[5]
      bits = lista[1]
    print("cantidad de bits: ", bits)
    print("el factor 1 es: ", factor1)
    print("el factor 2 es: ", factor2)

  return bits, factor1, factor2, archivo


def proyecto():
    print("Bienvenido al Multiplicador de numeros binarios")
    print("Digite 1 si desea ajuntar un archivo tipo .tx")
    print("Digite 2 si desea utilizar la consola de programacion.")
    pivote=int(input())
    if pivote==1:
        archivo = leer_texto()
        bits = int(archivo[0])
        factor1 = archivo[1]
        factor2 = archivo[2]
        config = archivo[3]
        final = Entrada_Datos(bits, factor1, factor2)
        num1 =(final[0])
        num2 = (final[1])
        nuevovalor=multiplicacion(num1,num2)
        export_pdf(str(bits), factor1, factor2, str(num1),str(num2),str(nuevovalor), config)
        sys.exit()

    if pivote==2:
      print("Bases de los numeros: decimal=d, hexadecimal=h, binario=b")
      print("Digite 1 si sus numeros posee la misma base: ")
      print("Digite 2 si sus numeros posee bases diferentes: ")
      id=int(input())
      bits2=str(input("ingrese la cantidad de bits: "))
      config=''
      if id == 1:
          identificador=str(input("Digite la base de los numeros:" ))
          nuevovalor=menu1(identificador)
          num1,num2=nuevovalor
          numero1=int(num1)
          numero2=int(num2)
          nuevovalor=multiplicacion(numero1,numero2)
          export_pdf(bits2, num1, num2, str(num1),str(num2),str(nuevovalor), config)
          sys.exit()
      if id==2:
          nuevovalor=menu2()
          num1,num2=nuevovalor
          numero1=int(num1)
          numero2=int(num2)
          nuevovalor=multiplicacion(numero1,numero2)
          export_pdf(bits2, num1, num2, str(num1),str(num2),str(nuevovalor), config)
          sys.exit()
          
      else:
          print("no valido")
    
    else:
       ("Valor incorrecto")

if __name__=="__main__":
    proyecto()