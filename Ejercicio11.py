##Ejercicios intermedios
## 11. Heladería: factura de varios clientes

total_vendido = 0
clientes_atendidos = 0

cono = 0
vaso = 0
banana = 0
## Declarar mi condicion para terminar el bucle o si no nunca termina
seguir = "si"

while seguir == "si":
    print("\n--- NUEVO CLIENTE ---")
    
    producto = input("Ingrese el producto (cono, vaso, banana split): ")
    cantidad = int(input("Ingrese la cantidad de producto que desea: "))

    if producto == "cono":
        total = cantidad * 3000
        cono = cono + cantidad

    elif producto == "vaso":
        total = cantidad * 4000
        vaso = vaso + cantidad

    elif producto == "banana split":
        total = cantidad * 9000
        banana = banana + cantidad

    else:
        print("Producto no válido")
        total = 0

    print("Total a pagar del cliente:", total)

    total_vendido = total_vendido + total
    clientes_atendidos = clientes_atendidos + 1

    seguir = input("¿Desea ingresar otro cliente? (si/no): ")

print("\n--- RESUMEN FINAL ---")
print("Total vendido:", total_vendido)
print("Clientes atendidos:", clientes_atendidos)

if cono > vaso and cono > banana:
    print("El producto más pedido fue: cono")

elif vaso > cono and vaso > banana:
    print("El producto más pedido fue: vaso")

elif banana > cono and banana > vaso:
    print("El producto más pedido fue: banana split")
else:
    print("Hubo empate entre dos o más productos")