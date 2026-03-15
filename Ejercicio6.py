## Parqueadero: cobro por horas 
## Pide cuántas horas estuvo un carro en un parqueadero. 
## Reglas: 
## primera hora = 5000 
## Cada hora adicional = 3000 
## Muestra el total a pagar.
hora_parqueadero = 5000
hora_adicional = 3000

horas = int(input("Ingresa las horas de uso del parqueadero: "))

if horas == 1:
    total = hora_parqueadero * horas
    print ("Costo del parqueadero: ", total)
elif horas >= 2:
    total = (horas - 1) * hora_adicional + hora_parqueadero
    print ("Costo del parqueadero: ", total)
else:
    print("Valor no valido")