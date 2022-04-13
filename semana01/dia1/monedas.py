# PROGRAMA PARA CONVERTIR MONEDAS
#* VERSION 1.0 - CONVERTIR DE SOLES A DOLARES
# # INPUTS - ENTRADAS
# montoSoles = input("Ingrese el monto en soles: ")
# # PROCESO
# print (" opción 1 - soles a dolares")
# print (" opción 2 - dolares a soles")
# opcion = input("Elija una opción")
# montoDolares = float(montoSoles) / 3.80
# montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
# # OUTPUTS - SALIDAS
# print("El monto en dolares es: " + str(montoDolaresFormato))

#* VERSION 2.0 - CONVERTIR DE SOLES A DOLARES
# INPUTS - ENTRADAS
montoOrigen= input("Ingrese el monto a convertir: ")
# PROCESO
opcion = ""

while(opcion == ""):
    print (" opción 1 - soles a dolares")
    print (" opción 2 - dolares a soles")
    print (" opción 3 - soles a euros")
    print (" opción 4 - euros a soles")
    opcion = input("Elija una opción")
    if (opcion == "1"):    
        montoDolares = float(montoOrigen) / 3.80
        montoDolaresFormato = "$ {:,.2f}".format(montoDolares)
        # OUTPUTS - SALIDAS
        print("El monto en dolares es: " + str(montoDolaresFormato))
    elif (opcion == "2"):
        montoSoles = float(montoOrigen) * 3.80
        montoSolesFormato = "S/. {:,.2f}".format(montoSoles)
        # OUTPUTS - SALIDAS
        print("El monto en soles es: " , montoSolesFormato)
    elif (opcion == "3"):
        montoSoles = float(montoOrigen) / 4.05
        montoSolesFormato = "€ {:,.2f}".format(montoSoles)
        # OUTPUTS - SALIDAS
        print("El monto en euros es: " , montoSolesFormato)
    elif (opcion == "4"):
        montoEuros = float(montoOrigen) * 4.05
        montoSolesFormato = "S/. {:,.2f}".format(montoEuros)
        # OUTPUTS - SALIDAS
        print("El monto en soles es: " , montoSolesFormato)
    else:
        print("ALERTA!!! Debe seleccionar una opción valida")
        opcion = ""
        