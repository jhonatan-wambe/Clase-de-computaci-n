/*/ Clase 29 enero
Hacer un programa con la siguentes funciones
1. calcular subtotal: recibe por parametro precio del producto y cantidad vendida.
permite calcular el subtotal.

2. calcular valor iva: usa la funcion calcular sub total y calcula el valor del iva.

3. calcular descuento: si la cantidad es superior a 50 unidades, hacer un descuento del
20 %, si la cantidad se encuentra entre 10 y 20 unidades hacer un descuento del 30%. si la 
cantidad es inferior a 10 hacer un descuento del 40 %.

4 calcular el total.

imprimir el nombre del cliente, el producto comprado y el total a pagar.
*/


#include <iostream>
#include <math.h>
#include <string>

using namespace std;
const double IVA = 0.19, ;

int Subtotal(int precio, int cantidad){
    return cantidad * precio;
}

double Iva_descuento(double precio, double cantidad){
    return Subtotal(precio, cantidad) * IVA;
}

double Descuento(int cantidad){
    if cantidad()
}

int main()
{
    int subtotal = Subtotal(1000, 50);
    double j = Iva_descuento(1000, 50);
    
    cout<<"El subtotal de la venta: "<<subtotal<<endl;
    cout<<"El subtotal de la venta-iva: "<<subtotal - j<<endl;
}
