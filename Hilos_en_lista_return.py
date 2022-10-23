from concurrent.futures import thread


import threading
import time

respuestas = [] # Aqui guardaremos las respuqestas de los hilos

def Afeitarse():
    time.sleep(6)
    respuestas.append("Me he afeitado!")

def Pesarse():
    time.sleep(3)
    respuestas.append("Me he pesado!")

def Desayunar():
    time.sleep(10)
    respuestas.append("He desayunado!")

lista_funciones = [Afeitarse, Pesarse, Desayunar]
lista_hilos = []

for i in range(3):
    hilo = threading.Thread(target=lista_funciones[i])
    hilo.start()
    lista_hilos.append(hilo)

for hilo in lista_hilos:
    hilo.join() # Cogemos cada hilo esperamos a que termine y lo metemos en el hilo principal

for respuesta in respuestas:
    print(respuesta)# Cogemos cada return guardado en nuestra lista respuestas y lo imprimimos

print(time.perf_counter())


