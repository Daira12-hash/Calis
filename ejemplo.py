
#el usuario adivina un numero del 0 al 100, teniendo 10 intentos.
import random 
intentos=0
numero_random=random.randint(0,100)
limite =10

def adivina_numero():
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
            return numero_random
        if numero < numero_random:
            print ("Es mayor")
        if numero > numero_random:
            print("Es menor")       
    print("Perdiste")
    return numero_random
adivina_numero()



