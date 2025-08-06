from decimal import Decimal, getcontext
getcontext().prec = 2
print("hola bienvenido a la calculadora de indice de masa corporal")
print ("""primero que nada queremos conocerte.
Asi que dinos ¿cual es tu nombre completo?""")
apellido  = input("""Apellido paterno
                  """)
apellidom= input("""Apellido materno" 
                  """)
nombre= input("""tu o tus nombres 
                 """)
print ("perfecto"+" "+nombre) 
print ("Ahora por favor contesta las siguiente preguntas para poder calcular tu IMC")
while True:
     try:
         estatura =Decimal(input("""cual es tu altura en metros.
        Ejemplo 1.56\n\t"""))
         break
     except:
         print("porfavor ingrese solo  la estatura en metros como el ejmplo")
print("Ok perfecto"+" "+nombre)
while True:
    try:
        peso=Decimal(input("""Y ahora dime ¿cual es tu peso?
        Ejemplo: 85.1\n\t """))
        break
    except:
        print("por favor ingrese solo la estatura como en el ejemplo")

IMC = peso/(estatura**2)
print(f"Bien {nombre} tu IMC es:\n\t", IMC )
if IMC < 18.5:
    print ("tienes un porcentaje de grasa bajo")

elif 18.5 <= IMC < 25:
    print("tienes un porcentaje de grasa normal")

elif 25<= IMC < 30:
    print("tienes un porcentaje de grasa alto")

else:
    print("tienes obesidad")
print("Datos de usuario")
print("nombre:",nombre +" "+ apellido +" "+ apellidom, """
estatura:""", estatura,"""
peso:""", peso,"""
IMC:""", IMC)



