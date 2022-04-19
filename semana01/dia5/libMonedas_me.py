class moneda:
    
    def __init__(self,monedaOrigen,monedaDestino,cambio):
        self.cambio = cambio
        self.monedaOrigen = monedaOrigen
        self.monedaDestino = monedaDestino
        
    def mostrar(self):
        print("La moneda de origen es " + self.monedaOrigen + " y su tipo de cambio a "+ self.monedaDestino + " es " + str(self.cambio))
        
    def convertir1(self,monto):
        if(self.monedaOrigen == "soles"):
            if(self.monedaDestino == "dolares"):
                resultado = monto / self.cambio
                print("El monto cambiado es: " + "$ {:,.2f}".format(resultado))
            elif(self.monedaDestino == "euros"):
                resultado = monto / self.cambio
                print("El monto cambiado es: " + "$ {:,.2f}".format(resultado))
        elif(self.monedaOrigen == "dolares"):
            if(self.monedaDestino == "soles"):
                resultado = monto * self.cambio
                print("El monto cambiado es: " + "$ {:,.2f}".format(resultado))
        elif(self.monedaOrigen == "euros"):
            if(self.monedaDestino == "soles"):
                resultado = monto * self.cambio
                print("El monto cambiado es: " + "$ {:,.2f}".format(resultado))
                
    def convertir2(self,monto):
        if(self.monedaOrigen == "soles" and self.monedaDestino == "dolares"):
            resultado = monto / self.cambio
            print("El monto cambiado es: " + "$ {:,.2f}".format(resultado))
        elif(self.monedaOrigen == "soles" and self.monedaDestino == "euros"):
            resultado = monto / self.cambio
            print("El monto cambiado es: " + "$ {:,.2f}".format(resultado))
        elif(self.monedaOrigen == "dolares" and self.monedaDestino == "soles"):
            resultado = monto * self.cambio
            print("El monto cambiado es: " + "$ {:,.2f}".format(resultado))
        elif(self.monedaOrigen == "euros" and self.monedaDestino == "soles"):
            resultado = monto * self.cambio
            print("El monto cambiado es: " + "$ {:,.2f}".format(resultado))
            

monedaDolares = moneda('soles','dolares',3.71)
monedaDolares.mostrar()
monedaDolares.convertir2(150)