import random 
#lista de equipos
equipos = ["Millonarios", "Nacional", "America", "Junior", "Santa fe", "Tolima", "Bucaramanga", "Pasto", "Huila", "Alianza"]
num_equipos = len(equipos) # toma el numeor de equipos

# Funcion para simular un partido

def simular_partido(equipo1, equipo2):
    goles1 = random.randint(0,5) # genera un numero aleatorio de 0,5 
    goles2 = random.randint(0,5)
    print(f"{equipo1} {goles1} - {goles2} {equipo2}")
    
# Elegir dos equipos al azar
equipo_local = random.choice(equipos) # random.choice(equipos) escoge un elemento aleatoriamente de la lista equipos 
equipo_visita = random.choice([e for e in equipos if e != equipo_local]) # recorre cada elemento de la lista equipos y lo compara con el equipo local

# simular el partido
simular_partido(equipo_local, equipo_visita)
