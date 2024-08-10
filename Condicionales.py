print("Programa de Becas 2024")
distancia_escuela=int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce Salario anual de tus padres: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:

    print("Tienes derecho a beca")

else:

    print("No tienes derecho a beca")


print("Asignaturasoptativas Año 2024")
print("Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y Accesibilidad")
opcion=input ("Escribe la asignatura escogida: ")

asignatura=opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
        print("Asignatura escogida " + asignatura)
else:
        print("No existe")