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
	char destino;//Nacional o Internacional
	string codigo;//Alfa numérico
	Nodo *sgt;
};

typedef struct Nodo *Tlista;

void RegistrarSobres(Tlista &lista,char dest, string cod){
	Tlista actual;
	actual=lista;
	int contador=1;
	while(actual!=NULL){
		contador++;
		actual = actual->sgt;
	}
	
	//lLenando sobres
	if(contador>5){
		cout<<"Maximo 8 sobres, lleno \n";
		return;
	}
	Tlista q;
	q = new Nodo();
	q->destino = dest;
	q->codigo = cod;
	q->sgt = lista;
	lista = q;
}

void distribuirSobres(Tlista &lista,Tlista &colaNacional,Tlista &colaInternacional){
	int contColaN = 0, contColaI = 0;
	if(lista == NULL){
		cout<<"No hay sobres para distribuir \n";
	}
	while(lista!=NULL){
		Tlista actual;
		actual=lista;
		lista=lista->sgt;
		actual->sgt=NULL;
		if(actual->destino == 'N'){
			actual->sgt=colaNacional;
			colaNacional=actual;
			contColaN++;
		}else if(actual->destino == 'I'){
			actual->sgt=colaInternacional;
			colaInternacional=actual;
			contColaI++;
		}
		actual=actual->sgt;
	}
	cout<<"La cantidad de sobres pertenecientes a la cola nacional es : "<<contColaN<<endl;
	cout<<"La cantidad de sobres pertenecientes a la cola internacional es: "<<contColaI<<endl;
}

void mostrarSobres(Tlista lista){
	Tlista actual;
	actual = lista;
	while(actual!=NULL){
		cout<<"["<<actual->destino<<"]["<<actual->codigo<<"],";
		actual = actual->sgt;
	}
}

void mostrarCola(Tlista cola){
	Tlista actual;
	actual = cola;
	while(actual!=NULL){
		cout<<"["<<actual->destino<<"]["<<actual->codigo<<"],";
		actual = actual->sgt;
	}
}

void enviarSobre(Tlista &cola){
	if(cola == NULL){
		cout<<"Caja vacia \n";
	}
	Tlista actual;
	actual = cola;
	cola = cola->sgt;
	actual->sgt=NULL;
	delete actual;

}

int main(){
	Tlista lista = NULL,colaNacional = NULL, colaInternacional = NULL,cola=NULL;
	char opcion,dest;
	string cod;
	do{
		cout<<"\nMenu:\n";
		cout<<"1.-Registrar sobres\n";
		cout<<"2.-Distribuir sobres\n";
		cout<<"3.-Enviar sobres\n";
		cout<<"4.-\n";
		cout<<"5.-\n";
		cout<<"6.-";
		cout<<"7.-Salir del programa\n";
		cout<<"Seleccione la opcion:\n";
		cin>>opcion;
		cout<<"*********\n";
		switch(opcion){
			case '1':
				cout<<"Seleccione el destino Nacional(N) o Internacional(I)\n";
				cin>>dest;
				if(dest=='N'||dest=='I'){
				cout<<"Digite el codigo del sobre\n";
				cin>>cod;
				RegistrarSobres(lista,dest,cod);
				cout<<"Agencia de sobre \n";
				mostrarSobres(lista);	
				}else{
					cout<<"Error..\n";
				}
				break;
			case '2':
				distribuirSobres(lista,colaNacional,colaInternacional);
				cout<<"Sobres extraidos existosamente\n";
				cout<<"\n Elementos de la Cola Nacional \n";
				mostrarCola(colaNacional);
				cout<<"\n Elementos de la Cola Internacional \n";
				mostrarCola(colaInternacional);
				break;
			case '3':
				cout<<"Ingrese el destino del sobre a enviar Nacional(N) o Internacional(I)\n";
				cin>>dest;
				if(dest == 'N'){
					enviarSobre(colaNacional);
					cout<<"Enviados con éxito \n";
					cout<<"Cola Nacional : \n";
					mostrarCola(colaNacional);
				}else if(dest == 'I'){
					enviarSobre(colaInternacional);
					cout<<"Enviados con éxito \n";
					cout<<"Cola Internacional : \n";
					mostrarCola(colaInternacional);
				}
				break;
			default:
				cout<<"Error,seleccione una opcion valida\n";
		}
}while(opcion='3');

return 0;
}
