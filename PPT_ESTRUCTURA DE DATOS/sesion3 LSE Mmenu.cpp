#include <iostream>

using namespace std;

struct nodo{
	int nro;
	int tipo;
	struct nodo *sgte; 	
	
};

typedef struct nodo *TpLista;// crear tipo de dato struct nodo
// Funcion para crear Nodo
TpLista  crearNodo(){
	int n, t;
	TpLista q=new(struct nodo );
	system("CLS");
	cout<<"\nIngresar numero--> ";cin>>n;
	cout<<"\nIngresar Tipo--> ";cin>>t;
	q->nro=n;
	q->tipo=t;
	q->sgte = NULL;
	return q;
}

void mostrarLista(TpLista lista){
	TpLista t=lista;
	while(t != NULL ){
		cout<<"nr = "<<t->nro<<" tipo= "<<t->tipo<<" --> ";
		t=t->sgte;
	}
	cout<<" NULL"<<endl;
}

void insertarInicio(TpLista &lista){
	TpLista w= crearNodo();
	w->sgte=lista;
	lista=w;
}
void insertarFinal(TpLista &lista){
	
	TpLista w= crearNodo(),t=lista;

	while(t->sgte != NULL)
		t=t->sgte;
	t->sgte=w;	
}

void insertarPosicion(TpLista &lista, int pos){
	
	TpLista w= crearNodo(),t=lista, s=NULL;
	int x=1;
	bool flag=false;
	if(pos ==1)
		insertarInicio(lista);
	else{
		while( x != pos &&  t->sgte != NULL){
			s=t;
			t=t->sgte;
			x++;
			if(x==pos)
				flag=true;
			
		}
		
	if(flag ==false){
		cout<<" Error, posicion ingresada no existe..."<<endl;
		
	}else{
		
		s->sgte=w;
		w->sgte=t;	
	}
			
		
	}
		
}

void eliminarInicio(TpLista &lista){
	TpLista w=lista;
	lista=lista->sgte;
	delete(w);
	
}
 void eliminarFinal(TpLista &lista){
 	TpLista t=lista, s=NULL;
 	while(t->sgte != NULL){
 		s=t;
 		t=t->sgte;
	 }
 	s->sgte=NULL;
 	delete(t);
 }

void eliminarPosicion(TpLista &lista, int pos){
	TpLista t=lista, s=NULL;
	int x=1;
	bool flag=false;
	if(pos==1){
	
		eliminarInicio(lista);
		return;
	}
	while(	x!= pos && t->sgte != NULL ){
		s=t;
		t=t->sgte;
		x++;
		if(x==pos)
			flag=true;
	}
	if(flag == false){
		cout<<"Error, Posicion ingresada NO EXISTE.."<<endl;
		
	}else{
		s->sgte=t->sgte;
		delete(t);
		
	}
}


void menu(){
system("CLS");
 cout<<"\n\t LISTA ENLAZADA SIMPLE\n\n";
 cout<<"1.- Insertar al Inicio "<<endl;
 cout<<"2.- Insertar al Final "<<endl;	
 cout<<"3.- Insertar por Posicion "<<endl;	
 cout<<"4.- Mostrar Lista"<<endl;
 cout<<"5.- Eliminar primer Nodo"<<endl;	
 cout<<"6.- Eliminar ultimo Nodo"<<endl;	
 cout<<"7.- Eliminar por Posicion "<<endl;	
 cout<<"8.- Buscar y Reemplazar "<<endl;	
 cout<<"0.- Salir "<<endl<<endl;	
 
 cout<<"Ingresar Opcion--->  "<<endl;
}

//***************************************
int main() {

	int posicion,opc, busca, reemp;
	TpLista lista=NULL;// variable gusrada el inicio de la lista

	do{
		menu();
		cin>>opc;
		switch(opc){
			case 1:{
				if(lista==NULL){
					lista=crearNodo();	
				}
				else{
					insertarInicio(lista);
				}
				
				
				
				system("pause");
				break;
				}
				
			case 2:{
				if(lista==NULL){
					lista=crearNodo();	
				}
				else{
					insertarFinal(lista);
				}
				
				
				system("pause");
				break;
				}
				
			case 3:
			{
				if(lista==NULL){
					cout<<" Lista Vacia, no permite opcion";
					break;
				}
				else{
					cout<<"Ingresar posicion del nodo--> ";cin>>posicion;
					
					insertarPosicion(lista, posicion);
				}
				system("pause");
				break;
				}	
			case 4:{
				
				mostrarLista( lista);
				system("pause");
				break;
				}
			case 5:{
				if(lista==NULL){
					cout<<"Error lista vacia";
					break;	
				}
				else{
					eliminarInicio(lista);
				}
				break;
			}
			case 6:{
				if(lista==NULL){
					cout<<"Error lista vacia";
					break;	
				}
				else{
					eliminarFinal(lista);
				}
				break;
			}	
			case 7:{
				if(lista==NULL){
					cout<<" Lista Vacia, no permite opcion";
					break;
				}
				else{
					cout<<"Ingresar posicion del nodo a eliminar--> ";cin>>posicion;
					
					eliminarPosicion(lista, posicion);
				}

				
				system("pause");
				break;
			}
			case 8:{
				system("pause");
				break;
			}
		}
	
	}while(opc !=0);
	system("pause");
	
	return 0;
}

