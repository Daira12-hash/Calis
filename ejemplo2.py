


import random 
intentos=0
numero_random=50
limite =10
while intentos < limite:
    intentos= intentos + 1
    numero=int(input("adivina el numero del 0 al 100, tienes 10 intentos"))
    if numero == numero_random:
        print("Ganaste")
        quedan = limite -  intentos
        print(f"\intentos restantes{quedan}")
        intentos=11
    if numero < numero_random:
        print ("Es mayor")
    if numero > numero_random:
        print("Es menor")
if numero != numero_random:
    print("Perdiste")

