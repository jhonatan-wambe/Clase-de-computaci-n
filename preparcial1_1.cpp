// punto 1 preparcial1
#include <iostream>
using namespace std;

int main()
{
    int semilla=0, val=0, val2=0, val3=0, val4=0;
    cout<<("Ingrese el valor de la semilla: "); cin>>semilla;
    srand(semilla); // numero de la semilla
    val = rand() % 12 + 1;
    cout<<"\nTiro inicial...";
    cout<<"\nLanzando dados ... ";
    cout<<"\nNumero de dados: "<<val;

    if(val == 2 || val == 3 || val == 12) // este || significa OR
    {
        cout<<"\nPerdedor en el tiro incial";
    }else if (val == 7 || val == 11){
        cout<<"\nGanador en el tiro incial";
    }else{
        cout<<"\nTiro secundario..";
        cout<<"\nLanzando dados ";
        val2 = rand() % 12 + 1;
        cout<<"\nNumero de dados: "<<val2;
        if(val2 == 7 ){
            cout<<"\nEl jugador Perdio";
        }else if (val2 == val){
            cout<<"\nEl jugador Gano";
        }else{
            cout<<"\nSigue jugando..";
            cout<<"\nLanzando dados ";
            val3 = rand() % 12 + 1;
            cout<<"\nNumero de dados: "<<val3;
        }
        
    }

    return 0;
}
