##  Tienda deportiva: contar productos caros
# Pide el precio de 6 productos al final 
# indica cuántos cuestan más de 100000.
n = 6
contador_productos = 0

for i in range (1,n,1):
    precio = int(input("Por favor ingresa el precio del producto: "))
        
    if precio > 100000:
        contador_productos = contador_productos + 1
    
print("Productos que cuestan mas de 100000: ", contador_productos)


