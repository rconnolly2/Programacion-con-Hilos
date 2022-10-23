from concurrent.futures import thread
import threading
import time

def Afeitarse():
    time.sleep(3)
    print("Me he afeitado!")

def Pesarse():
    time.sleep(2)
    print("Me he pesado!")

def Desayunar():
    time.sleep(10)
    print("He desayunado!")


hilo1 = threading.Thread(target=Afeitarse) # Creamos hilo y asignamos que ejecute la funcion: Afeitarse
hilo1.start() # Empezamos hilo 1
hilo2 = threading.Thread(target=Pesarse) # Creamos hilo y asignamos que ejecute la funcion: Pesarse
hilo2.start() # Empezamos hilo 2
hilo3 = threading.Thread(target=Desayunar) # Creamos hilo y asignamos que ejecute la funcion: Desayunar
hilo3.start() # Empezamos hilo 3

#Afeitarse()
#Pesarse()
#Desayunar()

print(threading.active_count()) # Cantidad de hilos utilizandose
print(threading.enumerate())
print(time.perf_counter()) # Tiempo de ejecucion de hilo principal

