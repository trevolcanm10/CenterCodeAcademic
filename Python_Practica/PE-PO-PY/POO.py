
'''

class Animal:
    #Constructor
    def __init__(self, especie,edad):
        self.especie = especie
        self.edad = edad

    #Método genérico pero con implementación particular    
    def hablar(self):
        #Método vacío
        pass
    
    def moverse(self):
        #Método vacío	
        pass
    
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)
    

#Herencia
class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

class Vaca(Animal):
    def hablar(self):
        print("Muu!")
    def moverse(self):
        print("Caminando con 4 patas")
        
class Abeja(Animal):
    def hablar(self):
        print("Bzzz!")
    def moverse(self):
        print("Volando")
    def picar(self):
        print("Picar!")
        
mi_perro = Perro('mamífero',10)
mi_vaca = Vaca('mamífero',23)
mi_abeja = Abeja('mamífero',1)

mi_perro.describeme()
mi_vaca.describeme()
mi_abeja.describeme()

mi_perro.hablar()
mi_perro.moverse()

mi_vaca.hablar()
mi_vaca.moverse()

mi_abeja.hablar()
mi_abeja.moverse()

'''
'''
class ContadorDePalabras:
    def __init__(self):
        self.contador = 0
    def contar(self,texto):
        palabras = texto.split()
        self.contador += len(palabras)
    def obtener_contador(self):
        return self.contador
    
#Creamos instancia de la clase ContadorDePalabras
contador_palabras = ContadorDePalabras()
#Agregamos palabras al texto
contador_palabras.contar("Hola, mi nombre es Denilson")
contador_palabras.contar("Y estoy aprendiendo Python")
#Obtenemos el contador
print(f"El numero de palabras es : {contador_palabras.obtener_contador()}")

'''
