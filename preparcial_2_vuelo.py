import random

def generar_vuelos(nv):
    # Verificar que el número de vuelos sea mayor que 0
    if nv <= 0:
        print("El número de vuelos debe ser mayor que 0.")
        return
    
    pasajeros = []  # Lista para almacenar los códigos de los pasajeros
    millas = []     # Lista para almacenar las millas acumuladas por cada pasajero
    
    for _ in range(nv):  # Generar el número de vuelos especificado
        # Generar un número aleatorio de pasajeros entre 50 y 100
        num_pasajeros = random.randint(50, 100)
        # Generar una distancia aleatoria entre 500 y 5000 kilómetros
        distancia = random.randint(500, 5000)
        
        for _ in range(num_pasajeros):  # Por cada pasajero en el vuelo
            codigo = generar_codigo_pasajero()  # Generar un código para el pasajero
            estatus = calcular_estatus(codigo)  # Calcular el estatus del pasajero
            millas_ganadas = calcular_millas(distancia, estatus)  # Calcular millas ganadas
            
            # Actualizar la lista de pasajeros y sus millas
            actualizar_millas(pasajeros, millas, codigo, millas_ganadas)
    
    return pasajeros, millas  # Retornar las listas de pasajeros y sus millas acumuladas

def generar_codigo_pasajero():
    # Generar un código de pasajero aleatorio entre 100 y 999
    return random.randint(100, 999)

def calcular_estatus(codigo):
    # Determinar el estatus del pasajero basado en su código
    if codigo % 12 == 0:  # Diamante
        return "Diamante"
    elif codigo % 7 == 0:  # VIP
        return "VIP"
    else:  # Sin estatus especial
        return "Regular"

def calcular_millas(distancia, estatus):
    # Calcular las millas ganadas dependiendo del estatus del pasajero
    if estatus == "Diamante":
        return distancia // 20  # 1 milla por cada 20 km
    elif estatus == "VIP":
        return distancia // 60  # 1 milla por cada 60 km
    else:
        return distancia // 100  # 1 milla por cada 100 km

def actualizar_millas(pasajeros, millas, codigo, millas_ganadas):
    # Actualizar la lista de millas por pasajero
    if codigo not in pasajeros:  # Si el pasajero no está en la lista
        pasajeros.append(codigo)  # Agregar el código del nuevo pasajero
        millas.append(millas_ganadas)  # Agregar millas ganadas
    else:  # Si el pasajero ya existe
        index = pasajeros.index(codigo)  # Encontrar el índice del pasajero
        millas[index] += millas_ganadas  # Actualizar las millas acumuladas

# Programa principal
def main():
    # Solicitar al usuario el número de vuelos
    nv = int(input("Ingrese el número de vuelos: "))
    # Generar vuelos y obtener los pasajeros y sus millas
    pasajeros, millas = generar_vuelos(nv)
    
    # Mostrar resultados de los códigos de pasajeros y sus millas acumuladas
    print("Códigos de pasajeros y millas acumuladas:")
    for codigo, milla in zip(pasajeros, millas):
        print(f"Pasajero: {codigo}, Millas: {milla}")

# Llamada a la función principal
main()
