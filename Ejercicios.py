import math

print ("Prograna de calculo de raiz cuadrada")
numero=int(input("Introduce un numero: "))

intentos=0

while numero<0:
    print("No se puede hallar raiz de un numero negativo")

    if intentos==2:
        print("Has consumido demasiados intentos. Finalizando el programa")
        break;

    numero=int(input("Introduce un numero, por favor: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))