from pydoc import doc
from flask import Flask,render_template,request

# para concectarse a firebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

# para concectarse a firestore
from firebase_admin import firestore
db = firestore.client()
app = Flask(__name__)

# Accediendo a la base de datos biografia en firestore
colBiografia = db.collection('biografia')
docBiografia = colBiografia.get()
lstBiografia = []
for doc in docBiografia:
    # print(doc.to_dict())
    dicBiografia = doc.to_dict()
    
# Accediendo a la base de datos biografia en firestore
colEnlaces = db.collection('enlaces')
docEnlaces = colEnlaces.get()
lstEnlaces = []
for doc in docEnlaces:
    print(doc.to_dict())
    dicEnlaces = doc.to_dict()
    lstEnlaces.append(dicEnlaces)



#* Trabajando con la api de github
@app.route('/')
def index():
    
    context = {
        'biografia':dicBiografia,
        'enlaces':lstEnlaces
    }

    return render_template('home.html',**context)

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
    context = {
        'biografia':dicBiografia,
        'enlaces':lstEnlaces
    }
    return render_template('acercade.html',**context)

@app.route('/portafolio')
def portafolio():
    colProyectos = db.collection('proyectos')
    docProyectos = colProyectos.get()
    #print(docProyectos)
    lstProyectos = []
    
    for doc in docProyectos:
        # print(doc.to_dict())
        dicProyecto = doc.to_dict()
        lstProyectos.append(dicProyecto)       
    
    context = {
        'proyectos':lstProyectos,
        'biografia':dicBiografia,
        'enlaces':lstEnlaces        
    }

    return render_template('portafolio.html',**context)

@app.route('/contacto')
def contacto():
    context = {
        'biografia':dicBiografia,
        'enlaces':lstEnlaces
    }
    return render_template('contacto.html',**context)

app.run(debug=True)


