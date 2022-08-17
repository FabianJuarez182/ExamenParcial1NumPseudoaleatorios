# Universidad del Valle de Guatemala
# Departamento de Ingeniería
# Matematica Discreta seccion 10
# Fabián Estuardo Juárez Tello 21440
# Catedrático: Mario Castillo

#Crear las variables y listas para utilizar las variables
ArrayFinal = []

#Pedir la variable del modulo para utilizar en las listas
cantNumPseudo = input("\n Ingrese la cantidad de numeros pseudoaleatorios que quiere generar: ")
m = input("\nIngrese el modulo: ")
a = input("\n Ingrese el multiplicador: ")
c = input("\n Ingrese el incremento: ")
s = input("\n Ingrese una semilla: ")
contador = 0
impresion = ""
#ciclo para generar el numero psudoaleatorio
for i in range(int(cantNumPseudo)): 
    if (contador < 1): #Condicion para el primer numero
        contador = contador + 1
        numPseu = 2
        ArrayFinal.append(numPseu)
        numPseudo = numPseu
    else: #Condicion para los siguientes numeros
        numPseudo = ((int(a)*int(numPseudo))+int(c)) % int(m)
        ArrayFinal.append(numPseudo)
#ciclo para imprimir los datos en pantalla
for i in range(int(cantNumPseudo)):
    if (i > 0 and i < int(cantNumPseudo)-1):
        impresion += str(ArrayFinal[i]) + ", "
    if (i> 0 and i == int(cantNumPseudo)-1):
        impresion += str(ArrayFinal[i])
print("\n[" + impresion + "]")