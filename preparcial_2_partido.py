import random
random.seed(1234)

# Lista de equipos
equipos = ["Millonarios", "Nacional", "America", "Junior", "Santa fe", "Tolima", "Bucaramanga", "Pasto", "Huila", "Alianza"]
num_equipos = len(equipos)  # Número de equipos
num_partidos = (num_equipos * (num_equipos - 1)) // 2  # Número de partidos
equipo_local = [0] * num_partidos
equipo_visita = [0] * num_partidos
goles_local = [0] * num_partidos
goles_visita = [0] * num_partidos
total_puntos = [0] * num_equipos  # Total de puntos por equipo

# Generar partidos
def generar_partidos(equipo_local, equipo_visita, goles_local, goles_visita, num_equipos):
    partido = 0
    for i in range(num_equipos):
        for j in range(i + 1, num_equipos):
            equipo_local[partido] = i
            equipo_visita[partido] = j
            goles_local[partido] = random.randint(0, 5)
            goles_visita[partido] = random.randint(0, 5)
            partido += 1

# Calcular puntos por cada partido
def calcular_puntos(equipo_local, equipo_visita, goles_local, goles_visita, total_puntos, num_partidos):
    for i in range(num_partidos):
        if goles_local[i] > goles_visita[i]:  # Gana el equipo local
            total_puntos[equipo_local[i]] += 3
        elif goles_local[i] < goles_visita[i]:  # Gana el equipo visitante
            total_puntos[equipo_visita[i]] += 3
        else:  # Empate
            total_puntos[equipo_local[i]] += 1
            total_puntos[equipo_visita[i]] += 1

# Calcular el equipo campeón
def calcular_campeon(total_puntos, num_equipos):
    max_puntos = max(total_puntos) # Esta línea encuentra el valor máximo en la lista total_puntos.
    for i in range(num_equipos):  # Este es un bucle que recorre todos los equipos (los índices de la lista total_puntos).
        if total_puntos[i] == max_puntos: # Dentro del bucle, se verifica si los puntos del equipo en la posición i son iguales a max_puntos. 
                                          # Es decir, si el puntaje del equipo en la posición i es el puntaje más alto del torneo.
            return i # Si el puntaje del equipo en la posición i es igual a max_puntos,
                     # la función retorna el índice i del equipo que tiene más puntos, lo que significa que ese equipo es el campeón.

# Mostrar puntos de cada equipo
def print_puntos_totales(equipos, total_puntos, num_equipos):
    print("Puntos totales por equipo:")
    for i in range(num_equipos):
        print(f"{equipos[i]}: {total_puntos[i]} puntos")

# Llamada a las funciones
generar_partidos(equipo_local, equipo_visita, goles_local, goles_visita, num_equipos)
calcular_puntos(equipo_local, equipo_visita, goles_local, goles_visita, total_puntos, num_partidos)
campeon = calcular_campeon(total_puntos, num_equipos)

# Imprimir resultados
print_puntos_totales(equipos, total_puntos, num_equipos)
print(f"El ganador del Campeonato es {equipos[campeon]} con {total_puntos[campeon]} puntos.")

