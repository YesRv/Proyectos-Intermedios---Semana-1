##  Peluquería: turno del día
## Pide la hora de llegada de un cliente en formato entero de 0 a 23.
# 
# mañana si está entre 6 y 11 
# tarde si está entre 12 y 17 
# noche si está entre 18 y 22 
# fuera de horario en cualquier otro caso 
  

hora_entrada = int (input(" Ingresa la hora de entrada del cliente:  "))

if hora_entrada >=6 and hora_entrada <=11:
    print ("Hora de entrada: Mañana")
elif hora_entrada >= 12 and hora_entrada <=17:
    print ("Hora de entrada: Tarde")
elif hora_entrada >=18 and hora_entrada <=22:
    print ("Hora de entrada: Noche")
else:
    print ("Fuera de horario")
