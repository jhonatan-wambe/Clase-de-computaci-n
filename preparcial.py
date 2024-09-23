import random

# Lista de equipos
equipos = ["Nacional", "Millonarios", "América", "Junior", "Santa Fe"]

# Función para simular un partido
def simular_partido(equipo1, equipo2):
    goles1 = random.randint(0, 5)
    goles2 = random.randint(0, 5)
    print(f"{equipo1} {goles1} - {goles2} {equipo2}")

# Elegir dos equipos al azar
equipo_local = random.choice(equipos)
equipo_visita = random.choice([e for e in equipos if e != equipo_local])

# Simular el partido
simular_partido(equipo_local, equipo_visita)
