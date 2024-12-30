#POO

'''
class Persona:
    #Constructor
    def __init__(self, nombre, apellido, edad):
        print(f"Creando persona {nombre}, {apellido}, {edad}")
        
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años")
    def cantar(self,cancion):
        print(f"Estoy cantando la canción: {cancion}")
            
mi_persona = Persona("Denilson","Morales","25")
print(mi_persona)
mi_persona.saludar()
mi_persona.cantar("Despacito")
'''


''' 

class Perro:
    #Atributos
    especie = 'mamífero'
    def __init__(self,nombre,raza,edad):
        print(f"Creando perro {nombre}, {raza}, {edad}")
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    
    def ladra(self):
        print("Guau")
    def camina(self,pasos):
        print(f"Caminando {pasos} pasos")
        
mi_perro = Perro("Buddy","Golden Retriever","7")
print(mi_perro.nombre)
print(mi_perro.raza)
mi_perro.ladra()
mi_perro.camina(10)

'''


class Carro:
    def __init__(self, marca, modelo, año):
        print(f"Creando carro {marca}, {modelo}, {año}")
        self.marca = marca
        self.modelo = modelo
        self.año = año
        
    def arrancar(self):
        print("El carro arranca")
    def acelerar(self, velocidad):
        print(f"El carro acelera a {velocidad} km/h")
    def frenar(self, velocidad):
        print(f"El carro frena a {velocidad} km/h")
        
mi_carro = Carro("Toyota","Corolla","2020")
print(mi_carro.marca)
print(mi_carro.modelo)
print(mi_carro.año)
mi_carro.arrancar()
mi_carro.acelerar(120)
mi_carro.frenar(60)
