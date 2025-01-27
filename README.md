#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    // Declaracion de variables
    string nombre, cargo,contador_de_registros, n;
    int salario;
    float as, ap, st, t_pagar;
    
    //Captura de Datos
    cout<<"Desea hacer un registro: ";
    cin>>contador_de_registros;
    
    cout<<"Digite su nombre: ";
    cin>>nombre;
    cout<<"Digite su cargo: ";
    cin>>cargo;
    cout<<"Digite el valor de su salario: ";
    cin>>salario;
    

    //formulas para el calculo
    as=salario*0.004;
    ap=salario*0.004;
    
    if(salario > (1423500*2))
    {
        st=0;
    }
    else
    {
        st=200000;
    }
    t_pagar=salario-ap-as+st;
    
    cout<<nombre<<" tiene un total de "<<t_pagar<<endl;
    
    

    return 0;
}
