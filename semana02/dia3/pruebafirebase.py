# para concectarse a firebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("token.json")
firebase_admin.initialize_app(cred)

# para concectarse a firestore
from firebase_admin import firestore

db = firestore.client()

# accediendo a la colección de proyectos
colProyectos = db.collection('proyectos')
# obteniendo todos los proyectos que tengo
docProyectos = colProyectos.get()

# recorriendo el objeto
for doc in docProyectos:
    #para pasar el objeto a diccionario
    print(doc.to_dict())


