import matplotlib.pyplot as plt # Importa la librería matplotlib para graficar
import random # Importa la librería random para generar números aleatorios

m=list(range(1, 13)) # Crea una lista con los números del 1 al 12 (representa los "cubículos")
n=[random.randint(1,3000) for _ in range(12)]# Genera una lista de 12 números aleatorios entre 1 y 3000 (representa la cantidad de canicas en cada cubículo)
plt.bar(m, n) # Dibuja un gráfico de barras con los cubículos en el eje X y las canicas en el eje Y
plt.title("Maquina de Galton ") # Coloca el título del gráfico
plt.xlabel("cubiculos")  # Coloca el título del gráfico
plt.ylabel("canicas")# Etiqueta el eje Y como "canicas"
plt.show() # Muestra el gráfico en pantalla