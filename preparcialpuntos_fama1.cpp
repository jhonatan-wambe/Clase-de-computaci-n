// en el numero 78 para hallar el 8 se puede hacer asi 78 % 10 = 78
// en el numero 78 para hallar el 7 se puede hacer asi 78 / 10 = 7 (en python se pone //)
// definir al inicio que 78 es un entero 
// if (!gano) significa no gano

#include <iostream>
using namespace std;

int main()
{
    int numsec;
    int numb;
    int unidades;
    int fama;
    int punto;
    bool gano = false; // se niega porque no ha ganado nada
    
    cout<<"jugador A, ingrese el número secreto";
    cin>>numsec;
    
    if(num < 10 || numsec > 99)
    {
       cout<<"Numero invalido " ;
    }
    else
    {
        decenas = numsec / 10;
        unidades = numsec % 10;
        
        //intento 1
        cout<<"Jugador B, ingrese cual cree que es el numero secreto";
        cin>>numb;
        if(numb < 10 || numb > 99)
        {
            cout<<"Numero invalido -pierde turno";
        }
        else
        {
            fama = 0;
            punto = 0;
            //verificando si el digito de las decenas está en el numero secreto
            if(numb == numsec)
            {
                cout<<"El jugador B gano !!"
                gano = true;
            }
            else{
                fama = 0;
                punto = 0;
                //verifico si el digito de las decenas está en el numero secreto
                if (numb/10 == decenas)
                {
                    punto++;
                }
                else (numb/10 == unidades)
                {
                    punto++;
                }
                //Verifico si el dígito de las unidades está en el número secreto
                if(numb%10 == decenas)
                {
                    punto++;
                }
                else if(numb%10 == unidades)
                {
                    fama++;
                }
                cout<<"El número ingresado tiene "<<fama<<" famas y "<<punto<<" puntos"<<endl;
            }
        }
        // Fin intento 1
        
        //Intento 2
        if(!gano){
            cout<<"Jugador B, ingrese cuál cree que es el número secreto";
            cin>>numb;
            if(numb < 10 || numb > 99){
                cout<<"Número inválido - Pierde turno";
            }else{
                if(numb == numsec){
                    cout<<"El jugador B Ganó!";
                    gano = true;
                }else{
                    fama = 0;
                    punto = 0;
                    //Verifico si el dígito de las decenas está en el número secreto
                    if(numb/10 == decenas){
                        fama++;
                    }else if(numb/10 == unidades){
                        punto++;
                    }
                    //Verifico si el dígito de las unidades está en el número secreto
                    if(numb%10 == decenas){
                        punto++;
                    }else if(numb%10 == unidades){
                        fama++;
                    }
                    cout<<"El número ingresado tiene "<<fama<<" famas y "<<punto<<" puntos"<<endl;
                }
            }
        }
        //Fin intento 2
        
        //Intento 3
        if(!gano){
            cout<<"Jugador B, ingrese cuál cree que es el número secreto";
            cin>>numb;
            if(numb < 10 || numb > 99){
                cout<<"Número inválido - Pierde turno";
            }else{
                if(numb == numsec){
                    cout<<"El jugador B Ganó!";
                    gano = true;
                }else{
                    fama = 0;
                    punto = 0;
                    //Verifico si el dígito de las decenas está en el número secreto
                    if(numb/10 == decenas){
                        fama++;
                    }else if(numb/10 == unidades){
                        punto++;
                    }
                    //Verifico si el dígito de las unidades está en el número secreto
                    if(numb%10 == decenas){
                        punto++;
                    }else if(numb%10 == unidades){
                        fama++;
                    }
                    cout<<"El número ingresado tiene "<<fama<<" famas y "<<punto<<" puntos"<<endl;
                }
            }
        }
        //Fin intento 3
        
        //Intento 4
        if(!gano){
            cout<<"Jugador B, ingrese cuál cree que es el número secreto";
            cin>>numb;
            if(numb < 10 || numb > 99){
                cout<<"Número inválido - Pierde turno";
            }else{
                if(numb == numsec){
                    cout<<"El jugador B Ganó!";
                    gano = true;
                }else{
                    fama = 0;
                    punto = 0;
                    //Verifico si el dígito de las decenas está en el número secreto
                    if(numb/10 == decenas){
                        fama++;
                    }else if(numb/10 == unidades){
                        punto++;
                    }
                    //Verifico si el dígito de las unidades está en el número secreto
                    if(numb%10 == decenas){
                        punto++;
                    }else if(numb%10 == unidades){
                        fama++;
                    }
                    cout<<"El número ingresado tiene "<<fama<<" famas y "<<punto<<" puntos"<<endl;
                }
            }
        }
        //Fin intento 4
        
        //Intento 5
        if(!gano){
            cout<<"Jugador B, ingrese cuál cree que es el número secreto";
            cin>>numb;
            if(numb < 10 || numb > 99){
                cout<<"Número inválido - Pierde turno";
            }else{
                if(numb == numsec){
                    cout<<"El jugador B Ganó!";
                    gano = true;
                }else{
                    fama = 0;
                    punto = 0;
                    //Verifico si el dígito de las decenas está en el número secreto
                    if(numb/10 == decenas){
                        fama++;
                    }else if(numb/10 == unidades){
                        punto++;
                    }
                    //Verifico si el dígito de las unidades está en el número secreto
                    if(numb%10 == decenas){
                        punto++;
                    }else if(numb%10 == unidades){
                        fama++;
                    }
                    cout<<"El número ingresado tiene "<<fama<<" famas y "<<punto<<" puntos"<<endl;
                }
            }
        }
        //Fin intento 5
    }

    return 0;
}
