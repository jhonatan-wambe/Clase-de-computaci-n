
#include <iostream>
#include <math.h>
using namespace std;
int main()
{
    int edad=0, trabajo=0, estudia=0, comida=0;
    float promedio=0, tasa=0;
    
    cout<<"*** OLDIE BANK ***\n";
    cout<<"Digite su edad "; cin>>edad;
    
    cout<<"\n¿Comida preferida?";
    cout<<"\n 1 Hamburguesa ";
    cout<<"\n 2 Perro caliente";
    cout<<"\n 3 Pizza";
    cout<<"\n 4 Sushi";
    cout<<"\n- Digite el numero: "; cin>>comida;
    
    cout<<"\nDigite 1 SI | 2 NO";
    cout<<"\n¿Usted estudia? "; cin>>estudia;
    if (estudia == 1){
        cout<<"\nBienvenido Estudiante";
        cout<<"\nDigite su promedio: "; cin>>promedio;
    }
    cout<<"\nDigite 1 SI | 2 NO";
    cout<<"\n¿Usted trabaja? "; cin>>trabajo;
    
    if (edad < 20)
    {
        tasa == .20;
        cout<<"\nEdad por debajo de 20";
        if (Estudiante == 1)
        {
            if(promedio < 3.5)
            {
                tasa = tasa + 0.5;
            }
        }
    }else
    {
        cout<<"\nEdad por encima de 20 años";
    }
    
    

    return 0;
}
