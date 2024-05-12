/*1. Opción 1: Permita crear un nodo con un valor entero (puede ser positivo o
negativo, asignado al azar, a excepción del cero). Basado en esto, considerar lo
siguiente:
a. Si la el valor es negativo, el nodo deberá insertarse al inicio de la lista enlazada
b. Si el valor es positivo, el nodo deberá insertarse al final de la lista enlazada
c. Mostrar la lista enlazada por cada nuevo nodo que se ingrese
2. Opción 2: Recorrer la lista enlazada y mostrar el valor mayor y menor, así como
sus correspondientes posiciones en la lista (si hay duplicado, mostrar uno de
ellos). Adicionalmente obtener la cantidad de elementos de la lista y la suma
promedio de los valores de los nodos
*/
#include<iostream>
using namespace std;
struct Nodo{
	int dato;
	Nodo *siguiente;
};
typedef struct Nodo *Tlista;
void insertarAlInicio(Tlista &lista,int valor){
	Tlista q;
	q = new Nodo();
	q->dato=valor;
	q->siguiente=lista;
	lista=q;
}
void insertarAlFinal(Tlista &lista,int valor){
	Tlista q,t;
	q = new Nodo();
	q->dato=valor;
	q->siguiente=NULL;
	if(lista==NULL){
		lista=q;
	}else{
		t=lista;
		while(t->siguiente!=NULL){
			t=t->siguiente;
		}
		t->siguiente=q;
	}
}

void mostrarLista(Tlista lista){
	Tlista actual;
	actual = lista;
	while(actual!=NULL){
		cout<<actual->dato<<" ";
		actual=actual->siguiente;
	}
}

void encontrarMayorMenor(Tlista lista,int &mayor,int &menor,int &posMayor,int &posMenor){
	Tlista actual;
	actual = lista;
	mayor = lista->dato;
	menor = lista->dato;
	posMayor = 1;
	posMenor = 1;
	
	if(actual == NULL){
		cout<<"La lista no contiene elementos \n";
		return;
	}
	int posicion=1;
	while(actual!=NULL){
		if(actual->dato>mayor){
			mayor=actual->dato;
			posMayor=posicion;
		}
		if(actual->dato<menor){
			menor=actual->dato;
			posMenor=posicion;
		}
		actual=actual->siguiente;
		posicion++;
	}
}

float promedioLista(Tlista lista){
	Tlista actual;
	actual = lista;
	int suma=0,contador=0;
	float promedio;
	if(lista == NULL){
		cout<<"La lista no tiene elementos\n";
		return 0;
	}
	while(actual!=NULL){
		suma = suma + actual->dato;
		contador++;
		actual=actual->siguiente;
	}
	
	promedio = suma/contador;
	return promedio;
}

int contarElementos(Tlista lista){
	Tlista actual = lista;
	int contador = 0;
	while(actual !=NULL){
		contador++;
		actual = actual->siguiente;
	}
	return contador;
}
int main(){
	Tlista lista = NULL;
	int dato;
	char opcion;
	
	do{
		cout<<"*********\n";
		cout<<"Menu:\n";
		cout<<"1.-Insertar valores al principio de la lista-->Valores negativos \n";
		cout<<"2.-Insertar valores al final de la lista -->Valores positivos \n";
		cout<<"3.-Encontrar al mayor y menor de la lista \n";
		cout<<"4.-Mostrar valores de la lista\n";
		cout<<"5.-Promedio de los valores de la lista\n";
		cout<<"6.-Salir del programa\n";
		cout<<"Seleccione la opcion:\n";
		cin>>opcion;
		cout<<"*********\n";
		switch(opcion){
			case '1':
				cout<<"Ingrese un valor\n";
				cin>>dato;
				if(dato<0){
					insertarAlInicio(lista,dato);
					cout<<"Los elementos de la lista son:\n";
					mostrarLista(lista);	
				}else{
					cout<<"Error,verifique la instruccion \n";
				}
				break;
			case '2':
				cout<<"Ingrese un valor\n";
				cin>>dato;
				if(dato>0){
					insertarAlFinal(lista,dato);
					cout<<"Los elementos de la lista son: \n";
					mostrarLista(lista);	
				}else{
					cout<<"Error,verifique la instruccion \n";
				}
				break;
			case '3':
				int mayor , menor,posMayor,posMenor;
				encontrarMayorMenor(lista,mayor,menor,posMayor,posMenor);
				cout<<"El mayor elemento de la lista es : "<<mayor<<" en la posicion: "<<posMayor<<endl;
				cout<<"El menor elemento de la lista es : "<<menor<<" en la posicion: "<<posMenor<<endl;
				break;
			case '4':
				cout<<"Los elementos de la lista\n";
				mostrarLista(lista);
				break;
			case '5':
				float promedio;
				promedio = promedioLista(lista);
				cout<<"La cantidad de elementos en la lista es:"<<contarElementos(lista)<<endl;
				cout<<"El promedio de los valores en la lista es:"<<promedio<<endl;
				break;
			case '6':
				break;
			default:
				cout<<"Error,seleccione una opcion valida\n";
		}
	}while(opcion!=6);
}
	
