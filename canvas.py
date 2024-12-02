
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from Trabajo import probabilidades, aplicacion, tractores

"""
x = [300, 400, 500]
y = [12.222, 14.667, 16.267]
plt.plot(x, y)  # Crea el gráfico
plt.title('Dias por litros utilizados')
plt.xlabel('Litros utilizados')
plt.ylabel('Dias')
plt.show()
"""


##Calculadora de rango y alcance de hectareas trabajadas por un tren antes de fallar

#mojado de 300, cubre 6 hectareas diarias
"""
variable = np.random.uniform(0,6,1000)

promedio = variable.mean()
desviacion = variable.std()
rango = (promedio-desviacion,promedio+desviacion)
print(rango) 
rango = random.uniform(rango[0], rango[1])
rango_trabajado = round (rango,3)
print(rango_trabajado) 
"""


#Total de dias de trabajo
"""
trenes = 3
fallo = 0
hectareas_totales = 0
dias_totales = 0

dia_trabajado = 6*trenes + fallo
#print(dia_trabajado)

for i in range(50):
    if hectareas_totales>=220:
        round(dias_totales, 3)
        print(f"Se han trabajado {dias_totales}dias")
        break
    else:
        hectareas_totales = hectareas_totales + dia_trabajado
        dias_totales = dias_totales+1
        pass
"""


#parte-> nuevo dia -> falla? -> ejecutar rango trabajado -> final del dia -> alcance 220 h? - repetir

"""
#El fallo de 1 2 o 3 tractores

pf = 0.05 #probabilidad de fallo
npf = 0.95 #probabilidad de ningun fallo

#aplicamos triangulo de pascal
p_0 =1*      npf**3 
p_1 =3*pf*   npf**2 
p_2 =3*pf**2*npf
p_3 =1*pf**3
#redondeo a milesimas
p_0 = round(p_0, 3) 
p_1 = round(p_1, 3)
p_2 = round(p_2, 3)
p_3 = round(p_3, 3)

#esto crea un dado cargado de 4 caras con las probabilidades de que fallen de 0 a 3 tractores
probabilidades = [p_0, p_1, p_2, p_3]
resultado = random.choices([0, 1, 2, 3], weights=probabilidades, k=1)
print(resultado[0])
"""

"""
Simulacion
#Variables

hectareas = 220
n_tractor = 3
fallo = 0
hectareas_totales = 0
dias_totales = 0
dia_trabajado = 6*n_tractor + fallo #fijo aun

def conteo_dias(nombre=None):
    if hectareas_totales>=hectareas:
        print(hectareas_totales)
        round(dias_totales, 3)
        print(f"Se han trabajado {dias_totales}dias")
    else:
        print(f"llevan {hectareas_totales} hectareas")
        hectareas_totales = hectareas_totales + dia_trabajado
        dias_totales = dias_totales+1

for i in range(1):
    
    #esto crea un dado cargado de 4 caras con las probabilidades de que fallen de 0 a 3 tractores
    resultado = random.choices([0, 1, 2, 3], weights=probabilidades, k=1)
    print(resultado)

    if resultado[0] == 0:
        conteo_dias()
        pass
    elif resultado[0] == 1:
        pass
   """

#x = random.choices([0, 1, 2, 3], weights=probabilidades, k=1)
#print(x[0])
"""
variable = np.random.uniform(0,aplicacion.rendimiento,1000)
promedio = variable.mean()
desviacion = variable.std()
rango = (promedio-desviacion,promedio+desviacion)
rango = random.uniform(rango[0], rango[1])
rango_trabajado = round (rango,3)

rango_trabajado = 0        
dia_trabajado = aplicacion.rendimiento*(tractores-x[0]) + rango_trabajado
print(dia_trabajado)
"""
"""
escenario = 3
        # se selecciona un número aleatorio entre 0 y el rendimiento de hectareas de un tractor
rango_trabajado = 0 
for i in range(escenario):
    rango_trabajado = rango_trabajado + random.uniform(0,aplicacion.rendimiento)

print(rango_trabajado)   
"""

x = 16375 * 30
print(x)