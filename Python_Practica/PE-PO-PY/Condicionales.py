'''
Escribir un programa que solicite al usuario un número entero y muestre en pantalla si el número es Positivo (+) o Negativo (-). 
En caso de que el número sea igual a cero (0) se debe mostrar en pantalla: 
El número no es Positivo ni Negativo.

#Declaración de variables
num_entero = 0.0

#Solicitud de datos al usuario
num_entero = float(input("Digite un numero: "))

if num_entero > 0:
    print(f"El numero {num_entero} es Positivo")
elif num_entero < 0:
    print(f"El numero {num_entero} es Negativo")
else:
    print(f"El numero {num_entero} no es Positivo ni Negativo")
    
'''
'''
Escribir un Programa que solicite al usuario la edad de 2 personas, y diga cuál es mayor. Ejemplo:

- La Primera persona es mayor!

Si la edad de ambos es igual se muestra el siguiente mensaje:

- Ambos tienen la misma edad!

'''

'''
#Declaración de variables
edad_primera_persona = 0.0
edad_segunda_persona = 0.0

#Solicitud de datos al usuario
edad_primera_persona = int(input('Digite la edad de la primera persona: '))
edad_segunda_persona = int(input('Digite la edad de la segunda persona: '))

if edad_primera_persona > edad_segunda_persona:
    print('La Primera persona es mayor!')
elif edad_segunda_persona > edad_primera_persona:
    print('La Segunda persona es mayor!')
else:
    print('Ambos tienen la misma edad!')
'''

'''
► Enunciado:
Introducir un número por teclado y que se muestre un mensaje indicando si es par o impar.

#Declaración de variables
numero_ingresado = int(input('Digite un numero: '))

if numero_ingresado % 2 == 0:
    print('El numero es par')
elif numero_ingresado == 0:
    print('El numero es cero')
else:
    print('El numero es impar')
    
'''
'''
Introducir un número por teclado y que se muestre un mensaje indicando si es múltiplo de 3.
#Declaración de variables
numero_ingresado = int(input('Digite un numero: '))
if numero_ingresado % 3 == 0:
    print('El numero es multiplo de 3')
else:
    print('El numero no es multiplo de 3')
'''
'''
Escribir un programa que solicite al usuario una letra y diga si esta es MAYÚSCULA o minúscula.

#Declaración de variables 
letra = ' '
#Solicitud de datos al usuario
letra = input('Digite una letra: ')

if letra >= 'a' and letra <='z': # a-z (97-122)
    print(f'{letra} es una letra minúscula')
elif letra >='A' and letra <='Z':# A-Z (65-90)
    print(f'{letra} es una letra mayúscula')
else:
    print(f'{letra} no es una letra')
    
'''
'''
Escribir un programa que solicite al usuario 3 números, compararlos y decir cual es mayor.

#Declaración de variables
num1 = 0.0
num2 = 0.0
num3 = 0.0

#Solicitud de datos al usuario

num1 = float(input('Digite el primer numero: '))
num2 = float(input('Digite el segundo numero: '))
num3 = float(input('Digite el tercer numero: '))

if num1 > num2 and num1 > num3:
    print(f'El número {num1} es el mayor')

elif num2 > num1 and num2 > num3:
    print(f'El número {num2} es el mayor')
else:
    print(f'El número {num3} es el mayor')

___________________________________________

#Declaraciónde variables
num1 = 0.0
num2 = 0.0
num3 = 0.0
#Solicitud de datos al usuario

num1 = float(input('Digite el primer numero: '))
num2 = float(input('Digite el segundo numero: '))
num3 = float(input('Digite el tercer numero: '))

if num1 > num2 :
    if num1 > num3:
        maximo = num1
    else:
        maximo = num3
        
else:
    if num2 > num3:
        maximo = num2
    else:
        maximo = num3

print('>>> El numero maximo es: %5.2f' %(maximo))
'''

