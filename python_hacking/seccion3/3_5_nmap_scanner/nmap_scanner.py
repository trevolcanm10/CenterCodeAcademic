import nmap #Librería de python que nos permite usar funcionalidades con Nmap
from openai import OpenAI #Se usa para conectar a la API de Openai
from dotenv import load_dotenv # Se usa para cargar las variables de entorno

def host_scan(network):
    #Creación de un objeto PortScanner
    nm = nmap.PortScanner()
    #Verificación si los hosts están activos
    nm.scan(hosts=network,arguments='-sn')
    active_hosts = [host for host in nm.all_hosts() if nm[host].state()=='up']
    #Retorna una lista de direcciones IP de los hosts activos
    return active_hosts


def services_scan(network):
    nm = nmap.PortScanner()
    #SV detección de servicios por Nmap
    nm.scan(hosts=network,arguments='-sV')
    network_data = {}
    #Hosts activos e inactivos
    for host in nm.all_hosts():
        if nm[host].state() =='up':
            network_data[host]={}
            for proto in nm[host].all_protocols():
                network_data[host][proto]={}
                ports = nm[host][proto].keys()
                for port in ports:
                    service = nm[host][proto][port]['name']
                    version = nm[host][proto][port]['product'] + " " + nm[host][proto][port]['version']
                    network_data[host][proto][port] = {'service':service, 'version': version}
    return network_data

def priorizar_hosts(network_data):
    load_dotenv()
    client = OpenAI()

    chat_completion = client.chat.completions.create(

        messages = [
            {
                "role": "system", "content":"Eres un experto en Ciberseguridad y en gestion de priorizacion de vulnerabilidades."},
            {
                "role": "user", "content":f"Teniendo en cuenta el siguiente descubrimiento de hosts,puertos y servicios , ordena los hosts de mas vulnerable a menos vulnerable y propon los siguientes pasos para la fase de explotacion en un ejercicio de hacking ético.\n\n {network_data}"
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

if __name__=="__main__":
    network_data = services_scan('192.168.126.0/24')
    print(priorizar_hosts(network_data))

