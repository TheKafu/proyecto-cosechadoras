import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Hago la clase tractor para diferenciar los distintos mojamientos con su rendimiento diario
class Tractor:
    def __init__(self, rendimiento_c, rendimiento, tractor_activo, tractor_activo2, cosechadora_activa):

        self.rendimiento_c = rendimiento_c              # rendimiento de cosechadra
        self.rendimiento = rendimiento                  # rendimiento de tractor
        self.tractor_activo = tractor_activo            # arriendo de 1 tractor
        self.tractor_activo2 = tractor_activo2          # arriendo de 2 tractores
        self.cosechadora_activa = cosechadora_activa    # uso de cosechadora

aplicacion1 = Tractor(13, 6, False, False, True)       # aplicacion de 300 L/ht
aplicacion2 = Tractor(12, 5, False, False, False)       # aplicacion de 400 L/ht
aplicacion3 = Tractor(11, 4.5, False, False, False)     # aplicacion de 500 L/ht

# asigno en valores fijos la cantidad de tractores y cosechadoras para uso dentro de la simulacion
tractores = 3 
cosechadora = 1

# calculo la probabilidad de que fallen 0, 1, 2 o 3 tractores

pf = 0.05       # probabilidad de que falle
npf = 0.95      # probabilidad de no falle

# Por triangulo de pascal, existen 4 escenarios:

p_0 =1*      npf**3     # ninguno falla
p_1 =3*pf*   npf**2     # 1 falla
p_2 =3*pf**2*npf        # 2 fallan
p_3 =1*pf**3            # 3 fallan

# redondeo a milesimas las probabilidades resultantes
p_0 = round(p_0, 3) 
p_1 = round(p_1, 3)
p_2 = round(p_2, 3)
p_3 = round(p_3, 3)

# y cargo a un array de 4 opciones las 4 probabilidades de que ocurra tal escenario (como un dado cargado)
probabilidades = [p_0, p_1, p_2, p_3]   # el dado trabaja con una precicion de 0.999 debido a la perdida decimales

# realizo el mismo proceso para la cosechadora

npc = 0.9       #probabilidad de no fallo de la cosechadora
pc = 0.1        #probabilidad de fallo de la cosechadora

# en este caso el array tiene solo 2 datos (como una moneda cargada)
probabilidades_c = [npc, pc]
#print(f"Probabilidades de falla de tractores: {p_0} ; {p_1} ; {p_2} ; {p_3} \nProbabilidades de falla de cosechadora: {npc} ; {pc}")


# creamos el espacio a simular
def simulacion(app):
    # definimos la variable de dias totales que tomo el proceso y hectareas acumuladas por dia

    aplicacion = app                    # carga de aplicacion a la funcion simulacion()
    dias_totales = 0                    # contador de dias 
    hectareas_totales = 0
    hectareas = 220
    if app.tractor_activo == True:
        hectareas = 190
    elif app.tractor_activo2 == True:
        hectareas = 160
    cosechadora_count = 0

    # se crea un loop lo suficientemente grande para calcular los dias a trabajar
    print("Inicio del loop")
    for i in range(100):

### si el total acumulativo de hectareas es menor a las hectareas totales 
        if hectareas_totales<hectareas:
            
            ## Inicio un dia
            print(f"Iteracion {i + 1} \n--------------")

            # se selecciona uno de los 4 escenarios de manera aleatoria y lo restamos de los tractores utilizados
            # esto para calcular los tractores operativos durante el dia
            escenario = random.choices([0, 1, 2, 3], weights=probabilidades, k=1) 
            tractores_totales = tractores - escenario[0]
            # para la cosechadora solo es necesario saber si falló o no
            escenario_c = random.choices([0, 1], weights=probabilidades_c, k=1) 
            print(f"+Escenario: {escenario[0]} falla/s ; Tractores: {tractores} ; Tractores operando: {tractores_totales}")
            print(f"+Escenario_C: {escenario_c[0]} falla/s ")
            print(f"Hectareas previas: {hectareas_totales}")

    ### Para trabajar los tractores:

            # si por lo menos uno falla
            if escenario[0] > 0:
                print("¡¡Alerta: han fallado tractores!!")
                # iteramos este proceso por la cantidad de tractores con falla 
                rango_trabajado = 0 
                for i in range(escenario[0]):
                    # cargamos una sumatoria de un numero aleatorio entre 0 y el rendimiento en hectareas
                    # esto sera lo trabajado por los tractores antes de fallar
                    rango_trabajado = rango_trabajado + random.uniform(0,aplicacion.rendimiento)

                # finalmente calculamos el trabajo diario por los tractores con la siguiente formula:
                # rendimiento diario (en hectareas) * tractores operativos + rango trabajado por los tractores con falla
                dia_trabajado = aplicacion.rendimiento*(tractores_totales) + rango_trabajado
                print(f"Trabajo diario T logrado: {round(dia_trabajado,1)}")
            # si ningun tractor falla
            else:
                # calculamos el trabajo diario multiplicando el rendimiento diario por la cantidad de tractores
                dia_trabajado = aplicacion.rendimiento*(tractores)
                print(f"Trabajo diario T logrado: {dia_trabajado}") 

            # sumamos las hectareas trabajadas del dia al total de hectareas y sumamos un dia al total de dias
            hectareas_totales = hectareas_totales + dia_trabajado

    ### Para trabajar con la cosechadora:

            # si tenemos la cosechadora activa realizamos el mismo proceso que realizamos con los tractores
            if app.cosechadora_activa == True:

                # verificamos que la cosechadora no se encuentre en un dia de penalización
                # son 2 dias de reparación a la cosechadora luego de fallar
                if cosechadora_count == 0:
                    print("Cosechadora activa")

                    # si falla la cosechadora 
                    if escenario_c[0] == 1:      
                        print("¡¡Alerta: ha fallado la cosechadora!!")
                        # cargamos el dia trabajado con un numero entre 0 y el rendimiento en hectareas
                        # esto será lo trabajado por la cosechadora antes de fallar
                        dia_trabajado = random.uniform(0,aplicacion.rendimiento_c)

                        # como falló la cosechadora le damos 2 dias de penalización por falla
                        cosechadora_count = cosechadora_count + 2
                        print(f"Trabajo diario C logrado: {dia_trabajado}") 
                        
                    # si no falla la cosechadora
                    else:
                        # se carga el dia trabajado con el rendimiento total de la cosechadora
                        dia_trabajado = aplicacion.rendimiento_c 
                        print(f"Trabajo diario C logrado: {dia_trabajado}")   
                # si se encuentra en un dia de penalización, solo se descuenta uno de estos dias
                else:
                    print(f"Cosechadora en reparacion \n Dias restantes: {cosechadora_count}")
                    cosechadora_count = cosechadora_count - 1
                    pass

                # sumamos las hectareas trabajadas del dia al total de hectareas y sumamos un dia al total de dias
                hectareas_totales = hectareas_totales + dia_trabajado

            dias_totales = dias_totales+1
            print(f"Hectareas acumuladas: {hectareas_totales}")
            print(f"Dias acumulados: {dias_totales}")
            print("Fin de iteracion")
            print("--------------")

            # Fin del dia

### si el total acumulativo de hectareas es mayor o igual a las hectareas totales
        else:
            round(dias_totales, 3)
            print("Alerta: Fin de la jornada\n")
            print(f"Se han trabajado {dias_totales}dias")
            break

    return dias_totales

simulacion (aplicacion1)