'''
Escribir un programa que solicite al usuario 5 números, compararlos y decir cual es mayor.

#Declaracion de variables
num1 = 0.0
num2 = 0.0
num3 = 0.0
num4 = 0.0
num5 = 0.0

#Solicitud de datos al usuario

num1 = float(input('Digite el primer numero: '))
num2 = float(input('Digite el segundo numero: '))
num3 = float(input('Digite el tercer numero: '))
num4 = float(input('Digite el cuarto numero: '))
num5 = float(input('Digite el quinto numero: '))

posible_maximo = num1

if(num2 > posible_maximo):
    posible_maximo = num2

if(num3 > posible_maximo):
    posible_maximo = num3

if(num4 > posible_maximo):
    posible_maximo = num4

if(num5 > posible_maximo):
    posible_maximo = num5
    
maximo = posible_maximo

print(f'El numero mayor es: {maximo}')


'''
'''
Escribir un programa en el cual Dados 5 números enteros solicitados al usuario, determinar cuál de los 4 números enteros es más cercano al primero.

#Declaración de variables
num1 = 0.0
num2 = 0.0
num3 = 0.0
num4 = 0.0
num5 = 0.0

Resta1 = 0.0
Resta2 = 0.0
Resta3 = 0.0
Resta4 = 0.0



#Solicitud de datos al usuario  
num1 = int(input('Digite el primer numero: '))
num2 = int(input('Digite el segundo numero: '))
num3 = int(input('Digite el tercer numero: '))
num4 = int(input('Digite el cuarto numero: '))
num5 = int(input('Digite el quinto numero: '))

#Hallamos la menor diferencia
Resta1= num1 - num2
Resta2= num1 - num3
Resta3= num1 - num4
Resta4= num1 - num5

#Menor diferencia
menor_diferencia = Resta1

if Resta2 < menor_diferencia and Resta2 >= 0:
    menor_diferencia = Resta2
else:
    if Resta2 > menor_diferencia and Resta2 <=0:
        menor_diferencia = Resta2

if Resta3 < menor_diferencia and Resta3 >= 0:
    menor_diferencia = Resta3
else:
    if Resta3 > menor_diferencia and Resta3 <=0:
        menor_diferencia = Resta3
        
if Resta4 < menor_diferencia and Resta4 >= 0:
    menor_diferencia = Resta4
else:
    if Resta4 > menor_diferencia and Resta4 <=0:
        menor_diferencia = Resta4

#Determinamos el número más cercano al primero
numero_cercano = num1-menor_diferencia

print(f'El numero más cercano al primero es: {numero_cercano}')

► Enunciado:

Crear un Algoritmo que permita hallar la solución a una ecuación de primer grado, de la forma: ax + b = 0

El objetivo es despejar la x y validar los posibles datos para arrojar la respuesta.

Al despejar la x tendremos que:

x = -b/a

Por lo tanto tendremos los siguientes escenarios:

1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.

2) Si a es IGUAL a 0 (a == 0) tendremos que:

Si b es DIFERENTE de 0 (b != 0) la ecuación no tiene solución.

Si b es IGUAL a 0 (b == 0) la ecuación tiene Infinitas Soluciones.

___

► Variables:

a: Coeficiente principal.

b: Término Independiente.

x: Incógnita.

___

'''
'''
► Enunciado:

Crear un Algoritmo que permita hallar la solución a una ecuación de primer grado, de la forma: ax + b = 0

El objetivo es despejar la x y validar los posibles datos para arrojar la respuesta.

Al despejar la x tendremos que:

x = -b/a

Por lo tanto tendremos los siguientes escenarios:

1) Si a es DIFERENTE de 0 (a != 0) la ecuación tiene solución.

2) Si a es IGUAL a 0 (a == 0) tendremos que:

Si b es DIFERENTE de 0 (b != 0) la ecuación no tiene solución.

Si b es IGUAL a 0 (b == 0) la ecuación tiene Infinitas Soluciones.

___

► Variables:

a: Coeficiente principal.

b: Término Independiente.

x: Incógnita.

___

#Declaración de variables
coeficiente_principal = 0.0
termino_independiente = 0.0
variable_x = 0.0 

ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""

#Solicitud de datos al usuario
coeficiente_principal = float(input('Digite el coeficiente principal (a): '))
termino_independiente = float(input('Digite el termino independiente (b): '))

MENSAJE_INICIAL = "ECUACION DE PRIMER GRADO: ax + b = 0"
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO, RELLENO2))
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(f">>> Valor de a: {coeficiente_principal}")
print(f">>> Valor de b: {termino_independiente}")
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(f"ECUACION: {coeficiente_principal} * X + {termino_independiente} = 0" )
print(CADENA_VACIA.center(ANCHO, RELLENO1))
if coeficiente_principal != 0:
    print('La ecuacion tiene solucion.')
    variable_x = -termino_independiente / coeficiente_principal
    print(f'>>> SOLUCION: x = {variable_x}')
if coeficiente_principal == 0:
    if termino_independiente != 0:
        print('La ecuacion no tiene solucion.')
    else:
        print('La ecuacion tiene infinitas soluciones.')
print(CADENA_VACIA.center(ANCHO, RELLENO1))

'''
#Importación de librerías
from math import sqrt
#Declaración de variantes
a = 0#coeficiente_principal
b = 0#coeficiente_secundario
c = 0#termino_independiente
discriminante = 0
x1 = 0.0
x2 = 0.0

ANCHO = 55
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""
#Solicitud de datos al usuario
a = float(input('Digite el coeficiente de x² (a): '))
b = float(input('Digite el coeficiente de x (b): '))
c = float(input('Digite el termino independiente (c): '))
discriminante = b**2 - 4*a*c
MENSAJE_INICIAL = "ECUACION DE SEGUNDO GRADO: ax² + bx + c = 0"
#Encabezado del Programa
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO, RELLENO2))
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(f">>> El valor de a: {a}")
print(f">>> El valor de b : {b}")
print(f">>> El valor de c : {c}")

try:
    x1 = (-b + sqrt(discriminante)) / (2 * a)
    x2 = (-b - sqrt(discriminante)) / (2 * a)
    
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    
    if x1 == x2:
        print(">>> SOLUCION: x = %4.2f" % x1)
    else:
        print(">>> SOLUCIONES: x1 = %4.2f y x2 = %4.2f" % (x1, x2))
except ZeroDivisionError:
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    if c != 0:
        print('La ecuacion no tiene solucion')
    else:
        print('La ecuacion tiene infinitas soluciones')
        
except ValueError:
    # Casos:
    # 1) Se produce una division por cero.
    # 2) Se produce por calcular la raız cuadrada de un discriminante
    # negativo.
    print(CADENA_VACIA.center(ANCHO,RELLENO1))
    print('No hay soluciones reales')
        

print(CADENA_VACIA.center(ANCHO,RELLENO1))
