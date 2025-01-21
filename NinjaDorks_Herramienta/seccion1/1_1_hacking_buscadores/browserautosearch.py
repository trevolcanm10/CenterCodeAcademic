from selenium import webdriver #Automatizar navegadores web 
from selenium.webdriver.firefox.service import Service as FirefoxService#Configura el servicio del controlador de firefox
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager#Gestor automático del navegador
from webdriver_manager.chrome import ChromeDriverManager#Gestor automático del navegador
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait#Espera dinámicamente a que una condición se cumpla 
from selenium.webdriver.common.keys import Keys#Sirve para simular pulsaciones con el teclado
import time



class BrowserAutoSearch:
    def __init__(self):
        self.browser = self._initialize_browser()
    
    def _initialize_browser(self):
        browsers={

            "firefox":{
                "manager":GeckoDriverManager,
                #Instalamos el controlador
                "service": FirefoxService,
                #Personalización de las opciones para el navegador
                "options":webdriver.FirefoxOptions(),
                "driver": webdriver.Firefox
            },

            "chrome":{
                "manager":ChromeDriverManager,
                "service":ChromeService,
                "options":webdriver.ChromeOptions(),
                "driver":webdriver.Chrome
            }
        }
        #Inicializamos los navegadores
        for browser_name , browser_info in browsers.items():
            try:
                return browser_info["driver"](service=browser_info["service"](browser_info["manager"]().install()),
                                              options=browser_info["options"])
            except Exception as e:
                print(f"Error al iniciar el navegador {browser_name}: {e}")
        #Lanzamiento de excepciones personalizadas
        raise Exception("No se pudo inicializar ningún navegador.Por favor, instala Firefox o Chrome.")
    def accept_cookies(self, button_selector):
        """Acepta el anuncio de cookies de un buscador."""
        try:
            accept_button = WebDriverWait(self.browser,10).until(
                EC.element_to_be_clickable((By.ID, button_selector)))
            accept_button.click()

        except Exception as e:
            print("Error al encontrar o hacer click en el botón de aceptar cookies", e)
    
    def search_google(self,query):
        "Realiza una búsqueda en google"
        #Abre google
        self.browser.get("http://www.google.com")
        self.accept_cookies(button_selector='L2AGLb')
        #Encuentra el cuadro de búsqueda y envia la cadena de texto
        search_box = self.browser.find_element(By.NAME, 'q')
        search_box.send_keys(query + Keys.ENTER)
        #Esperamos a que la página cargue los resultados
        time.sleep(5)

    def google_search_results(self):
        """Extrae los resultados de una consulta en google"""
        #Extraemos los enlaces y descripciones de los primeros resultados
        results = self.browser.find_elements(By.CSS_SELECTOR, 'div.g')
        custom_results = []

        for result in results:
            try:
                cresult = {}
                cresult["title"] = result.find_element(By.CSS_SELECTOR,'h3').text
                cresult["link"] = result.find_element(By.TAG_NAME,'a').get_attribute('href')
                cresult["description"] = result.find_element(By.CSS_SELECTOR,'div.VwiC3b').text
                custom_results.append(cresult)
            except Exception as e:
                print("Un elemento no pudo ser extraído:",e)
                continue
        return custom_results
    
    def quit(self):
        self.browser.quit()

#Inicializamos el webdriver de GoogleChrome
#service = Service(ChromeDriverManager().install())#Instalamos el controlador
#options = webdriver.ChromeOptions()#Personalización de las opciones para el navegador
#browser = webdriver.Chrome(service=service,options=options)#Lanzamiento del navegador

