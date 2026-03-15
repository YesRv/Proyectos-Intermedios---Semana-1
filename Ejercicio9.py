##9. Spa: servicio disponible
# # Pide al usuario qué servicio desea y muestra un mensaje confirmando  
#En un spa hay estos servicios:
# masaje 
# facial 
# manicure 

servicio = ("Masaje, Facial, Manicure")

pedido = str(input("¿Que servicio desea?  "))

if pedido == "Masaje":
    print ("Excelente a escogido Masaje")
elif pedido == "Facial":
    print ("Excelente a escogido Facial")
elif pedido == "Manicure":
    print ("Excelente a escogido Manicure")
else:
    print ("Servicio no disponible")