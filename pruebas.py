import time
lista = [36,38,39,40]

contador = 0
while True:
    print(lista[contador])
    contador += 1; contador = contador % len(lista)
    time.sleep(0.5)