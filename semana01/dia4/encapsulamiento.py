#clase para administrar los usuarios de un sistema
class Usuario:
    
    def __init__(self,nom,pwd):
        self.nombre = nom
        # self._password = pwd
        self.__password = pwd
        #default: public; _ : protected(se puede modificar dentro de la misma clase); __ : private(no se puede modificar a menos que sea por los métodos getter y setter)
        
    def iniciarSesion(self):
        if(self.nombre == 'admin' and self.__password == '12345'):
            print("Bienvenido " + self.nombre)
        else:
            print("Datos de acceso incorrectos" + " " + self.__password)            
        
#### usando mi clase usuario
usuario1 = Usuario('admin','admin')
usuario1.iniciarSesion()

usuario2 = Usuario('admin2','12345')
usuario2.__password='123456' #no será capaz de modificarse con private
usuario2.iniciarSesion()