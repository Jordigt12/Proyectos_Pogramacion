import os #caja de herramientas para interactuar con el sistema operativo
#le pregunta al usuario que datos del cuadrate quiere buscar 
eje_x=int(input("Hola profavor ingresa el valor de X que deseas consultar\n"))
eje_y=int(input("Hola profavor ingresa el valor de Y que deseas consultar\n")) 
# Determina en qué parte del plano cartesiano se encuentran las coordenadas
if 0==eje_x==eje_y:  # Ambos valores son cero, por lo tanto están en el origen
    print("Origen")
elif 0<eje_x and 0>eje_y: # X positivo, Y negativo
    print("Cuadrante IV")
elif 0>eje_x and 0>eje_y:# X negativo, Y negativo
    print("Cuadrante III") 
elif 0>eje_x and 0<eje_y: # X negativo, Y positivo
    print("Cuadrante II")
else:                      # Cualquier otro caso: X positivo, Y positivo
    print("Cuadrante I")
os.system('pause') #pausa la ejecucion del codigo hasta que el usuario pulse una tecla para que pueda ver el resultado