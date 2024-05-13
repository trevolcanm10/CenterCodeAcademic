/*Una compañía requiere registrar una relación de cajas de productos que
tiene en almacén, cada caja cuenta con un código numérico único y una
etiqueta con su peso.
• Elaborar un programa en C++ que permita registrar dichos paquetes al
final de una lista circular simplemente enlazada. Muestre la cantidad de
paquetes, el peso total y el peso promedio de todos los paquetes de la
lista.
• Aplicar el método de ordenamiento Burbuja para ordenar
ascendentemente la lista de paquetes según su peso. Muestre la lista
ordenada*/

#include<iostream>
using namespace std;
struct Nodo{
	int codigo;
	float peso;
	Nodo *siguiente;
};
typedef struct Nodo *Tlista;


void registrarCaja(Tlista &lista,int valor,float peso){
	Tlista q,t;
	q = new Nodo;
	q->codigo = valor;
	q->peso = peso;
	q->siguiente = lista;
	lista = q;
}


void mostrarCaja(Tlista lista){
	Tlista actual;
	actual=lista;
	while(actual!=NULL){
		cout<<"[ CD->"<<actual->codigo<<"][Peso->"<<actual->peso<<" kg]";
		actual=actual->siguiente;
	}
}

int cantidadPaquetes(Tlista lista){
	Tlista actual;
	actual = lista;
	int contador=0;
	while(actual!=NULL){
		contador++;
		actual=actual->siguiente;
	}
	return contador;
}
void promedioCajas(Tlista lista) {
    if (lista == NULL) {
        cout << "La lista esta vacia" << endl;
        return;
    }

    int suma = 0;
    int contador = 0;
    double promedio;
	Tlista actual;
	actual = lista;
    while (actual!= NULL) {
    	suma = suma + actual->peso;
        contador++;
        actual = actual->siguiente;
    }
	promedio = suma/contador;
	cout<<"El peso total de los paquetes es : "<<suma<<endl;
    cout <<"El promedio de los pesos de las cajas es : "<<promedio<<endl;
}

void intercambiar(Tlista &a, Tlista &b) {
    int tempCodigo = a->codigo;
    float tempPeso = a->peso;
    a->codigo = b->codigo;
    a->peso = b->peso;
    b->codigo = tempCodigo;
    b->peso = tempPeso;
}

void ordenarCajaPorPeso(Tlista lista) {
    if (lista == NULL || lista->siguiente == NULL) {
        return; // La lista está vacía o tiene solo un elemento, ya está ordenada.
    }

    bool intercambio;
    Tlista actual;
    Tlista siguiente = NULL;

    do {
        intercambio = false;
        actual = lista;

        while (actual->siguiente != siguiente) {
            if (actual->peso > actual->siguiente->peso) {
                intercambiar(actual, actual->siguiente);
                intercambio = true;
            }
            actual = actual->siguiente;
        }
        siguiente = actual;
    } while (intercambio);
}


int main(){
	Tlista lista = NULL;
	char opcion;
	int  codigo;
	float peso;
		do{
			cout<<"\nMenu"<<endl;
			cout<<"1.-Registra caja\n";
			cout<<"2.-Cantidad de paquetes\n";
			cout<<"3.-Peso total y promedio de los paquetes \n";
			cout<<"4.-Ordenar la lista de paquetes segun se peso -->Burbuja\n";
			cout<<"5.-Salir\n";
			cout<<"Seleccione una opcion\n";
			cin>>opcion;
			switch(opcion){
				case '1':	
					cout<<"Digite el codigo de la caja\n";
					cin>>codigo;
					cout<<"Digite el peso de la caja \n";
					cin>>peso;
					registrarCaja(lista,codigo,peso);
					cout<<"La cajas registradas son: \n";
					mostrarCaja(lista);
					break;
				case '2':
					cout<<"La cantidad de paquetes es: \n";
					cout<<cantidadPaquetes(lista);
					break;
				case '3':
					cout<<"Las cajas registradas son : \n";
					cout<<"__________________________\n";
					mostrarCaja(lista);
					cout<<"\n__________________________\n";
					promedioCajas(lista);
					break;
				case '4':
					cout<<"La lista de paquetes ordenada por peso es: \n";
					ordenarCajaPorPeso(lista);
					cout<<"__________________________\n";
					mostrarCaja(lista);
					cout<<"\n__________________________\n";
					break;
				case '5':
					cout<<"Salir del programa\n";
					break;
				default:
					cout<<"Opcion no valida,intente de nuevo"<<endl;
		}
	}while(opcion != 5);
}
