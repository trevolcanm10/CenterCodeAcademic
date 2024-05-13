/*
Utilizando Estructura de datos tipo Pilas y Colas , construir un algoritmo (aplicación en
C++) que permita simular el siguiente caso practico a través del menú de opciones:
En una Agencia de Correos, recibe sobres con destino Nacional o Internacional. Cada
sobre recibido indica el destino de envío, además se le asigna un código que lo
identifica.
Opción 1: Recibir sobres.- Permite registrar los sobres en una Pila de sobres recibidos
(soporta un máximo de 8 sobres) Mostrar los elementos de la Pila, indicando su
destino y código
Opción 2: Distribuir sobres.- Extrae un pedido según el tipo de envio y transferirlo a
una cola de Envíos Nacionales o Envíos Internacionales, según sea el caso. Mostrar los
elementos de la pila y de las dos colas, así como la cantidad de pedidos por cada cola
Opción 3.- Enviar Sobre.- Se indicará el tipo de envio (Nacional o Internacional) que se
va a despachar, seleccionándolo de la cola que le corresponda . Cada vez que se
ejecute esta opción, debe liberar un sobre de la cola. Mostrar los elementos de cada
cola y actualizar su cantidad.
*/
#include<iostream>
using namespace std;

struct Nodo{
	int dato;
	string destino;
	Nodo *siguiente;
};
typedef struct Nodo *Tlista;


void registrarSobres(Tlista &pila , int valor,string destino){
	int contador = 0;
	Tlista actual = pila;
	
	while(actual!=NULL){
		contador++;
		actual=actual->siguiente;
	}
	
	if(contador>=8){
		cout<<"La pila esta llena\n";
		return;
	}
	Tlista q;
	q = new Nodo();
	q->dato = valor;
	q->destino = destino;
	q->siguiente = pila;
	pila = q;
}

void mostrarSobres(Tlista pila){
	Tlista actual;
	actual = pila;
	while(actual!=NULL){
		cout<<"Destino : "<<actual->destino<<", Codigo: "<<actual->dato<<endl;
		actual = actual->siguiente;
	}
}

void extraerPedido(Tlista &pila,Tlista &colaNacional,Tlista &colaInternacional){
	if(pila==NULL){
		cout<<"La pila no contiene elementos \n";
	}
	while(pila!=NULL){
		Tlista temp = pila;
		pila = pila->siguiente;
		temp->siguiente = NULL;
		
		if(temp->destino == "Nacional"){
			temp->siguiente =colaNacional;
			colaNacional = temp;
		}else if(temp->destino == "Internacional"){
			temp->siguiente = colaInternacional;
			colaInternacional = temp;
		}
	
	}
}

void mostrarCola(Tlista cola,string nombreCola){
	cout<<"Contenido de la cola"<<nombreCola<<":"<<endl;
	int cantidadPedidos = 0;
	Tlista actual = cola;
	while(actual!=NULL){
		cout << "Destino: " << actual->destino << ", Codigo: " << actual->dato << endl;
		cantidadPedidos++;
        actual = actual->siguiente;
	}
	cout<<"Cantidad de pedidos en la cola"<<nombreCola<<":"<<cantidadPedidos<<endl;
}

void enviarSobre(Tlista &cola,string nombreCola){
	if(cola ==NULL){
		cout << "La cola está vacía, no hay sobres para enviar." << endl;
        return;
	}
	
	Tlista temp = cola;
	cola = cola->siguiente;
	temp->siguiente = NULL;
	cout << "Se ha enviado el sobre con destino " << temp->destino << " y código " << temp->dato << endl;
    delete temp;
    
    mostrarCola(cola,nombreCola);
}
int main(){
	Tlista pila = NULL;
	Tlista colaNacional = NULL;
	Tlista colaInternacional = NULL;
	string cadena,destino;
	int dato;
	char opcion;
	do{
		cout<<"\nMenu:\n";
		cout<<"1.-Registrar sobres\n";
		cout<<"2.-Extraer pedido y distribuirlo a una cola Nacional - Internacional\n";
		cout<<"3.-Mostrar cola Nacional\n";
		cout<<"4.-Mostrar cola Internacional\n";
		cout<<"5.-Mostrar elementos de la pila,colaNacional,colaInternacional\n";
		cout<<"6.-Enviar sobre\n";
		cout<<"7.-Salir del programa\n";
		cout<<"Seleccione la opcion:\n";
		cin>>opcion;
		cout<<"*********\n";
		switch(opcion){
			case '1':
				cout<<"Registrar sobres Nacionales(N) o Internacionales(I)\n";
				cin>>cadena;
				cout<<"Asigne el codigo al sobre registrado \n";
				cin>>dato;
				if(cadena =="N" || cadena =="I"){
					registrarSobres(pila,dato,(cadena == "N"? "Nacional":"Internacional"));
					cout<<"Sobre registrado \n";
					if(cadena == "N"){
						cout<<"Nacional";
					}else{
						cout<<"Internacional";
					}
					cout<<"-> "<<dato<<endl;
				}else{
					cout<<"Error,opcion no valida \n";
				}
				mostrarSobres(pila);
				break;
			case '2':
				extraerPedido(pila,colaNacional,colaInternacional);
				cout<<"Extraidos y distribuidos correctamente\n";
				break;
			case '3':
				mostrarCola(colaNacional,"Nacional");
				break;
			case '4':
				mostrarCola(colaInternacional,"Internacional");
				break;
			case '5':
				cout<<"Los elementos de la pila son: \n";
				mostrarSobres(pila);
				cout<<"Los elementos de la colaNacional son: \n";
				mostrarCola(colaNacional,"Nacional");
				cout<<"Los elementos de la colaInternacional son: \n";
				mostrarCola(colaInternacional,"Internacional");
				break;
			case '6':
				cout << "Seleccione la cola desde la cual desea enviar el sobre:" << endl;
    			cout << "1. Cola Nacional" << endl;
    			cout << "2. Cola Internacional" << endl;
    			cout << "Opción: ";
    			 int opcionCola;
			    cin >> opcionCola;
			
			    switch (opcionCola) {
			        case 1:
			            enviarSobre(colaNacional, "Nacional");
			            break;
			        case 2:
			            enviarSobre(colaInternacional, "Internacional");
			            break;
			        default:
			            cout << "Opcion no valida." << endl;
			    }
				break;
			case '7':
				cout<<"Saliendo del programa....\n";
				break;
			default:
				cout<<"Error,seleccione una opcion valida\n";
		}
	}while(opcion!=7);
}
