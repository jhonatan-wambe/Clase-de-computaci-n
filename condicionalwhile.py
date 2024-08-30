# ¿como plantearia el algoritmo para calcular el factorial de un numero?
# n! = 1*2*3*4*5*6*.....*n-2*n-1*n
# long entero 
# flujo de energia en una planta nuclear
# como optimizar al motor de spacex
# realizar simulaciones de alto nivel
# EPICS - es una comunidad de desarrollo 
# resulven un problema de una comunidad 

n = int(input("Digite el n: "))
factorial = 1
i = 1

while(i<=n):
    # factorisar *= (n-i) 
    # i = i + 1
    # el resumen de las dos lineas de codigo de arriba es factorial*= (n-i++)
    factorial *=i
    i = i + 1
    print(f"EL factorial de {n} es = {factorial}")
