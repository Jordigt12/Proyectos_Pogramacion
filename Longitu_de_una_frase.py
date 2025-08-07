import os
frase= input("hola ingresa una palabra\n") #aqui el usuario debe ingresar una palabra
if 4>len(frase): #si la x palabra es menor a 4 caracteres imprimira un mensaje
    print("faltan letras")
elif 8<len(frase): #si la x palabra es mayor a 8 caracteres imprimira un mensaje 
    print("sobran letras")
else: #si la x palabra se encuentra en el rango de 4 a 8 palabras aparecera un mensaje 
    print("palabra valida mi paps")
    print()
    os.system('pause')