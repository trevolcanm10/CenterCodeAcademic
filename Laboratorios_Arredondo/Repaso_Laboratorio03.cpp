/*Operaciones sobre listas enlazadas simples
Generar un menú de opciones en C++ el cual permita realizar las operaciones de una lista simplemente enlazada,
según lo siguiente:
Opción 1.- Permita insertar y mostrar números al final de una lista simplemente enlazada, de tal forma que el
numero a insertar sea menor al valor promedio de los elementos de la lista.
Opción 2.- Crear un nuevo nodo que contenga un numero impar e insertarlo en la posición media de la lista
Opción 3.- Ubicar el elemento con menor valor (mostrar su valor y posición) y eliminarlo de la lista.
Opción 4.- Mostar los elementos de la lista
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
	q->dato = valor;
	q->siguiente = lista;
	lista = q;
}

void insertarAlFinal(Tlista &lista,int valor){
	Tlista t,q;
	q = new Nodo();
	q->dato = valor;
	q->siguiente = NULL;
	if(lista == NULL){
		lista = q;
	}else{
		t = lista;
		while(t->siguiente!=NULL){
			t = t->siguiente;
		}
		t->siguiente = q;
	}
}

void mostrarLista(Tlista lista){
	Tlista actual;
	actual = lista;
	while(actual!=NULL){
		cout<<actual->dato<<" ";
		actual = actual->siguiente;
	}
}

void insertarPosicionMedia(Tlista &lista,int valor){
	Tlista q,actual;
	int medida = 0;//Tamaño de la lista
	q = new Nodo();
	q->dato= valor;
	q->siguiente = NULL;
	actual = lista;
	while(actual!=NULL){
		medida++;
		actual = actual->siguiente;
	}
	
	int posMedia;
	posMedia = medida/2;//La mitad del elemento de la lista
	
	actual = lista;
	Tlista anterior = NULL;
	int posActual = 0;
	while(posActual<posMedia && actual!=NULL){
		anterior = actual;
		actual = actual->siguiente;
		posActual++;
	}
	if(anterior == NULL){
		q->siguiente = lista;
		lista = q;
	}else{
		anterior->siguiente = q;
		q->siguiente = actual;
	}
}

void eliminarMenor(Tlista &lista){
	if(lista == NULL){
		cout<<"La lista esta vacia \n";
		return;
	}
	Tlista menor = lista;
	Tlista anterior = NULL;
	Tlista actual = lista->siguiente;
	int posicion = 2;
	int posicionMenor = 1;
	while(actual!=NULL){
		if(actual->dato < menor->dato){
			menor = actual;
			posicionMenor = posicion;
			anterior = lista;
		}
		actual = actual->siguiente;
		posicion++;
	}
	cout<<"El elemento con el menor valor es: "<<menor->dato<<endl;
	cout<<"Se encontraba en la posicion: "<<posicionMenor<<endl;
	if(anterior == NULL){
		lista = lista->siguiente;
		delete menor;
	}else{
		anterior->siguiente = menor->siguiente;
		delete menor;
	}
}
int promedioLista(Tlista lista){
	Tlista actual;
	actual = lista;
	int suma=0,contador=0;
	float promedio;
	if(lista == NULL){
		cout<<"La lista no presenta elementos\n";
	}
	while(actual!=NULL){
		suma=suma+actual->dato;
		contador++;
		actual=actual->siguiente;
	}
	promedio=suma/contador;
	return promedio;
}
int main(){
	Tlista lista = NULL;
	int dato;
	char opcion;
	do{
		cout<<"\n*****************************\n";
		cout<<"Menu:\n";
		cout<<"1.-Insertar valores\n";
		cout<<"2.Calculo del promedio e insercion al final de la lista \n";
		cout<<"3.-Insertar elemento impar en el medio de la lista \n";
		cout<<"4.-Buscar el menor elemento y eliminarlo\n";
		cout<<"5.-Mostrar valores de la lista\n";
		cout<<"Seleccione una opcion: \n";
		cin>>opcion;
		switch(opcion){
			case '1':
				cout<<"\nDigete el valor que desee insertar\n";
				cin>>dato;
				insertarAlInicio(lista,dato);
				cout<<"Los elementos de la lista son \n";
				mostrarLista(lista);
				break;
			case '2':
				cout<<"\nDigite el valor que desea insertar\n";
				cout<<"Ingrese un valor menos al promedio de la lista\n";
				cout<<"El promedio de la lista es : "<<promedioLista(lista)<<endl;
				cin>>dato;
				if(dato<promedioLista(lista)){
					cout<<"El promedio de la lista es :"<<promedioLista(lista)<<endl;
					insertarAlFinal(lista,dato);
					mostrarLista(lista);
				}else{
					cout<<"Elemento no insertardo(dato > promedio)\n";
				}
				break;
			case '3':
				cout<<"Digite el numero a insertar-->Impar"<<endl;
				cin>>dato;
				if(dato%2!=0){
					insertarPosicionMedia(lista,dato);
					cout<<"Elemento insertado con exito\n";
					cout<<"Lista actualizada \n";
					mostrarLista(lista);
				}else{
					cout<<"Error,verifique la instruccion"<<endl;
				}
				break;
			case '4':
				eliminarMenor(lista);
				break;
			case '5':
				cout<<"Elementos de la lista : \n";
				cout<<"_______________________\n";
				mostrarLista(lista);
				cout<<"\n_____________________\n";
				break;
			default:
				cout<<"Error,ingrese un opcion validad \n";	
		}
		
	}while(opcion!=5);		
}
