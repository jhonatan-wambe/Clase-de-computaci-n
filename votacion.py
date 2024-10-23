'''
uno para hacer el conteo de votos y otro para votacion de candidatos

1000 filas 4 columnas
evaluacion de archivos y matrices

hacer dos subsistemas

leer todos los estudiantes
nombre del estudiante 
voto por un cadidato 

funciones
una genera de manera aleatoria
una con la que ingresa los datos

Que tiene que hacer el programa
candidato ganador
votos en blanco
votos por facultad
decano ganador por facultad

'''


import random

# Leer votos
Identificacion = []

#generando el Id 
def generar_Id_estudiante():
    return random.randint(1000000000,1000000000)

def Ingresar_id():
    id = generar_Id_estudiante()
    Identificacion.append(id)

    
def mostrar_estudiantes():
    print("\n Lista de estudiantes")
    for i in range(len(Identificacion)):
        print(f"{[i+1]}. {Identificacion[i]} ")

for _ in range(5):
    Ingresar_id()
    
mostrar_estudiantes()
