# El jugador A ingresa el número secreto
numero_secreto = int(input("Jugador A, ingresa el numero secreto de dos digitos: "))

# Extraer los dígitos del número secreto
digito1_secreto = numero_secreto // 10
digito2_secreto = numero_secreto % 10

# Jugador B tiene 5 intentos
intentos = 5

while intentos > 0:
    # El jugador B ingresa su intento
    intento = int(input("Jugador B, ingresa tu intento de dos digitos: "))

    # Extraer los dígitos del intento
    digito1_intento = intento // 10
    digito2_intento = intento % 10

    # Contadores para fama y punto
    fama = 0
    punto = 0

    # Verificar fama
    if digito1_intento == digito1_secreto:
        fama += 1
    if digito2_intento == digito2_secreto:
        fama += 1

    # Verificar punto
    if digito1_intento == digito2_secreto and digito1_intento != digito1_secreto:
        punto += 1
    if digito2_intento == digito1_secreto and digito2_intento != digito2_secreto:
        punto += 1

    # Mostrar resultados
    print(f"Tienes {fama} fama(s) y {punto} punto(s).")

    # Verificar si ganó
    if fama == 2:
        print("¡Felicidades! Has adivinado el numero secreto.")
        break

    # Decrementar intentos
    intentos -= 1

    # Verificar si quedan intentos
    if intentos == 0:
        print(f"Lo siento, te has quedado sin intentos. El numero secreto era: {numero_secreto}")
    else:
        print(f"Te quedan {intentos} intentos.")
