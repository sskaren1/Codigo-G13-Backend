opcion = 0
while(opcion > 0):
    print("=====OPCIONES=====")
    print("1) opción 01")
    print("2) opción 02")
    print("3) opción 03")
    print("4) salir")
    opcion = int(input("opcion elegida:"))
    print("ud selecciono la opcion " + str(opcion))
    salir= input("desea salir (si/no)")
    if(salir=="no"):
        opcion = 0