##Tienda de mascotas: alimento por tipo de animal

animal1 = "Perro"
animal2 = "Gato"
animal3 = "Conejo"
alimento_Perro = ("Pollito, Huesos crudos, Croquetas")
alimento_Gato = ("Pollito, Lata de atún, churus")
alimento_Conejo = ("Zanahoria, Lechuga, Tomate")

print ("Sugerencia de alimento por tipo de mascota ")
mascota = str (input("Ingresa tu mascota: "))

if mascota == "Perro":
    print("Recomendacion de alimento: ",alimento_Perro)
elif mascota == "Gato":
    print("Recomendacion de alimento: ",alimento_Gato)
elif mascota == "Conejo":
    print("Recomendacion de alimento: ",alimento_Conejo)
else:
    print ("Mascota no encontrada")