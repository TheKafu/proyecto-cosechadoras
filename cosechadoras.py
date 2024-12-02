# Mira mama, estoy en una tesis
import random

# Definir parámetros y variables
total_hectareas = 220
capacidad_tanque = 2000  # litros
rendimiento_diario = 6   # hectáreas por día
jornada_laboral = 7.5    # horas por día
dias_laborales_semana = 5
probabilidad_falla = 0.05
tiempo_reparacion = 1    # días

class Tractor:
    def _init_(self, id, capacidad_tanque, rendimiento_diario, probabilidad_falla):
        self.id = id
        self.capacidad_tanque = capacidad_tanque
        self.rendimiento_diario = rendimiento_diario
        self.probabilidad_falla = probabilidad_falla
        self.en_reparacion = False
        self.dias_reparacion_restantes = 0
    
    def trabajar(self):
        if self.en_reparacion:
            self.dias_reparacion_restantes -= 1
            if self.dias_reparacion_restantes == 0:
                self.en_reparacion = False
            return 0
        
        if random.random() < self.probabilidad_falla:
            self.en_reparacion = True
            self.dias_reparacion_restantes = tiempo_reparacion
            return 0
        
        return self.rendimiento_diario

# Inicializar tractores
tractores = [Tractor(id=i, capacidad_tanque=capacidad_tanque, rendimiento_diario=rendimiento_diario, probabilidad_falla=probabilidad_falla) for i in range(3)]

# Simulación
hectareas_tratadas = 0
dias_trabajados = 0
while hectareas_tratadas < total_hectareas:
    for dia in range(dias_laborales_semana):
        if hectareas_tratadas >= total_hectareas:
            break
        for tractor in tractores:
            hectareas_tratadas += tractor.trabajar()
            if hectareas_tratadas >= total_hectareas:
                break
        dias_trabajados += 1
    dias_trabajados += 2  # Añadir fin de semana

# Resultados
print(f"Total de días trabajados: {dias_trabajados}")