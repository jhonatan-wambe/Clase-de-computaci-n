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

#include <iostream>
using namespace std;


void leer_v(int v[]){
    int i,r=0;
    // llenar el vector
    for(i=0; i<10; i++)
    {
        r=rand()%100;
        v[i]=r;
        cout<<"v["<<i<<"]= "<<v[i]<<endl;
    }
}

void v_pares(int v[])
{
    int v_pares[10], k=0, i;
    for (i=0; i<10;i++){
        v_pares[10]=0;
    }
    for (i=0; i<10;i++)
    {
        if (v[i] % 2==0){
            v_pares[k]=v[i];
            k++;
        }
    }
    for (i=0; i<10; i++){
        cout<<v[i]<<" ";
    }
    cout<<endl;
    for(i=0; i<10; i++){
        cout<<v_pares[i]<<"  ";
    }
    cout<<endl;
}

int main()
{
    // declarar variables
    int v[10], valor;
    leer_v(v);
    v_pares(v);
    return 0;
}


#include <iostream>
using namespace std;
int main()
{
    int divisor = 2, numero; 
    cout<<"ingrese numero:"; cin>>numero;
    cin<<numero;
    while(numero%divisor!=0){
        divisor=divisor+1;
    }
    if (numero==divisor){
        cout<<"Es primo";
    }else{
        cout<<"No es primo";
    }
    return 0;
}

// https://www.codigazo.com/en-c/codigos-para-recorrer-arreglo-en-c

#include <iostream>
using namespace std;

int main()
{
    int v[6],i,r=0;
    
    for(i=0; i<6; i++){
        //cout<<"V["<<i<<"]";
        r=rand()%100;
        v[i]=r;
    }
    for(i=0; i<6; i++){
        cout<<"V["<<i<<"]= "<<v[i]<<endl;
    }
    return 0;
}

#include <iostream>
using namespace std;

const int b=0;

void leer_v(int v[]){
    int i,r=0;
    // llenar el vector
    for(i=0; i<6; i++)
    {
        r=rand()%100;
        v[i]=r;
        cout<<"v["<<i<<"]= "<<v[i]<<endl;
    }
}

int buscar_dato(int v[], int valor){
    int i, posicion;
    for (i=0; i<6;i++){
        if (v[i]==valor){
            posicion = i;
        }else{
            posicion = -1;
        }
    }
    return posicion;
}

int main()
{
    // declarar variables
    int v[6], valor;
    leer_v(v);
    cout<<"Que valor desea buscar: ";
    cin>>valor;
    cout<<"El valor "<<valor<<" Buscado esta en la posicion: "<<buscar_dato(v, valor)<<endl;
    return 0;
}




