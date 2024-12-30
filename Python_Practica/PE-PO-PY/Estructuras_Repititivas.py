'''
Escribir un programa en el cual se solicite al usuario un número y se imprima la tabla de multiplicar del 1 al 10 del valor introducido.

#Declaracion de variable
numero = 0
#Solicitud de dato
numero = int(input("Digite un numero:"))
#Impresion de la tabla de multiplicar
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
    

#Declaracion de variable
numero = 0
iterador = 1
resultado = 0
#Solicitud de dato
numero = int(input("Digite un numero: "))
#Usando while
while iterador >=1 and iterador <=10:
    resultado = numero * iterador
    print(f"{numero} x {iterador} = {resultado}")
    iterador += 1

'''
'''
Escribir un programa en el cual se solicite al usuario un número y se imprima la tabla de potencias del 1 al 10 del valor introducido.

#Declaración de variables
numero = 0;

#Solicitud de dato
numero = int(input("Digite un numero: "))

#Impresion de la tabla de potencias

for i in range(1, 11):
    print(f"{numero} elevado a la {i} = {numero ** i}")

'''

'''
Escribir un programa que imprima los números pares entre 0 y 200 de forma creciente.

#Declaracion de variables
numeros = 0
#Impresion de los numeros pares
for pares in range(0,201):#(inicio,final,paso)
    if pares % 2 == 0:
        print(pares)
        
'''
'''
Escribir un programa que imprima los números pares de forma creciente hasta un número introducido por el usuario.

#Declaración de variables
numero = 0
iterador = 0
#Solicitud de dato
numero = int(input("Digite un numero: "))
while iterador < numero:
    if iterador % 2 == 0:
        print(iterador)
    iterador += 1
'''
'''
Escribir un programa que imprima todos los números primos hasta un número introducido por el usuario.
#Declaración de variables
numero = 0
iterador = 0
#Solicitud de dato
numero = int(input("Digite un numero: "))

while iterador < numero:
    es_primo = True
    if iterador > 1:
        for i in range(2, iterador):
            if (iterador % i) == 0:
                es_primo = False
                break
    if es_primo:
        print(iterador)
    iterador += 1
'''

'''
#Calculadora
Crea una Matriz 4x4 que almacene los valores de un teclado matricial. 
Imprime la matriz, la cuarta fila y el asterisco (*) en pantalla.

#Declaración de variables
Matriz = []
Fila = 3
Columna = 0
#Creacion de la matriz
Matriz = [ ['1','2','3','A'], ['4', '5','6', 'B'],['7', '8', '9', 'C'],['*', '0', '#', 'D'] ]

#Impresion de la matriz
print(">>> Imprimir Matriz : %s" %(Matriz))
print(">>> Impresión de la 4ta Fila: %s" %((Matriz[Fila])))
print(">>> Imprimir Matriz : %s" %(Matriz[Fila][Columna]))
'''

'''
Crea una matriz 3x3 que almacene los valores del 1 al 9. 
El tamaño de la matriz indica la cantidad de filas. 
Imprime cada fila de la matriz en pantalla.

#Declaración de las variables
Matriz = []
Longitud = 0
#Armado de la matriz
Matriz = [[1,2,3], [4,5,6], [7,8,9]]
Longitud = len(Matriz)
#Impresion de la cantidad de la matriz en pantalla
print(">>> Cantidad de Filas : %s" %(Longitud))
#Impresion de la matriz
print(">>> Matriz : %s" %(Matriz))
#Impresion de cada fila de la matriz
for fila in range (Longitud):
    print(">>> Fila %d : %s" %(fila + 1 , Matriz[fila]))
    
'''

'''
Haz un programa para crear una matriz nula Mmxn, 
donde se le solicite al usuario su dimensión m x n, 
(m son las filas y n son las columnas). Imprime cada fila de la matriz en pantalla.

#Declariación de variables
n = 0#Numero de filas
m = 0#Numero de columnas
Matriz = []
#Solicitud de datos al usuario
n = int(input("Digite el numero de filas: "))
m = int(input("Digite el numero de columnas: "))
#Creación de la matriz
for fila in range(n):
    Matriz.append([0]*m)
#Longitud de la matriz
Longitud = len(Matriz)

print("\n>>> MATRIZ M(%dx%d): %s\n" %(n,m,Matriz))

#Imprimir cada fila de la matriz              
for fila in range(Longitud):
    print(Matriz[fila])

'''
'''


'''