import tabulate
#PROGRAMA PARA
# CREATE - C
# READ - R
# UPDATE - U
# DELETE - D

print("-" * 50)
print("|" + " " * 9 + "MATRICULA DE ALUMNOS EN CODIGO " + " "* 8 + "|")
print("-" * 50)
print("|" + " " * 9 + "MENU DE OPCIONES     " + " "* 18 + "|")
print("|" + " " * 9 + "[1] REGISTRAR ALUMNO " + " "* 18 + "|")
print("|" + " " * 9 + "[2] MOSTRAR ALUMNOS  " + " "* 18 + "|")
print("|" + " " * 9 + "[3] ACTUALIZAR ALUMNO" + " "* 18 + "|")
print("|" + " " * 9 + "[4] ELIMINAR ALUMNO  " + " "* 18 + "|")
print("|" + " " * 9 + "[5] SALIR            " + " "* 18 + "|")
print("-" * 50)

opcion = 0
alumnos = [{'nombre':'cesar mayta','email':'cesarmayta@gmail.com','celular':'232323'}]
# print(len(alumnos))

while(opcion != 5):
    opcion = int(input("INGRESE OPCION DEL MENU :"))    
    if(opcion == 1):
        print("NUEVO ALUMNO")        
        nombre  = input("NOMBRE  : ")
        email   = input("EMAIL   : ")
        celular = input("CELULAR : ")        
        dictAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(dictAlumno)        
        print("ALUMNO REGISTRADO CON EXITO!!!")
        
    elif(opcion == 2):
        print("RELACIÓN DE ALUMNOS")
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]
        print(tabulate.tabulate(registros,cabeceras, showindex=True))
        
    elif(opcion == 3):
        print("ACTUALIZAR ALUMNO")
        index = int(input("Ingrese el id del registro del alumno a actualizar: "))
        for x in range(0,len(alumnos)):            
            if x==index:
                nombre  = input("NOMBRE  : ")
                email   = input("EMAIL   : ")
                celular = input("CELULAR : ") 
                dictAlumno = {
                    'nombre':nombre,
                    'email':email,
                    'celular':celular
                }
                alumnos[x]=dictAlumno 
                print("REGISTRO DE ALUMNO ACTUALIZADO CON EXITO!!!")  
                              
    elif(opcion == 4):
        print("ELIMINAR ALUMNO")
        index = int(input("Ingrese el id del registro del alumno a eliminar: "))
        for x in range(0,len(alumnos)):            
            if x==index:
                del alumnos[x]   
                print("REGISTRO DE ALUMNO ELIMINADO CON EXITO!!!")   
                     
    elif(opcion == 5):
        print("FINALIZANDO PROGRAMA")
        
    else:
        print("OPCION INCORRECTA")