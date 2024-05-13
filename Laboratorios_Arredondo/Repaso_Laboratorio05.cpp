/*
1.-Crear una pila que permita maximo solo 5 elementos,
ademas que solo permite ingresar pesos de 10 y 50.
2.-Extraemos la pila uno por uno y la cargamos en una lista.
3.-Asignar pesos al azar entre 10 y 20 , recorriendo desde el inicio de la lista
a los elementos que ya existen(ida).
4.-Asignar pesos al azar entre 30 y 50 , recorriendo desde el ultimo elemento de la lista
adiciona a cada elemento que ya existe(vuelta).
5.-Se elimina los elementos cuyo peso total o acumulado es mayor a 75
*/
	

#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;
struct Nodo{
	int dato;
	Nodo *siguiente;
};
typedef struct Nodo *Tlista;

void pushPila(Tlista &pila , int valor){
	int contador = 0;
	Tlista actual = pila;
	
	while(actual!=NULL){
		contador++;
		actual=actual->siguiente;
	}
	
	if(contador>=5){
		cout<<"_____________________\n";
		cout<<"La pila esta llena";
		cout<<"\n_____________________\n";
		return;
	}
	Tlista q;
	q = new Nodo();
	q->dato = valor;
	q->siguiente = pila;
	pila = q;
}


void mostrarPila(Tlista pila){
	Tlista actual;
	actual = pila;
	while(actual!=NULL){
		cout<<actual->dato<<" ";
		actual = actual->siguiente;
	}
}
void extraerDato_Lista(Tlista &pila,Tlista &lista){
	if(pila==NULL){
		cout<<"La pila no contiene elementos \n";
	}
		Tlista temp = pila;
		pila=pila->siguiente;
		temp->siguiente = NULL;
		temp->siguiente = lista;
		lista = temp;

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

void asignarPesosAzar(Tlista &lista){
    srand(time(NULL));
    Tlista actual = lista;
    while(actual != NULL){
        int pesoAleatorio = rand() % 11 + 10;
        int pesoOriginal = actual->dato;
		actual->dato = actual->dato + pesoAleatorio;
        cout << "Peso original-> " << pesoOriginal << ", Peso aleatorio -> " << pesoAleatorio << endl;
        actual = actual->siguiente;
    }
}

void asignarPesosAzarVuelta(Tlista &lista){
    srand(time(NULL)); 

    Tlista actual = lista;
    Tlista anterior = NULL;
    Tlista ultimo = NULL;

    while(actual->siguiente != NULL){
        anterior = actual;
        actual = actual->siguiente;
    }
    ultimo = actual;
    
    while(ultimo != NULL){
        int pesoAleatorio = rand() % 21 + 30;
        int pesoOriginal = ultimo->dato;
        ultimo->dato += pesoAleatorio;
        cout << "Peso original ->" << pesoOriginal << ", Peso aleatorio -> " << pesoAleatorio << endl;
        actual = lista;
        anterior = NULL;
        while(actual != ultimo){
            anterior = actual;
            actual = actual->siguiente;
        }
        ultimo = anterior;
    }
}

void eliminarPesoMayor(Tlista &lista){
    Tlista actual = lista;
    Tlista anterior = NULL;
    
    while(actual != NULL){
        
        if(actual->dato > 75){
            if(anterior != NULL){
                anterior->siguiente = actual->siguiente;
                delete actual;
                actual = anterior->siguiente; 
            } else {
                lista = actual->siguiente;
                delete actual;
                actual = lista; 
            }
        } else {
            anterior = actual;
            actual = actual->siguiente;
        }
    }
}

int main(){
	Tlista pila = NULL;
	Tlista lista = NULL;
	int dato;
	char opcion;
	do{
		cout<<"\nMenu:\n";
		cout<<"1.-Ingresar elemento en la pila\n";//Ingresar elemento al inicio de una lista enlazada
		cout<<"2.-Descargar elemento de la pila\n";//Extraer elemento de la lista enlazada
		cout<<"3.-Asignar pesos a la lista(ida)\n";
		cout<<"4.-Asignar pesos a la lista(vuelta)\n";
		cout<<"5.-Eliminar elemento\n";
		cout<<"6.-Mostrar Lista\n";
		cout<<"7.-Salir del programa\n";
		cout<<"Seleccione una opcion \n";
		cin>>opcion;
		switch(opcion){
			case '1':
				cout<<"Inserte un peso en el rango de 10-50:\n";
				cin>>dato;
				if(dato>=10 && dato<=50){
					pushPila(pila,dato);
					cout<<"\nLos pesos ingresados son:\n";
					mostrarPila(pila);
				}else{
					cout<<"Dato ingresado invalido,verifique la instraccion\n";
				}
				break;
			case '2':
				extraerDato_Lista(pila,lista);
				cout<<"Los elementos de la lista son: \n";
				mostrarPila(lista);
				break;
			case '3':
				 asignarPesosAzar(lista);
   	 			 cout << "Pesos aleatorios asignados a cada elemento existente en la lista.\n" << endl;
   	 			 cout<<"___________________________________________\n";
    		     cout << "Lista actualizada con los nuevos pesos:" << endl;
    			 mostrarPila(lista);
    			 cout<<"\n__________________________________________\n";
				break;
			case '4':
				 asignarPesosAzarVuelta(lista);
    			 cout << "Pesos aleatorios entre 30 y 50 asignados a cada elemento existente en la lista (vuelta)." << endl;
    			 cout<<"___________________________________________\n";
    			 cout << "Lista actualizada con los nuevos pesos:" << endl;
                 mostrarPila(lista);
                 cout<<"\n___________________________________________\n";
				break;
			case '5':
				eliminarPesoMayor(lista);
    			cout << "Elementos con peso total mayor a 75 eliminados correctamente." << endl;
			    cout << "Lista actualizada:" << endl;
			    cout<<"___________________________________________\n";
			    mostrarPila(lista);
			    cout<<"\n___________________________________________\n";
			    break;
			case '6':
				cout<<"Los elementos de la lista son : \n";
				cout<<"___________________________________________\n";
				mostrarPila(lista);
				cout<<"\n___________________________________________\n";
				break;
			case '7':
				break;
			default:
				cout<<"Error,seleccione una opcion valida\n";
		}
	}while(opcion!=7);	
}
