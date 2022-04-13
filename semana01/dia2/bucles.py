#entrada
tabla = int(input("Ingresa la tabla de multiplicar que desea mostrar: "))
#proceso
valor1 = tabla*1;
valor2 = tabla*2;
valor3 = tabla*3;
#salida
print(str(tabla )+ " x 1 = " + str(valor1))
print(str(tabla )+ " x 2 = " + str(valor2))
print(str(tabla )+ " x 3 = " + str(valor3))

#* Tabla de mutliplicar usando for
print("Tabla usando for")
for contador in range(1,10,2): #* range(1,10,2) -> el ',2' es el incremento en cada iteración
    valor = tabla * contador
    #print(str(tabla) + ' X ' + str(contador) + ' = ' + str(valor))
    print(tabla,' X ',contador,' = ',valor)