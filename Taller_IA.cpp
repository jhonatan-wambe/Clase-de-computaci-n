#include <iostream>    // Para entrada/salida estándar (cin, cout)
#include <vector>      // Para usar vectores, que son arrays dinámicos
#include <cstdlib>     // Para la función rand() (generación de números aleatorios)
#include <ctime>       // Para la función time() (usada para sembrar el generador de números aleatorios)
#include <algorithm>   // Para funciones como max_element (encontrar el máximo en un vector)

using namespace std;   // Para evitar escribir std:: antes de cin, cout, vector, etc.

// Función para simular el lanzamiento de dados
vector<int> rollDice(int numDice = 2) {
    vector<int> result;
    for (int i = 0; i < numDice; i++) {
        result.push_back(rand() % 6 + 1);
    }
    return result;
}

// Función para verificar si un número es primo
bool isPrime(int n) {
    if (n < 2) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

// Función para jugar una mano dividida
int playSplitHand(int initialValue) {
    int total = initialValue;
    cout << "Nueva mano, comenzando con: " << total << endl;
    
    while (true) {
        vector<int> dice = rollDice(3);  // Lanzamos 3 dados para la mano dividida
        int rollSum = 0;
        for (int die : dice) rollSum += die;
        
        total += rollSum;
        cout << "Lanzamiento: ";
        for (int die : dice) cout << die << " ";
        cout << ", Suma: " << rollSum << ", Total: " << total << endl;

        if (total > 23) {
            cout << "Te pasaste de 23 en esta mano dividida." << endl;
            return 0;
        }

        char choice;
        cout << "¿Quieres lanzar de nuevo en esta mano dividida? (s/n): ";
        cin >> choice;
        if (choice != 's' && choice != 'S') return total;
    }
}

// Función para manejar el turno de un jugador
int playTurn() {
    int total = 0;
    while (true) {
        vector<int> dice = rollDice();
        int rollSum = dice[0] + dice[1];
        total += rollSum;
        cout << "Lanzamiento: " << dice[0] << " " << dice[1] << ", Suma: " << rollSum << ", Total: " << total << endl;

        if (total > 23) {
            cout << "Te pasaste de 23. Tu turno termina." << endl;
            return 0;
        }

        if (dice[0] == dice[1]) {  // Si saca dobles
            char choice;
            cout << "Sacaste dobles. ¿Quieres dividir? (s/n): ";
            cin >> choice;
            if (choice == 's' || choice == 'S') {
                cout << "Dividiendo la mano..." << endl;
                int hand1 = playSplitHand(dice[0]);
                int hand2 = playSplitHand(dice[0]);
                return max(hand1, hand2);
            }
        }

        if (total == 12) {
            char choice;
            cout << "Tienes 12. ¿Quieres lanzar solo un dado? (s/n): ";
            cin >> choice;
            if (choice == 's' || choice == 'S') {
                int extra = rollDice(1)[0];
                total += extra;
                cout << "Lanzaste un " << extra << ". Nuevo total: " << total << endl;
                return total;
            }
        }

        char choice;
        cout << "¿Quieres lanzar de nuevo? (s/n): ";
        cin >> choice;
        if (choice != 's' && choice != 'S') return total;
    }
}

// Función para comparar las puntuaciones y determinar el ganador
int compareScores(const vector<int>& scores) {
    vector<int> primeScores;
    for (int score : scores) {
        if (isPrime(score)) primeScores.push_back(score);
    }
    
    if (!primeScores.empty()) {
        return *max_element(primeScores.begin(), primeScores.end());
    }
    return *max_element(scores.begin(), scores.end());
}

// Función para jugar una ronda completa con todos los jugadores
void playGame(int numPlayers) {
    vector<int> scores(numPlayers);
    for (int i = 0; i < numPlayers; i++) {
        cout << "\nTurno del Jugador " << i+1 << endl;
        scores[i] = playTurn();
        cout << "Puntuación final del Jugador " << i+1 << ": " << scores[i] << endl;
    }

    int winningScore = compareScores(scores);
    vector<int> winners;
    for (int i = 0; i < numPlayers; i++) {
        if (scores[i] == winningScore) winners.push_back(i+1);
    }

    cout << "\nResultados finales:" << endl;
    for (int i = 0; i < numPlayers; i++) {
        cout << "Jugador " << i+1 << ": " << scores[i] << endl;
    }

    if (winners.size() == 1) {
        cout << "\n¡El Jugador " << winners[0] << " gana con una puntuación de " << winningScore << "!" << endl;
    } else {
        cout << "\n¡Empate entre los Jugadores ";
        for (size_t i = 0; i < winners.size(); i++) {
            cout << winners[i];
            if (i < winners.size() - 1) cout << ", ";
        }
        cout << " con una puntuación de " << winningScore << "!" << endl;
    }
}

int main() {
    srand(time(0));  // Inicializamos la semilla para números aleatorios
    
    int numPlayers;
    cout << "Ingrese el número de jugadores: ";
    cin >> numPlayers;

    char playAgain;
    do {
        playGame(numPlayers);
        cout << "¿Quieren jugar otra ronda? (s/n): ";
        cin >> playAgain;
    } while (playAgain == 's' || playAgain == 'S');

    return 0;
}
