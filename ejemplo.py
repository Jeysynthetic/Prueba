print("Hola mundo")


def mensajes():
    print('hola,como estas?')


mensajes()


def suma(num1, num2): #funciones

    resultado=num1+num2

    return resultado


print (suma(5, 7))


print (suma(2, 3))


def suma (num1, num2):

    resultado=num1+num2

    return resultado


almacena_resultado = suma (5,8)

print (almacena_resultado)


miLista=["Maria", "Guillermo", "Dulce", "Jeys"]

print(miLista[:2])

print(miLista.index("Jeys"))

print("Dulce" in miLista)


mitupla = ("Jeys", 13, 1, 25)
print(mitupla[1])


print(("Programa de notas"))

nota_alumno=input("Introduce la nota")
def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspendido"
    return valoracion

print(evaluacion(int(nota_alumno)))

print("Verificacion de accesp")

edad_usuario=int(input("Introduce tu edad: "))

if edad_usuario<18:
    print("No puedes pasar")
elif edad_usuario>100:
    print("Edad incorrecta")
else:
    print("Puedes pasa")

print("Programa listo")


