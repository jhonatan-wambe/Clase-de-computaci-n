
import random
random.seed(1234)

#lista de equipos
equipos = ["Millonarios", "Nacional", "America", "Junior", "Santa fe", "Tolima", "Bucaramanga", "Pasto", "Huila", "Alianza"]
num_equipos = len(equipos) # toma el numeor de equipos
num_partidos = (num_equipos * (num_equipos - 1)) // 2 

equipo_local = [0] * num_partidos
equipo_visita = [0] * num_partidos
goles_local = [0] * num_partidos
goles_visita = [0] * num_partidos
total_puntos = [0] * num_partidos

def generar_partidos(equipo_local, equipo_visita, goles_local, goles_visita, num_equipos):
    partido = 0
    for i in range(num_equipos):
        for j in range(i + 1, num_equipos):
            equipo_local[partido] = i
            equipo_visita[partido] = j
            goles_local[partido] = random.randint(0,5)
            goles_visita[partido] = random.randint(0,5)
            partido +=1
            
def calcular_puntos(equipo_local, equipo_visita, goles_local, goles_visita, num_equipos):
    for i in range(num_partidos):
        if goles_local[i] > goles_visita[i]:
            total_puntos[equipo_local[i]] += 3
        elif goles_local[i] < goles_visita[i]:
            total_puntos[equipo_local[i]] += 3
        else:
            total_puntos[equipo_local[i]] += 1
            total_puntos[equipo_visita[i]] += 1
            
def calcular_campeon(total_puntos, num_equipos):
    max_puntos = max(total_puntos)
    for i in range(num_equipos):
        if total_puntos[i] == max_puntos:
            return i
        
generar_partidos(equipo_local, equipo_visita, goles_local, goles_visita, num_equipos)
calcular_puntos(equipo_local, equipo_visita, goles_local, goles_visita, num_equipos, total_puntos)
campeon = calcular_campeon(total_puntos, num_equipos)

print_puntos_totales(equipos, total_puntos, num_equipos)
print(f"El ganador del Campeonato es {equipos[campeon]} con {total_puntos[campeon]} puntos. ")

