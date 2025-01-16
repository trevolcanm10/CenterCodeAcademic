from gpt4all import GPT4All
from openai import OpenAI

class OpenAIGenerator:
    
    #Constructor con parametro del modelo GPT
    def __init__(self,model_name='gpt-4o'):
        #Atributos de instancia 
        self.model_name = model_name
        self.client = OpenAI()

    #Funcion donde le pasamos el prompt
    def generate(self,prompt):
        #Documentacion de la api de GPT
        completion = self.client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
        )   
        return completion.choices[0].message.content

            

#Clase que contiene tanto la IA local como la AI con API de GPT
class IAAgent:

    #Constructor que contiene el parametro del generador
    def __init__(self,generator):
        self.generator = generator
        

    def generate_gdork(self,description):
        #Prompt
        prompt = self._build_prompt(description)
        try:
            output = self.generator.generate(prompt)
            return output
        
        except Exception as e:
            print(f"Error al generar el Google Dork: {e}")
            return None
                  

    #Creamos métodos de acceso interno
    def _build_prompt(self,description):
        return f"""
        Genera un Google Dork específico basado en la descripción del usuario. Un Google Dork utiliza operadores avanzados en motores de búsqueda para encontrar información específica que es difícil de encontrar mediante una búsqueda normal. Tu tarea es convertir la descripción del usuario en un Google Dork preciso. A continuación, se presentan algunos ejemplos de cómo deberías formular los Google Dorks basándote en diferentes descripciones:

        Descripción: Documentos PDF relacionados con la seguridad informática publicados en el último año.
        Google Dork: filetype:pdf "seguridad informática" after:2023-01-01

        Descripción: Presentaciones de Powerpoint sobre cambio climático disponibles en sitios .edu.
        Google Dork: site:.edu filetype:ppt "cambio climático"

        Descripción: Listas de correos electrónicos en archivos de texto dentro de dominios gubernamentales.
        Google Dork: site:.gov filetype:txt "email" | "correo electrónico"

        Ahora, basado en la siguiente descripción proporcionada por el usuario, genera el Google Dork correspondiente:

        Descripción:{description}
        """




