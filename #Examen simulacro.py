#Examen simulacro

numero = int(input("Escriba un numero: "))
 
if numero > 0:
    print("el numero es postivio")
elif numero < 0:
    print("el numero es negativo")
else:
    print("es un cero")
#Programa 2
numero = float(input("Escribe un numero: "))
if numero % 2 == 0:
    print("es un numero par")
else:
    print("Es un numero impar")
#programa 3
N = int(input("Escriba un numero: "))
total = 0
for i in range (N):
 total +=i
print("el total es ", total)
#Programa 2 de ciclos
N = int(input("escribe un numero: "))
for i in range(N):
    if i % 2 ==0:
        print (i)
        