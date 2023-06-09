import threading
import time
import rtmidi

# Sistema MIDI arriba
midi_out = rtmidi.MidiOut()
available_ports = midi_out.open_port(0,"pythonmidi")

def bpm(seg):
    seg = 60 / seg
    return(seg)

pulso = bpm(90)
compas = pulso * 4


#pulsador midi. Envía las señales midi
def pulsar(nota,vol,pul,release):
    note_on = [0x99, nota, vol]
    midi_out.send_message(note_on)
    arcis = pul*release
    time.sleep(arcis)
    note_off = [0x89, nota, 0]
    midi_out.send_message(note_off)
    time.sleep(pul-arcis)

# secuenciador, ocupa la funcion pulsar
def sequ(nota,vel,pul,release,dur):
    #recorrido de los parametros
    notarec = 0
    velrec = 0
    pulrec = 0
    releaserec = 0
    while True:
        pulsar(nota[notarec],vel[velrec],dur/pul[pulrec],release[releaserec])

        # recorrido de listas
        notarec += 1; notarec = notarec % len(nota)
        velrec += 1; velrec = velrec % len(vel)
        pulrec += 1; pulrec = pulrec % len(pul)
        releaserec += 1; releaserec = releaserec % len(release)

# ejecutar en multihilo
def ejecutar(conjunto):
    hilos = []
    for valores in conjunto:
        hilo = threading.Thread(target=sequ, args=valores)
        print(hilo)
        hilo.start()
        hilos.append(hilo)
    for hilo in hilos:
        hilo.join()




bombo = (
[36,37],
[96,96],
[8,4,4],
[1,1],compas
    )

caja = (
[38,39,40],
[96,100],
[4,8,4],
[1,1,1],compas
    )

tom = (
[42, 43, 44],
[24,36,48,60,72],
[4,8,4,8],
[0],compas
    )

hihat = (
[45, 46, 47, 48, 49],
[24,48],
[8,16,16],
[0],compas
    )

varios = (
[51, 50],
[30,40,20],
[16,8,16],
[0.6,0.2,0.9,0.6],compas
    )
todo = [bombo, caja, tom, hihat, varios]
ejecutar(todo)


