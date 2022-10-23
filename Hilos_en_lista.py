from concurrent.futures import thread


import threading
import time

def Afeitarse():
    time.sleep(6)
    print("Me he afeitado!")

def Pesarse():
    time.sleep(3)
    print("Me he pesado!")

def Desayunar():
    time.sleep(10)
    print("He desayunado!")

lista_funciones = [Afeitarse, Pesarse, Desayunar]
lista_hilos = []

for i in range(3):
    hilo = threading.Thread(target=lista_funciones[i])
    hilo.start()
    lista_hilos.append(hilo)

for hilo in lista_hilos:
    hilo.join() # Cogemos cada hilo esperamos a que termine y lo metemos en el hilo principal

print(time.perf_counter())

