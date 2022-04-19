from flask import Flask, request

#creamos objeto de la clase Flask
app = Flask(__name__)

# creamos mi primera ruta
@app.route('/')
def index():
    return '<center><h1>HOLA MUNDO FLASK</center></h1>'

@app.route('/saludo')
def saludo():
    nombre = request.args.get('nombre','no hay nombre')
    return '<center><h1>Hola {} </center></h1>'.format(nombre)
# http://127.0.0.1:5000/saludo?nombre=karen

@app.route('/suma')
def suma():
    n1 = request.args.get('n1', '0')
    n2 = request.args.get('n2', '0')
    resultado = int(n1) + int(n2)
    return '<center><b>La suma de {} + {} es {} </center></b>'.format(n1,n2,resultado)
# http://127.0.0.1:5000/suma?n1=3&n2=5

@app.route('/resta/<int:n1>/<int:n2>')
def resta(n1=0,n2=0):
    resultado = int(n1) - int(n2)
    return '<center><b>La resta de {} - {} es {} </center></b>'.format(n1,n2,resultado)
# http://127.0.0.1:5000/resta/20/5

# desplegamos nuestra app web
# app.run()
app.run(debug = True) # desplega la aplicación en modo desarrollo, si se hace un cambio automáticamente se reflejan los cambios
