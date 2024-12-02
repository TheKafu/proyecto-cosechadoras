import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



# Hago la clase tractor para diferenciar los distintos mojamientos con su rendimiento diario
class Tractor:
    def __init__(self, lph, rendimiento, activo):
        self.lph = lph
        self.rendimiento = rendimiento
        self.activo = activo

#cambiar lph por cosechadora
#lph = litros por hectárea, mojamiento       

aplicacion1 = Tractor(300, 6, True)
aplicacion2 = Tractor(400, 5, True)
aplicacion3 = Tractor(500, 4.5, True)

# Aca otorgo los datos variables para realizar la simulacion
tractores = 3 

###Calculo la probabilidad de que fallen 0, 1, 2 o 3 tractores

pf = 0.05 #probabilidad de que falle
npf = 0.95 #probabilidad de no falle


#Por triangulo de pascal, existen 4 escenarios:

p_0 =1*      npf**3 #ninguno falla
p_1 =3*pf*   npf**2 #1 falla
p_2 =3*pf**2*npf #2 fallan
p_3 =1*pf**3 #3 fallan

# redondeo a milesimas las probabilidades resultantes
p_0 = round(p_0, 3) 
p_1 = round(p_1, 3)
p_2 = round(p_2, 3)
p_3 = round(p_3, 3)
# y cargo a un array de 4 opciones las 4 probabilidades de que ocurra tal escenario
probabilidades = [p_0, p_1, p_2, p_3]
print("Dado de probabilidades:")
print(f"{p_0} ; {p_1} ; {p_2} ; {p_3}")

# creamos el espacio a simular, la variable a cargar es el tipo de aplicacion. P.E: simulacion(aplicacion1)
def simulacion(app):
    # definimos la variable de dias totales que tomo el proceso y hectareas acumuladas por dia
    aplicacion = app
    dias_totales = 0
    hectareas_totales = 0
    print("Inicio del loop")
    # se crea un loop lo suficientemente grande para calcular los dias a trabajar
    for i in range(100):
        
        # si el total acumulativo de hectareas es menor a las hectareas totales 
        if hectareas_totales<220:
            
            print(f"Iteracion {i + 1}")
            print("--------------")
            ## Inicio un dia

            # se selecciona uno de los 4 escenarios de manera aleatoria y lo restamos de los tractores utilizados
            # esto para calcular los tractores operativos durante el dia
            escenario = random.choices([0, 1, 2, 3], weights=probabilidades, k=1) 
            tractores_totales = tractores - escenario[0]
            print(f"+Escenario: {escenario[0]} falla/s ; Tractores: {tractores} ; Tractores operando: {tractores_totales}")
            # separamos los sucesos entre 2 opciones, que no falle ninguno o que por lo menos uno falle

            # si por lo menos uno falla:
            if escenario[0] > 0:      
                print("!!Alerta: han fallado tractores!!")
                # iteramos este proceso por la cantidad de tractores con falla 
                rango_trabajado = 0 
                for i in range(escenario[0]):
                    # cargamos una sumatoria de un numero aleatorio entre 0 y el rendimiento en hectareas
                    # esto sera lo trabajado por los tractores antes de fallar
                    rango_trabajado = rango_trabajado + random.uniform(0,aplicacion.rendimiento)

                # finalmente calculamos el trabajo diario por los tractores con la siguiente formula:
                # rendimiento diario (en hectareas) * tractores operativos + rango trabajado por los tractores con falla
                dia_trabajado = aplicacion.rendimiento*(tractores_totales) + rango_trabajado
                print(f"Trabajo diario logrado: {round(dia_trabajado,1)}")
            
            # si ningun tractor falla:
            else:
                print("!!Alerta: no han fallado tractores!!")
                # calculamos el trabajo diario multiplicando el rendimiento diario por la cantidad de tractores
                dia_trabajado = aplicacion.rendimiento*(tractores)
                print(f"Trabajo diario logrado: {dia_trabajado}")       

            # sumamos las hectareas trabajadas del dia al total de hectareas y sumamos un dia al total de dias
            print(f"Hectareas previas: {hectareas_totales}")
            hectareas_totales = hectareas_totales + round(dia_trabajado,1)
            dias_totales = dias_totales+1
            print(f"Hectareas acumuladas: {hectareas_totales}")
            print(f"Dias acumulados: {dias_totales}")
            print("Fin de iteracion")
            print("--------------")

            # Fin del dia

        # si el total acumulativo de hectareas es mayor o igual a las hectareas totales
        else:
            print("Alerta: Fin de la jornada")
            round(dias_totales, 3)
            print(f"Se han trabajado {dias_totales}dias")
            break

    return dias_totales

simulacion(aplicacion3)
"""
resultados = []
for i in range(1000):
    resultados.append(simulacion(aplicacion1))
resultados_np = np.array(resultados)
print(resultados_np[:10])
"""


#### cambiar lph por cosechadora