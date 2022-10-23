import requests
import time
import threading

#Este programa tiene como mision descargar 10 logos de colegiosantamonica lo mas rapido posible
r = requests
def DescargarImagen(Numero_png: int):
    '''
    Numero_png => El numero que se le asiganara a la imagen ejemplo : foto+Numero_png+.png
    '''
    respuesta = r.get("https://colegiosantamonica.eu/wp-content/uploads/2022/05/logo-colegio-agustinas-web.png")
    archivo = open("imagenes\\"+"foto" + str(Numero_png) + ".png", "xb")
    archivo.write(respuesta.content)
    print(("foto" + str(Numero_png) + " descargada!"))
    archivo.close()
    respuesta.close()

lista_hilos = []

for i in range(10):
    lista_hilos.append("hilo"+str(i))

for a in range(10):
    lista_hilos[a] = threading.Thread(target=DescargarImagen, args=(a,))
    lista_hilos[a].start()

#Vamos a esperar a que cada hilo acabe y volver al hilo principal
for b in range(10):
    lista_hilos[a].join()
    
print(time.process_time()) # Tiempo sin hilos : 2.208 seg
                            # Tiempo con hilos : 0.42 seg