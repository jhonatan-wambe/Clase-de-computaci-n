

#include<iostream>
#include <cmath>

using namespace std;
int main()
{ 
    int x=0, y=0;
    float ecuacion1=0, raiz_ecuacion1=0, ecuacion2=0, aux=0, raiz_aux=0;
    cout<<" "<<endl;
    cout<<"Hallar Z"<<endl;
    cout<<"Digite x: "<<endl;
    cin>>x;
    cout<<"Digite Y: "<<endl;
    cin>>y;

    ecuacion1 = (x + (pow(y, 2) / 3 + x));
    raiz_ecuacion1 = pow(ecuacion1, 1/2.); // 0.5 es lo mismo que (1/2)
    aux = 3 * x; // Para sacar la n raiz de un numero seria pow(a, 1/n.);
    raiz_aux = pow(aux, 1/2.);
    ecuacion2 = ((pow(x,2) / (pow(y,3) + x)) - 5) * raiz_aux;
    cout<<"Resultado ecuacion: "<<raiz_ecuacion1 - ecuacion2;
    return 0;
}
