import random 
#lista de equipos
equipos = ["Millonarios", "Nacional", "America", "Junior", "Santa fe", "Tolima", "Bucaramanga", "Pasto", "Huila", "Alianza"]

# Funcion para simular un partido

def simular_partido(equipo1, equipo2):
    goles1 = random.randint(0,5)
    goles2 = random.randint(0,5)
    print(f"{equipo1} {goles1} - {goles2} {equipo2}")
    
# Elegir dos equipos al azar
equipo_local = random.choice(equipos) # random.choice(equipos) escoge un elemento aleatoriamente de la lista equipos 
equipo_visita = random.choice([e for e in equipos if e != equipo_local])

# simular el partido
simular_partido(equipo_local, equipo_visita)
