## Gimnasio: promedio de rendimiento semanal

bajo = 0
medio = 0
alto = 0

for i in range(1, 6):
    print("\n--- Persona", i, "---")
    
    nombre = input("Ingresa el nombre de la persona: ")
    dias = int(input("Ingresa los días asistidos en la semana: "))
    minutos = int(input("Ingresa los minutos promedio entrenados por día: "))

    if dias < 3:
        print(nombre, "tiene bajo compromiso")
        bajo = bajo + 1

    elif dias >= 3 and dias <= 4:
        print(nombre, "tiene compromiso medio")
        medio = medio + 1

    else:
        print(nombre, "tiene compromiso alto")
        alto = alto + 1

print("\n--- RESULTADO FINAL ---")
print("Personas con bajo compromiso:", bajo)
print("Personas con compromiso medio:", medio)
print("Personas con compromiso alto:", alto)