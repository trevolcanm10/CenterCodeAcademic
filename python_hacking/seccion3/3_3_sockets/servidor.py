import socket#Modulo para trabajar con conexiones de red

#Creamos un servidor socket de tipo TCP
#Parametro 1 --> Uso de IPV4 como protocolo de red 
#Pametro 2 --> Uso del protocolo TCP

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Asignamos al socket una direccion local y un puerto
servidor.bind(('localhost',12345))

#Inicio de escucha de conexiones
servidor.listen()

print("Esperando conexiones...")


#Acepta una conexion 

conexion , direccion = servidor.accept()


with conexion:
    print("Conectado a:",direccion)
    while True:
        #Recibe datos hasta 1024 bytes
        datos = conexion.recv(1024)
        if not datos:
            break
        print("Datos recibidos del cliente: ", datos.decode())
        #Convierte el mensaje en binario , por que es lo que manejan los sockets
        mensaje = "Hola cliente.".encode()
        #Envia el mensaje de respuesta
        conexion.sendall(mensaje)

conexion.close()