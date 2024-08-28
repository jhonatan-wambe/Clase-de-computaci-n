#include <iostream>
using namespace std;

int main() {
    int numeroSecreto, intento;
    int intentosRestantes = 5;

    cout << "Jugador A, ingresa el numero secreto de dos digitos: ";
    cin >> numeroSecreto;

    // Asegurarse de que el numero secreto sea de dos dígitos.
    if (numeroSecreto < 10 || numeroSecreto > 99) {
        cout << "El numero secreto debe ser un numero de dos digitos." << endl;
        return 1;
    }

    int digito1Secreto = numeroSecreto / 10;
    int digito2Secreto = numeroSecreto % 10;

    // Limpiar la pantalla para que el Jugador B no vea el numero secreto
    cout << "\033[2J\033[1;1H";

    while (intentosRestantes > 0) {
        cout << "Jugador B, ingresa tu intento: ";
        cin >> intento;

        // Asegurarse de que el intento sea de dos dígitos.
        if (intento < 10 || intento > 99) {
            cout << "El intento debe ser un numero de dos digitos." << endl;
            continue;
        }

        int digito1Intento = intento / 10;
        int digito2Intento = intento % 10;

        bool fama = false;
        bool punto = false;

        // Comprobar "fama"
        if (digito1Intento == digito1Secreto || digito2Intento == digito2Secreto) {
            fama = true;
        }

        // Comprobar "punto"
        if ((digito1Intento == digito2Secreto && digito1Intento != digito1Secreto) || 
            (digito2Intento == digito1Secreto && digito2Intento != digito2Secreto)) {
            punto = true;
        }

        if (fama && punto) {
            cout << "Tienes una fama y un punto!" << endl;
        } else if (fama) {
            cout << "Tienes una fama!" << endl;
        } else if (punto) {
            cout << "Tienes un punto!" << endl;
        } else {
            cout << "No tienes ni fama ni punto!" << endl;
        }

        if (intento == numeroSecreto) {
            cout << "Felicidades! Has adivinado el numero secreto!" << endl;
            break;
        }

        intentosRestantes--;
        cout << "Te quedan " << intentosRestantes << " intentos." << endl;

        if (intentosRestantes == 0) {
            cout << "Lo siento! Has agotado todos tus intentos. El numero secreto era " << numeroSecreto << "." << endl;
        }
    }

    return 0;
}
