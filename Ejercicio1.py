## Heladeria sabor mas pedido 
## Sabores disponibles: Vainilla, Chocolate, Fresa

Vainilla = 0
Chocolate = 0
Fresa = 0

while Vainilla + Chocolate + Fresa < 5:

    sabor_helado = int (input ("Por favor ingresa el sabor que quieres: 1. Vainilla  2. Chocolate  3. Fresa "))
    if  sabor_helado == 1:
        print("Elegiste Vainilla ")
        Vainilla = Vainilla + 1
    elif sabor_helado == 2:
        print ("Elegiste Chocolate ")
        Chocolate = Chocolate + 1
    elif sabor_helado == 3:
        print ("Elegiste Fresa ")
        Fresa = Fresa + 1
    else:
        print (" Sabor no valido ")

print ("Vainilla = ", Vainilla)
print ("Chocolate= ", Chocolate)
print ("Fresa= ", Fresa)