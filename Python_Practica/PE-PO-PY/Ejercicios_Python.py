'''
Escribir un programa que muestre por pantalla el siguiente mensaje:

La felicidad se puede encontrar hasta en los más oscuros 
momentos, si somos capaces de usar bien la luz.
— Albus Dumbledore

'''
#print("La felicidad se puede encontrar hasta en los más oscuros momentos")
#print("Si somos capaces de usar bien la luz")
#print("Albus Dumbledore")

#print('''La felicidad se puede encontrar hasta en los más oscuros 
#momentos, si somos capaces de usar bien la luz
#— Albus Dumbledore''')


'''
Escribir un programa que almacene la cadena ¡Hola Mundo! en una  variable
y luego muestre por pantalla el contenido de la variable
cadena_texto = "¡Hola mundo!"
print(cadena_texto)
'''

'''
Escribir un programa que pregunte el nombre y apellido del usuario. 
Luego de ser introducidos los datos muestre por pantalla la cadena ¡Hola {nombre} {apellido}, 
gusto en conocerte!, donde:

nombre = input("Introduce su nombre:")
apellido = input("Introduce su apellido:")
print(f"¡Hola {nombre} {apellido}, gusto en conocerte!")
'''

'''
Escribir un programa que lea un entero positivo, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1. 
La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:

suma = n * (n + 1) / 2 

num =int(input("Digite un numero: "))
suma = num * (num + 1) / 2
print(f'La suma de 1 hasta {num} es: {suma}')
'''

'''
#Programa que solicite al usuario los datos para calcular el área de un Cuadrado (■), finalmente mostrar el resultado en pantalla.
#Area = Lado ** 2
lado = int(input("Digite el lado del cuadrado: "))
area = lado ** 2 
# Mostrará el área del cuadrado
print(f"El área del cuadrado es: {area}")
'''

'''
Programa que solicite al usuario los datos para calcular el área de un Triángulo (▲), 
finalmente mostrar el resultado en pantalla.
Area = (Base * Altura)/2
base = int(input("Digite la base del triángulo: "))
altura = int(input("Digite la altura del triángulo: "))
area = (base * altura) / 2
# Mostrará el área del triángulo
print(f"El área del triángulo es: {area}")
'''

'''
Programa que solicite al usuario los datos para calcular el área de un Círculo (●), finalmente mostrar el resultado en pantalla.
Área del círculo
Area = PI*(Radio**2)
radio = float(input("Digite la radio del círculo: "))
# Importar el valor de PI
PI = 3.1416
area = PI*(radio**2)
print(f'El area del circulo es: {area}')
'''

'''
Un radar común de detección de velocidad de la policía de caminos emite un rayo de microondas a una frecuencia f0. El rayo es reflejado por un automóvil que se aproxima y el rayo reflejado es captado y analizado por la unidad de radar. La frecuencia del rayo reflejado es cambiada ligeramente de f0 a f1 debido al movimiento del automóvil.

La relación entre la velocidad del automóvil, v, en millas por hora, y las dos frecuencias de microondas es:


Donde las ondas emitidas tienen una frecuencia de:

f0 = 2 x10^10 sec ^–1

Usando la fórmula dada, escriba un programa para calcular y desplegar la velocidad correspondiente a una frecuencia recibida de 2.0000004 x 10^10 sec–1.

Ahora aplicamos el procedimiento de desarrollo de software a este problema.

___

► Variables:

· Velocidad : Velocidad del Vehículo.

· Frecuencia0: Frecuencia inicial.

· Frecuencia1: Frecuencia Final.

___


ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""

MENSAJE_INICIAL = "RADAR DE VELOCIDAD"

Velocidad = 0.0
Frecuencia0 = 2e-10
Frecuencia1 = 2.0000004e-10

Formato_Respuesta = ">>> La Velocidad es: %0.2f millas/hora."

print(CADENA_VACIA.center(ANCHO,RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO,RELLENO2))
Velocidad = 6.685e8*(Frecuencia1-Frecuencia0)/(Frecuencia1+Frecuencia0)
print(CADENA_VACIA.center(ANCHO,RELLENO1))
print(Formato_Respuesta.center(ANCHO,RELLENO2) %(Velocidad))
print(CADENA_VACIA.center(ANCHO,RELLENO1))

'''

'''
Velocidad = 0.0
Frecuencia0=2e-10
Frecuencia1=2.0000004e-10
Velocidad = 6.685e8*(Frecuencia1-Frecuencia0)/(Frecuencia1+Frecuencia0)
print("-----------------------------------------------")
print("                RADAR DE VELOCIDAD           ")
print("----------------------------------------------")
print(f"La Velocidad es : {Velocidad} millas/hora")
print("----------------------------------------------")
'''

'''
► Enunciado:

Un Freelancer desea saber cuánto puede cobrar por su trabajo semanal y mensualmente, para ello solo necesita establecer el precio de su trabajo por hora.

Se estiman 40 horas de trabajo a la semana.

Las Fórmulas para calcular el pago Semanal y Mensual son:

1) Pago_Semanal = (DolaresPorHora x 40)

2) Pago_Mensual = (DolaresPorHora x 160)

___

► Variables:

Dolares_Por_Hora: Cantidad de Dólares que gana el Freelancer por hora.

Pago_Semanal: Almacena el resultado del pago semanal.

Pago_Mensual: Almacena el resultado del pago mensual.

___

'''

ANCHO = 40
RELLENO1 = "-"
RELLENO2 = " "
CADENA_VACIA = ""

MENSAJE_INICIAL = "CALCULADORA FREELANCER (USD)"
Dolares_Por_Hora = float(input('Digite el pago por hora que deseas recibir: '))
MENSAJE_INTERMEDIO = f"Precio en dolares por Hora: {Dolares_Por_Hora}"
Pago_Semanal = (Dolares_Por_Hora * 40)
Pago_Mensual = (Dolares_Por_Hora * 160)
Formato_Respuesta = f">>> PAGO SEMANAL: {Pago_Semanal:.2f} \n>>> PAGO MENSUAL: {Pago_Mensual:.2f}"
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(MENSAJE_INICIAL.center(ANCHO, RELLENO2))
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(MENSAJE_INTERMEDIO.center(ANCHO,RELLENO2))
print(CADENA_VACIA.center(ANCHO, RELLENO1))
print(Formato_Respuesta.center(ANCHO, RELLENO2))
print(CADENA_VACIA.center(ANCHO, RELLENO1))


