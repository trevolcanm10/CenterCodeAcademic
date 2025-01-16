from dotenv import load_dotenv,set_key
import os #Interactua con el SO
from googlesearch import GoogleSearch #Accedo al archivo googlesearch e accedo a GoogleSearch
from results_parser import ResultsParser
from file_downloader import FileDownloader
from ai_agent import OpenAIGenerator,IAAgent
import argparse
#Cargamos las variables en el entorno
import sys

def env_config():
    """Configurar el archivo .env con los valores proporcionados"""
    #Solicitamos la clave de la API de Goole y también su identificador
    api_key = input("Introduce tu API KEY de Google: ")
    engine_id = input("Introduce el ID del buscador personalizado de Google: ")
    #Crea o modifica los valores del archivo .env de acuerdo a los datos que ingresa el usuario
    set_key(".env","API_KEY_GOOGLE", api_key)
    set_key(".env","SEARCH_ENGINE_ID",engine_id)


def openai_config():
    """Configura la API KEY de OpenAI en el fichero .env ."""
    api_key = input("Introduce la API KEY de OpenAI:")
    set_key(".env","OPENAI_API_KEY",api_key)

def main(query,configure_env,start_page,pages,lang,output_json,output_html,download,gen_dork):
    #Comprobamos si existe el fichero .envç
    env_exists = os.path.exists(".env")#Retorna un valor bool por que comprueba la existencia del archivo .env

    if not env_exists or configure_env:
        #Llamamos a la funcion de configuración de nuestro archivo
        env_config()
        print("Archivo .env configurado satisfactoriamente.")
        sys.exit(1)

    #Cargamos la variable de nuestro entorno    
    load_dotenv()
    #Leemos la clave API(max. 100 peticiones/dia) y el ID del buscador
    API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")
    SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

    if gen_dork:
        #Preguntamos al usario si desea utilizar Open AI
        respuesta = ""
        while respuesta.lower() not in ("y","yes","no","n"):
            respuesta = input("Quieres utilizar gpt-4 de OpenAI (yes/no)?: ")
        
        if respuesta.lower() in ("y","yes"):
            #Comprobamos si esta definida la API KEY de OpenAI en el fiche .env
            if not "OPENAI_API_KEY" in os.environ:
                openai_config()
                load_dotenv()
            #Generacion del dork
            open_ai_generator = OpenAIGenerator()
            ia_agent = IAAgent(open_ai_generator)
        else:
            print("El modelo GPT4All está en desarrollo \n")
        
        respuesta =ia_agent.generate_gdork(gen_dork)
        print(f"\nRespuesta:\n{respuesta}")
        sys.exit(1)

    if not query:
        print("Indica una consulta con el comando -q.Utiliza el comando -h para mostrar la ayuda.")
        sys.exit(1)

    #Creamos un objeto
    gseach = GoogleSearch(API_KEY_GOOGLE,SEARCH_ENGINE_ID)

    resultados=gseach.search(query,
                             start_page=start_page,
                             pages=pages,
                             lang=lang)
    
    #Instacia de la clase ResultsParser
    rparser = ResultsParser(resultados)

    #Mostrar los resultados en linea de consola de comandos
    rparser.mostrar_pantalla()

    if output_html:
        rparser.exportar_html(output_html)
    if output_json:
        rparser.exportar_json(output_json)
    if download:
        #Verificar si estamos pasando 'all' para descargar todo los archivos
        if download == "all":
            file_types = ["all"] #Descargar todo los archivos
        else:
            #Se pasa la lista de tipos de archivos por comas 
            file_types = download.split(",") 
        #Nos quedamos unicamente con las urls de los resultados obtenidos
        urls = [resultado['link'] for resultado in resultados]
        #Instancimos nuestra clase FileDownloader
        fdownloader = FileDownloader("Descargas")
        fdownloader.filtrar_descargar_archivos(urls,file_types)

if __name__ == "__main__":
    #Configuración de los argumentos del programa
    parser = argparse.ArgumentParser(description="Esta herramienta permite realizar Hacking con buscadores de manera automática")
    parser.add_argument("-q","--query",type=str,
                        help="Especifica el dork que desea buscar.\nEjemplo: -q 'Denilson Morales Mallqui' ")
    parser.add_argument("-c","--configure",action="store_true",
                        help="Inicia el proceso de configuracion del archivo .env.\nUtiliza esta opcion sin otros argumentos para configurar las claves.")
    parser.add_argument("--start-page",type=int,default=1,
                        help="Define la pagina de inicio del buscador para obtener los resultados.")
    parser.add_argument("--pages",type=int,default=1,
                        help="El numero de páginas de resultados de búsqueda.")
    parser.add_argument("--lang",type=str,default="lang_es",
                        help="Codigo de idioma para los resultados de busqueda.Por defecto es 'lang_es' (espanol)")
    parser.add_argument("--json", type=str,
                        help="Exporta los resultados en formato JSON en el fichero especificado.")
    parser.add_argument("--html",type=str,
                        help="Exporta los resultados a formato HTML en el fichero especificado.")
    parser.add_argument("--download", type=str,default="None",
                        help="Especifica las extensiones de los archivos que quieres descargar separadas entre coma.Ej: --download 'pdf,doc,sql' ")
    parser.add_argument("-g","--generate-dork",type=str,help="Genera un dork a partir de una descripcion proporcionada por el usuario. \nEj: --generate-dork 'Lista de usuarios y passwords  en ficheros de texto.")

    args = parser.parse_args()#Contiene todo los argumentos parseados
    
    main(query=args.query,
         configure_env=args.configure,
         pages=args.pages,
         start_page=args.start_page,
         lang=args.lang,
         output_html=args.html,
         output_json=args.json,
         download=args.download,
         gen_dork=args.generate_dork)