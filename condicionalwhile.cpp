// tiene 3 intentos para digitar la clave de un banco

#include <iostream>
using namespace std;
int main()
{
    int n=3, i=0, intento=0, clave=12345;
    usingned long L=1; // desde 0 a 2^61
    
    cout<<"Digite su contraseña ";
    cin>>intento;
    
    while(intento != clave && intento < 2) // que sea correcta && numero de intentos no pase de dos
    {
        cout<<"Clave incorrecta. tiene "<<2-intento<<"Intentos mas"<<endl;
        intento++; //primero lo uso luego sumo || ++intento; primero sumana luego uso la variable
        cout<<"Digite nuevamente su contraseña";
        cin>>intento;
    }
    if (intento != clave){
        cout<<"Cuenta Bloqueada !!"<<endl;
    }else{
        cout<<"Bienvenido a su cuenta !!"<<endl;
    }
    

    return 0;
}
