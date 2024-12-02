import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parámetros
hectareas_total = 220
riegos = [300, 400, 500]  # Litros por hectárea
avance_diario = [6, 5, 4.5]  # Hectáreas por día por tractor
prob_fallo = 0.05  # Probabilidad de fallo
simulaciones = 10000

# Función de simulación
def simular_riego():
    dias_totales = []
    
    for _ in range(simulaciones):
        dias_riego = []
        for riego, avance in zip(riegos, avance_diario):
            dias_por_riego = 0
            hectareas_restantes = hectareas_total
            
            while hectareas_restantes > 0:
                fallan = np.random.rand(3) < prob_fallo  # Fallos de los 3 tractores
                avance_real = [
                    np.random.uniform(avance - 1, avance + 1) if fallo else avance
                    for fallo in fallan
                ]
                
                avance_total = sum(avance_real)
                hectareas_restantes -= avance_total
                dias_por_riego += 1
            
            dias_riego.append(dias_por_riego)
        
        dias_totales.append(sum(dias_riego))
    
    return dias_totales

# Ejecutar simulación
dias_totales = simular_riego()

# Análisis de resultados
media_dias = np.mean(dias_totales)
desviacion_dias = np.std(dias_totales)

print(f"Promedio de días totales: {media_dias:.2f}")
print(f"Desviación estándar de días totales: {desviacion_dias:.2f}")

# Graficar resultados
plt.hist(dias_totales, bins=50, color='skyblue', edgecolor='black')
plt.title("Distribución de días totales para completar los riegos")
plt.xlabel("Días totales")
plt.ylabel("Frecuencia")
plt.axvline(media_dias, color='red', linestyle='dashed', linewidth=1, label=f"Promedio: {media_dias:.2f}")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()