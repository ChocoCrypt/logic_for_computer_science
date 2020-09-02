import tkinter as tk
from PIL import Image
from time import sleep
class Torre(object):
    def __init__(self,numero,discos):
        self.numero=numero
        self.discos=discos
class Disco(object):
    def __init__(self,tamaño,posicion):
        self.tamaño=tamaño
        self.posicion=posicion
class letra_proposicional(object):
    def __init__(self,label,disc,torre,turno,posi):
        self.label=label
        self.disc=disc
        self.torre=torre
        self.turno=turno
        self.posicion=posi

letras = [chr(x) for x in range(97, 123)]
Discos=[1,2,3]
Torres=[1,2,3]
def letras(discos,palos):
    mylist=[]
    for i in Discos:
        for j in Torres:
            p=letra_proposicional(chr(96+i),i,j,1,4-i)
            mylist.append(p)
            print(p.label,"[",p.disc,p.torre,p.turno,p.posicion,"]")   #creamos todas las letras que me representaran la posicion de cada discon en cada turno
    return mylist

mylist2=[]
mylist2=letras(Discos,Torres)

##para la parte grafica existen 2 formas, la primera, es que como solamente son 8 pasos, se pueden poner 8 dibujos de fotos de hanoi
# la segunda, es hacer una animacion en pygame, consultar al profesor sobre cual es conveniente.
##imagenes

torre1 = Image.open("torre1.png")
torre2 = Image.open("torre2.png")
torre3 = Image.open("torre3.png")
torre4 = Image.open("torre4.png")
torre5 = Image.open("torre5.png")
torre6 = Image.open("torre6.png")
torre7 = Image.open("torre7.png")
torre8 = Image.open("torre8.png")


torre1.show()
# sleep(1)
# torre2.show()
# sleep(1)
# torre3.show()
# sleep(1)
# torre4.show()
# sleep(1)
# torre5.show()
# sleep(1)
# torre6.show()
# sleep(1)
# torre7.show()
# sleep(1)
# torre8.show()
