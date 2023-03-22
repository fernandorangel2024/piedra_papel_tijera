# Piedra, papel o tijera

import random

print("--------------------------------------------")
print("-----------Piedra, papel o tijera-----------")
print("--------------------------------------------")

print("1 Corresponde a piedra")
print("2 Corresponde a papel")
print("3 Corresponde a tijera")

# input

j = int(input(" TU ELECCIÓN : "))
    
# processing

m = random.randint(1,3)

if (j == 1):  #piedra
    if (m == 1):
        print("Empate")
        print("Elegiste piedra y la máquina sacó piedra")
    elif (m==2):
        print("Lo siento, perdiste")
        print("Elegiste piedra y la máquina saco papel")
    else:
        print("Felicidades, ganaste")
        print("Elegiste piedra y la máquina sacó tijera")

        
if (j == 2): #papel
    if (m == 1):
        print("Felicidades, ganaste")
        print("Elegiste papel y la máquina sacó piedra")
    elif (m == 2):
        print("Empate")
        print("Elegiste papel y la máquina sacó papel")
    else:
       print ("Lo siento, perdiste")
       print("Elegiste papel  y la máquina sacó tijera")


if (j == 3): #tijera
    if ( m == 1):
        print("Lo siento, perdiste")
        print("Elegiste tijera y la máquina sacó piedra")
    elif ( m ==2):
        print("Felicidades, ganaste")
        print("Elegiste tijera y la máquina sacó papel")
    else:
        print("Empate")
        print("Elegiste tijera y la máquina sacó tijera")

if (j > 3):
    print("Ingresaste una opcion inválida, revisa las opciones")