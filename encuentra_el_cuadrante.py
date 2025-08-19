import os
eje_x=int(input("Hola profavor ingresa el valor de X que deseas consultar\n"))
eje_y=int(input("Hola profavor ingresa el valor de Y que deseas consultar\n"))
if 0==eje_x==eje_y:
    print("Origen")
elif 0<eje_x and 0>eje_y:
    print("Cuadrante IV")
elif 0>eje_x and 0>eje_y:
    print("Cuadrante III")
elif 0>eje_x and 0<eje_y:
    print("Cuadrante II")
else:
    print("Cuadrante I")
print()
os.system('pause')