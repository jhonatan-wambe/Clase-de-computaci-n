# Entrada de datos
edad = int(input("Ingrese su edad: "))
promedio = float(input("Ingrese su promedio (si está estudiando): "))
comida_preferida = input("Ingrese su comida preferida (hamburguesa, perro caliente, pizza, sushi): ").lower()
trabaja = input("¿Actualmente trabaja? (sí/no): ").lower()

# Calcular la tasa de interés base
if edad < 20:
    tasa_interes = 20
else:
    tasa_interes = 18

# Ajustar la tasa según el promedio
if promedio < 3.5:
    tasa_interes -= 0.5
elif promedio <= 4.2:
    tasa_interes -= 0.8
else:
    tasa_interes -= 1.5

# Ajustar la tasa según la comida preferida
if comida_preferida == "hamburguesa":
    tasa_interes -= 0.2
elif comida_preferida == "perro caliente":
    tasa_interes -= 0.5
elif comida_preferida == "pizza":
    tasa_interes += 0.1
elif comida_preferida == "sushi":
    tasa_interes += 0.3

# Beneficio extra si la tasa es menor a 17% y la persona trabaja
if tasa_interes < 17 and trabaja == "sí":
    tasa_interes -= 1

# Salida de la tasa final
print(f"La tasa de interés final es: {tasa_interes}%")
