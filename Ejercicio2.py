## Gimnasio ingreso por edad
## Pide la edad de una persona y muestra a qué grupo pertenece.
## CLASES 
##menor de 13 → no puede ingresar 
## de 13 a 17 → clase juvenil 
## de 18 a 59 → clase general 
## 60 o más → clase senior 

edad = int(input("Por favor ingrese su edad: "))

if edad <=13:
    print("No puede ingresar")
elif edad >=14 and edad <= 17:
    print("Clase juvenil ")
elif edad < 59:
    print("Clase general")
elif edad >=60:
    print("Clase Senior")
else:
    print("Edad no valida")