
from flask import Flask, request,render_template

app = Flask(__name__)#Creamos la aplicación route

'''
from flask import Flask

app = Flask(__name__)#Creamos la aplicación route

#Creando rutas
@app.route('/')
def saludo():
    return 'Hola mundo, estoy aprendiendo a usar flask'

@app.route('/about')
def about():
    return 'Acá estamos aprendiendo sobre Flask'

@app.route('/cursos')
def cursos():
    return 'Estamos en la sección de cursos'

if __name__ == '__main__':
    app.run(debug=True)
'''

'''
#Creando rutas
@app.route("/get_ejemplo")
def get_ejemplo():
    return "Esto es un ejemplo de una ruta GET"

@app.route("/post_ejemplo", methods=["POST"])
def post_ejemplo():
    return "Esto es un ejemplo de una ruta POST"


'''

'''
@app.route("/saludar")
def saludo():
    nombres_lista = ["Neymar", "Denilson" , "Ashley"]
    return render_template("index.html", nombres=nombres_lista)
'''
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def acerca_de():
    return render_template("about.html")

@app.route("/saludar")
def saludar():
    return render_template("formulario.html")
@app.route("/submit", methods=["POST"])
def submit():
    nombre = request.form['namef']
    return f"Hola, {nombre}"
if __name__ == '__main__':
    app.run(debug=True)