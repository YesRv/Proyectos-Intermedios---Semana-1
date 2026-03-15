 ## Cine: entrada según edad
Niños = 8000
Adultos = 12000
Mayores = 9000

edad = int (input("Por favor ingresa la edad: "))

if edad <= 12:
    print("El valor de tu entrada es: ", Niños)
elif edad <=59:
    print("El valor de tu entrada es: ", Adultos)
elif edad >=60:
    print ("El valor de tu entrada es: ", Mayores)
else:
    print("Edad no valida")