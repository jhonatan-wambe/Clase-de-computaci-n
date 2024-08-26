import math

print("\n hallar Z")
x = int(input("Ingrese el valor de X: "))
y = int(input("Ingrese el valor de Y: "))

ecuacion1 = x + ((y**2 / 3 + x)) # Y esta elevada al cuadrado
# n = 5 Por ejemplo, para la raíz quinta
# raiz_enesima = ecuacion1 ** (1/n)
raiz_ecuacion1 = math.sqrt(ecuacion1)
ecuacion2 = (x**2 / (y**3 + x)) - 5 * (math.sqrt(3 * x))
z = raiz_ecuacion1 - ecuacion2
print(f"Resultado ecuacuacion1 {z}")
