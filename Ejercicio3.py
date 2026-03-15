##  Cafetería: total de una compra sencilla

Cafe = 4000
Te = 3500
Jugo = 5000

print ("// MENU CAFETERIA //")
print ("1. Cafe")
print ("2. Te")
print ("3. Jugo")

pedido = int(input (" Por favor ingrese su pedido: "))
n_tazas = int(input("Ingrese cuantas tazas desea: "))

if pedido == 1:
    total = Cafe * n_tazas
    print ("Total del pedido: ", total)
elif pedido == 2:
    total = Te * n_tazas
    print ("Total del pedido: ", total)
elif pedido == 3:
    total = Jugo * n_tazas
    print (" Total del pedido: ", total)
else:
    ("Pedido no valido")
    