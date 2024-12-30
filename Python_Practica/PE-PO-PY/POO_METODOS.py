#Métodos en Python: Instancia, clase y estáticos
class Clase:
    #Puedes acceder y modificar los atributos del objeto
    #Pueden acceder a otros métodos
    def metodo(self):
        return "Método normal",self
    #Reciben como argumento cls, que hace referencia a la clase
    #Acceden a la clase pero no a la instancia
    #Pueden modificar los atributos de la clase
    @classmethod
    def metodoclase(cls):
        return 'Método de clase', cls
    
    #No aceptan argumentos
    #No pueden acceder a la instancia ni a la clase
    @staticmethod
    def metodostatico():
        return "Método estático"