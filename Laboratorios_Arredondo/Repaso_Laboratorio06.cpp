/*Elaborar una solución en C++ para el caso
de la siguiente estructura de lista circular
doblemente enlazada:
1.- Ingresar nodos que contengan un código de identificación (puede ser alfanumérico o numérico) y un valor entre 100 y 300. Cada vez que se ejecute la opción debe insertar un nuevo nodo y permitir visualizar la lista
2.- Opción que permita recorrer la lista en sentido antihorario, restándole a cada nodo la cantidad de 50 por cada vuelta.
3.-Los nodos que lleguen a tener valores ceroo negativos, deberán ser extraídos ycolocados en una nueva lista enlazada simple.
Indicar el numero de vuelta y mostrar los elementos de la lista circular y de la lista simple 
Repetir hasta que la lista circular quede sin elementos*/
#include<iostream>
using namespace std;
struct Nodo{
	string codigo;
	int dato;
	Nodo *siguiente;
};
typedef struct Nodo *Tlista;

void insertarNodo(Tlista &lista, string codigo,int valor){
	Tlista q ;
	q = new Nodo();
	q->codigo = codigo;
	q->dato = valor;
	q->siguiente = lista;
	lista = q;
}
void mostrarLista(Tlista lista){
	Tlista actual;
	actual = lista;
	while(actual!=NULL){
		cout<<"["<<actual->codigo<<"],["<<actual->dato<<"]->";
		actual = actual->siguiente;
	}
}

void recorrerSentidoAntihorario(Tlista &lista){
    Tlista actual = lista;
    Tlista anterior = NULL;
    Tlista ultimo = NULL;
    while(actual->siguiente != NULL){
        anterior = actual;
        actual = actual->siguiente;
    }
    ultimo = actual;
    
    while(ultimo != NULL){
        int datoResto = 50;
        int datoOriginal = ultimo->dato;
        ultimo->dato = ultimo->dato - datoResto;
        actual = lista;
        anterior = NULL;
        while(actual != ultimo){
            anterior = actual;
            actual = actual->siguiente;
        }
        ultimo = anterior;
    }

}


void extraerNodosNegativos(Tlista &lista, Tlista &nuevaLista){
    Tlista actual = lista;
    Tlista anterior = NULL;

    while(actual != NULL){
        if(actual->dato <= 0){
            
            if(anterior != NULL){
                anterior->siguiente = actual->siguiente; 
            } else {
                lista = actual->siguiente; 
            }
            
            actual->siguiente = nuevaLista;
            nuevaLista = actual;

            /*
            actual = anterior != NULL ? anterior->siguiente : lista;
            */
            if (anterior != NULL) {
    			actual = anterior->siguiente;
			} else {
    			actual = lista;
			}
						
        } else {
            // Mover al siguiente nodo
            anterior = actual;
            actual = actual->siguiente;
        }
    }
}


int main(){
	Tlista lista = NULL;
	Tlista nuevaLista = NULL;
	char opcion;
	string codigo;
	int dato;
	do{
		cout<<"\nMenu:\n";
		cout<<"1.-Ingresar nodo\n";//Ingresar elemento al inicio de una lista enlazada
		cout<<"2.-Recorrer la lista en sentido antihorario - restamos a cada nodo la cantidad de 50 por cada vuelta\n";//Extraer elemento de la lista enlazada
		cout<<"3.-Extraer datos y distribucion a una nueva lista\n";
		cout<<"4.-Salir del programa\n";
		cin>>opcion;
		switch(opcion){
			case '1':
				cout<<"Digite el codigo de identificacion del nodo\n";
				cin>>codigo;
				cout<<"Digite el valor del nodo en el rango de (100-300)\n";
				cin>>dato;
				if(dato>=100 && dato<=300){
					insertarNodo(lista,codigo,dato);
					cout<<"Los elementos de la lista son: \n";
					mostrarLista(lista);
				}else{
					cout<<"Error,verifique la instruccion\n";
				}
				break;
			case '2':
				recorrerSentidoAntihorario(lista);
				cout<<"\n_______________________\n";
				cout<<"Lista actualizada\n";
				mostrarLista(lista);
				cout<<"\n_______________________\n";
				break;
			case '3':
				extraerNodosNegativos(lista, nuevaLista);
    			cout<<"\n_______________________\n";
   			 	cout<<"Lista circular:\n";
    			mostrarLista(lista);
    			cout<<"\n Nueva lista con nodos negativos:\n";
    			mostrarLista(nuevaLista);
    			cout<<"\n_______________________\n";
				break;
			case '4':
				cout<<"Saliendo del programa...\n";
				break;
			default:
				cout<<"Error,seleccione una opcion valida\n";
		}
	}while(opcion!=4);	
}
	
	
