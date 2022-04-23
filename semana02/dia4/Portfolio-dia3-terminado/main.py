from pydoc import doc
from flask import Flask,render_template,request,session

## para conectarse a firebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

### para conectarse a firestore
from firebase_admin import firestore
db = firestore.client()
app = Flask(__name__)

#creamos una clave secreta para las variables de sesión
app.secret_key = 'qwerty123456'

@app.route('/')
def index():
    # Accediendo a la base de datos biografia en firestore
    colBiografia = db.collection('biografia')
    docBiografia = colBiografia.get()
    for doc in docBiografia:
        dicBiografia = doc.to_dict()
    
    # Accediendo a la base de datos enlaces en firestore
    colEnlaces = db.collection('enlaces')
    docEnlaces = colEnlaces.get()
    lstEnlaces = []
    for doc in docEnlaces:
        print(doc.to_dict())
        dicEnlaces = doc.to_dict()
        lstEnlaces.append(dicEnlaces)


    session['biografia'] = dicBiografia
    session['enlaces'] = lstEnlaces

    return render_template('home.html')

@app.route('/peliculas')
def peliculas():
    listaPeliculas = ['CODA','ENCANTO','SONIC 2']

    nombre = request.args.get('nombre','')

    context = {
        'nombre':nombre,
        'peliculas':listaPeliculas
    }
    return render_template('peliculas.html',**context)

############### RUTAS DE MIS PAGINAS
@app.route('/acercade')
def about():
    return render_template('acercade.html')

@app.route('/portafolio')
def portafolio():
    colProyectos = db.collection('proyectos')
    docProyectos = colProyectos.get()

    lstProyectos = []
    for doc in docProyectos:
        print(doc.to_dict())
        dicProyecto = doc.to_dict()
        lstProyectos.append(dicProyecto)


    context = {
        'proyectos':lstProyectos
    }
    return render_template('portafolio.html',**context)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.run(debug=True)