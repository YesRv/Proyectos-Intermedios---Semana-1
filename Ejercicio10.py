## Academia de baile: asistencia
# Pide la cantidad de clases asistidas por un estudiante en un mes

# menos de 5 → asistencia baja 
# entre 5 y 8 → asistencia media 
# 9 o más → asistencia alta

nombre = str(input("Nombre del estudiante: "))
asistencias = int(input("Por favor ingresa el numero de asistencias de "+ nombre +": "))

if asistencias <= 5:
    print(nombre, ": Asistencia Baja")
elif asistencias <=8:
    print(nombre, ": Asistencia Media")
elif asistencias >=9:
    print(nombre, ": Asistencia Alta")
else:
    print("Valor no valido")
