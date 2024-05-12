#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

const int TAMANO = 5;

void imprimirArray(const int arr[], int tam) {
    for (int i = 0; i < tam; ++i) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void agregarElemento(int arr[], int& tam, int elemento) {
    for (int i = tam; i > 0; --i) {
        arr[i] = arr[i - 1];
    }
    arr[0] = elemento;
    ++tam;
}

void eliminarElemento(int arr[], int& tam) {
    for (int i = 0; i < tam - 1; ++i) {
        arr[i] = arr[i + 1];
    }
    --tam;
}

void inicializarSemilla() {
    srand(time(NULL));
}

int numeroAleatorio(int min, int max) {
    return min + rand() % (max - min + 1);
}

void actualizarVectorC(const int a[], const int b[], int c[], int tam) {
    for (int i = 0; i < tam; ++i) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    inicializarSemilla();
    
    int a[TAMANO];
    int b[TAMANO];
    int c[TAMANO];
    int tamA = 0;
    int tamB = 0;
    
    for (int i = 0; i < TAMANO; ++i) {
        a[i] = numeroAleatorio(1, 100);
        b[i] = -numeroAleatorio(1, 100);
        ++tamA;
        ++tamB;
    }
    
    actualizarVectorC(a, b, c, TAMANO);
    
    cout << "Array a: ";
    imprimirArray(a, tamA);
    cout << "Array b: ";
    imprimirArray(b, tamB);
    cout << "Array c (suma de a y b): ";
    imprimirArray(c, TAMANO);
    
    int opcion;
    do {
        cout << "\nMenu:\n1. Agregar elemento a\n2. Eliminar elemento a\n3. Agregar elemento b\n4. Eliminar elemento b\n5. Actualizar vector c\n6. Salir\nOpción: ";
        cin >> opcion;
        switch (opcion) {
            case 1:
                int nuevoElementoA;
                cout << "Ingrese el nuevo elemento para a: ";
                cin >> nuevoElementoA;
                agregarElemento(a, tamA, nuevoElementoA);
                break;
            case 2:
                eliminarElemento(a, tamA);
                break;
            case 3:
                int nuevoElementoB;
                cout << "Ingrese el nuevo elemento para b: ";
                cin >> nuevoElementoB;
                agregarElemento(b, tamB, -nuevoElementoB);
                break;
            case 4:
                eliminarElemento(b, tamB);
                break;
            case 5:
                actualizarVectorC(a, b, c, TAMANO);
                cout << "Vector c actualizado.\n";
                break;
            case 6:
                cout << "Saliendo del programa.\n";
                break;
            default:
                cout << "Opción inválida. Por favor, intente de nuevo.\n";
                break;
        }
        
        cout << "Array a: ";
        imprimirArray(a, tamA);
        cout << "Array b: ";
        imprimirArray(b, tamB);
        cout << "Array c (suma de a y b): ";
        imprimirArray(c, TAMANO);
    } while (opcion != 6);
    
    return 0;
}

