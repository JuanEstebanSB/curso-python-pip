import csv
import matplotlib.pyplot as plt

# Inicializar listas para los datos
fechas = []
valores = []

# Leer el archivo CSV y filtrar los datos
with open('App/datos.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
      # Leer el encabezado

    for row in reader:
        fecha = row[0]
        valor = float(row[1])

        # Filtrar datos: por ejemplo, solo valores mayores a 120
        if valor > 120:
            fechas.append(fecha)
            valores.append(valor)

# Graficar los datos filtrados
plt.figure(figsize=(10, 6))
plt.plot(fechas, valores, marker='o')  # Cambia a plt.scatter() o plt.bar() si lo prefieres

# Configurar la gráfica
plt.title('Valores Filtrados')
plt.xlabel('Fecha')
plt.ylabel('Valor')
plt.xticks(rotation=45)  # Rotar las fechas para mejor visualización
plt.grid()
plt.legend(['Valores > 120'])

# Mostrar la gráfica
plt.tight_layout()  # Ajustar el layout
plt.show()
