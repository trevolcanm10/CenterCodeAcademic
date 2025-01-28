import socket#Se usa para crear y gestionar conexiones de red 
import ipaddress#Se usa para crear rangos de direcciones IP
from concurrent.futures import ThreadPoolExecutor#Ejecutamos tareas concurrentes multihilo,lo cual permite realizar escaneos mas rápido
from rich.console import Console#Permiten imprimir textos estilizados con tablas 
from rich.table import Table
from scapy.all import *
import logging

#Desactivamos las salidas para warnings para Scapy
#Configuración para emisión solo de errores
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
#Anadimos una barra de carga o progreso
from tqdm import tqdm
class NetworkAnalyzer:

    def __init__(self,network_range,timeout=1):
        self.network_range = network_range
        self.timeout = timeout

    #Metodo interno 
    def _scan_host_sockets(self,ip,port=1000):
        try:
            #Creamos un socket para el uso de IPV4 , y el protocolo TCP
            with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
                s.settimeout(self.timeout)
                s.connect((ip,port))
                return (ip,True)

        except (socket.timeout,socket.error):
            return(ip,False)
    
    #Rastreando ip de máquinas windons a través de puertos conocidos
    def _scan_host_scapy(self,ip,scan_port = (135,445,139)):
        for port in scan_port:
            packet = IP(dst = ip)/TCP(dport=port,flags='S',window=0X4001,options = [('MSS',1460)])
            response, _ = sr(packet,timeout=self.timeout,verbose=0)
            if response:
                return(ip,True)
        return(ip,False)


    def hosts_scan_arp(self):
        hosts_up = []
        network = ipaddress.ip_network(self.network_range,strict=False)
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=str(network))
        response, _ = tqdm(srp(arp_request,timeout=self.timeout,iface_hint=str(network[1]),verbose=0),desc="Esca")
        for _, recevied in response:
            hosts_up.append(recevied.psrc)
        return hosts_up
    #Utilizamos ipaddress para pasar el rango de busqueda que deseo dentro de la funcion
    def hosts_scan(self,scan_port = (135,445,139)):
        network = ipaddress.ip_network(self.network_range,strict=False)
        #Programación multihilo para aumentar la velocidad del escaneo 
        #Listas
        hosts_up = []
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(self._scan_host_scapy,str(host),scan_port): host for host in tqdm(network.hosts(), desc="Escaneando hosts")}
            for future in tqdm(futures,desc="Obteniendo resultados"):
                if future.result()[1]:
                    hosts_up.append(future.result()[0])
        return hosts_up

    
    def pretty_print(self,data,data_type="hosts"):
        console = Console()
        table = Table(show_header=True,header_style="bold magenta")

        if data_type =="hosts":
            table.add_column("Hosts up", style="bold green")
            for host in data:
                table.add_row(host,end_section=True)
        
        console.print(table)



