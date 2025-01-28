import socket
#Creamos un cliente socket de tipo TCP
#Parametro 1 --> Uso de IPV4 como protocolo de red 
#Pametro 2 --> Uso del protocolo TCP

cliente = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cliente.connect(('localhost',12345))

try:
    while True:
        datos = input("Introduce los datos para enviar: ")
        cliente.sendall(datos.encode())
    #Enviamos datos
    #mensaje = "Hola servidor".encode()
    #cliente.sendall(mensaje)

    #Recibimos los datos del servidor,cantidad de datos 1024 bytes
    #respuesta = cliente.recv(1024)
    #print("Respuesta del servidor:",respuesta.decode())

except KeyboardInterrupt:
    cliente.close()
