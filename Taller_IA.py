import random  # Importamos el módulo random para generar números aleatorios

# Función para simular el lanzamiento de dados
def roll_dice(num_dice=2):
    return [random.randint(1, 6) for _ in range(num_dice)]

# Función para verificar si un número es primo
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Función para manejar el turno de un jugador
def play_turn():
    total = 0
    while True:
        dice = roll_dice()  # Lanzamos 2 dados
        roll_sum = sum(dice)
        total += roll_sum
        print(f"Lanzamiento: {dice}, Suma: {roll_sum}, Total: {total}")

        if total > 23:
            print("Te pasaste de 23. Tu turno termina.")
            return 0  # El jugador pierde si se pasa de 23

        if dice[0] == dice[1]:  # Si saca dobles
            choice = input("Sacaste dobles. ¿Quieres dividir? (s/n): ")
            if choice.lower() == 's':
                print("Dividiendo la mano...")
                hand1 = play_split_hand(dice[0])
                hand2 = play_split_hand(dice[0])
                return max(hand1, hand2)  # Devuelve la mejor puntuación de las dos manos

        if total == 12:
            choice = input("Tienes 12. ¿Quieres lanzar solo un dado? (s/n): ")
            if choice.lower() == 's':
                extra = roll_dice(1)[0]
                total += extra
                print(f"Lanzaste un {extra}. Nuevo total: {total}")
                return total  # Termina el turno después de lanzar un dado adicional

        choice = input("¿Quieres lanzar de nuevo? (s/n): ")
        if choice.lower() != 's':
            return total  # Termina el turno si el jugador no quiere lanzar de nuevo

# Función para manejar una mano dividida
def play_split_hand(initial_value):
    total = initial_value
    print(f"Nueva mano, comenzando con: {total}")
    while True:
        dice = roll_dice(3)  # Lanzamos 3 dados para la mano dividida
        roll_sum = sum(dice)
        total += roll_sum
        print(f"Lanzamiento: {dice}, Suma: {roll_sum}, Total: {total}")

        if total > 23:
            print("Te pasaste de 23 en esta mano dividida.")
            return 0

        choice = input("¿Quieres lanzar de nuevo en esta mano dividida? (s/n): ")
        if choice.lower() != 's':
            return total

# Función para comparar las puntuaciones y determinar el ganador
def compare_scores(scores):
    prime_scores = [score for score in scores if is_prime(score)]
    if prime_scores:
        return max(prime_scores)  # Si hay números primos, el mayor primo gana
    return max(scores)  # Si no hay primos, gana el mayor número

# Función para jugar una ronda completa con todos los jugadores
def play_game(num_players):
    scores = []
    for i in range(num_players):
        print(f"\nTurno del Jugador {i+1}")
        score = play_turn()
        scores.append(score)
        print(f"Puntuación final del Jugador {i+1}: {score}")

    winning_score = compare_scores(scores)
    winners = [i+1 for i, score in enumerate(scores) if score == winning_score]

    print("\nResultados finales:")
    for i, score in enumerate(scores):
        print(f"Jugador {i+1}: {score}")

    if len(winners) == 1:
        print(f"\n¡El Jugador {winners[0]} gana con una puntuación de {winning_score}!")
    else:
        print(f"\n¡Empate entre los Jugadores {', '.join(map(str, winners))} con una puntuación de {winning_score}!")

# Función principal que inicia el juego
def main():
    num_players = int(input("Ingrese el número de jugadores: "))
    while True:
        play_game(num_players)
        play_again = input("¿Quieren jugar otra ronda? (s/n): ")
        if play_again.lower() != 's':
            break

# Aseguramos que el juego solo se inicie si este script es el programa principal
if __name__ == "__main__":
    main()
