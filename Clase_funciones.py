# variables globales
# variables locales
# Para guardar mas varibles podemos usar un astructura de datos conocida como arreglos que puede guardar muchas variables
# son como un vector con cordenadas y tiene  un indice 
# Convinaciones de vectores y funciones || tambien vimos la funcion void || invocar funciones 
# para la funciones de calcular el promedio -> la mandan el float, el tamaño y luego imprime el resultado

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

# ---------------------------------------------------------------------

def calcular_promedio():
    n = 7
    notas = [n] # n es el tamaño del vector 
    
    for i in range(7):
        nota = float(input(f"Ingresa la nota {i + 1}: "))
        notas.append(nota)
        
        # Calcular el promedio
        promedio = sum(notas) / len(notas)
    
    print(f"El promedio de las notas es: {promedio}")

calcular_promedio()
