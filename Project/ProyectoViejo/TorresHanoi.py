import pygame

class Torre:
    def __init__(self,listadiscos:list  , nombre:str ):
        self.listadiscos = listadiscos
        self.nombre = nombre

    def checkorder(self):#mira si los discos están ordenados
        for i in (0,len(self.listadiscos) -2):
            if(self.listadiscos[i].tamano > self.listadiscos[i+1].tamano):
                print(self.listadiscos[i+1].tamano)
                return(False)
        return(True)

    def AppendDisc(self,disco):
        self.listadiscos.append(disco)

    def printDiscs(self):
        #print("imprimiendo discos para " + self.nombre + ":")
        if(len(self.listadiscos) != 0):
            for i in self.listadiscos:
                print(i.nombre , i.tamano)
        else:
            print("empty")

    def pop(self):
        self.listadiscos.pop()

    def top(self):
        return(self.listadiscos[-1])

class Disco:
    def __init__ (self,nombre, tamano ):
        self.tamano = tamano
        self.nombre = nombre

class TorresHanoi:
    def __init__(self, torre1 , torre2 , torre3 ): #esto luego podria ser una lista de torres si quisiera hacer un programa para n torres con n discos
        self.torre1 = torre1
        self.torre2 = torre2
        self.torre3 = torre3
        self.turno = 0

    def printTowers(self):
        print("Turno : " , self.turno)
        print("(1) primera torre :")
        self.torre1.printDiscs()
        print("(2) segunda torre :")
        self.torre2.printDiscs()
        print("(3) tercera torre :")
        self.torre3.printDiscs()

    def checkrules():
        if(self.torre1.checkorder() and self.torre2.checkorder() and self.torre3.checkorder()): #esto puede tener errores
            return(True)
        else:
            return(False)

    def moveDisc(self , pos1 , pos2):
        try:
            if(pos1 == 1):
                if(pos2 == 2):
                    self.torre2.AppendDisc(self.torre1.top())
                    self.torre1.pop()
                    self.turno = self.turno +1
                if(pos2 == 3):
                    self.torre3.AppendDisc(self.torre1.top())
                    self.torre1.pop()
                    self.turno =  self.turno +1
            if(pos1 == 2):
                if(pos2 == 1):
                    self.torre1.AppendDisc(self.torre2.top())
                    self.torre2.pop()
                    self.turno =  self.turno + 1
                if(pos2 == 3):
                    self.torre3.AppendDisc(self.torre2.top())
                    self.torre2.pop()
                    self.turno = self.turno +1
            if(pos1 == 3):
                if(pos2 == 1):
                    self.torre1.AppendDisc(self.torre3.top())
                    self.torre3.pop()
                    self.turno = self.turno +1
                if(pos2 == 2):
                    self.torre2.AppendDisc(self.torre3.top())
                    self.torre3.pop()
                    self.turno = self.turno +1
        except:
            print("torre :" +str(pos1) + " esta vacia, no es posible mover elemento a " + "torre " +str(pos2) )

#aca creo una lista con
def listadiscos(lista , n):
    lista = []
    for i in range(1, n):
        discoi = Disco("Disco"+ str(i),i)
        lista.append(discoi)
    return lista

def Test():
    disco1 = Disco("disco1", 1)
    disco2 = Disco("disco2" , 2)
    disco3 = Disco("disco3" , 3)
    listadiscos = [disco3 , disco2, disco1 ]
    listadiscos2 = []
    listadiscos3 = []
    torretest = Torre(listadiscos , "torretest")
    torretest2 = Torre(listadiscos2 , "torretes2 ")
    torretest3 = Torre(listadiscos3 , "torretest3")
    torretest.printDiscs()
    print(torretest.checkorder())
    #torretest.pop()
    torretest.printDiscs()
    torretest2.printDiscs()
    juegotest = TorresHanoi(torretest , torretest2 , torretest3)
    juegotest.printTowers()
    juegotest.moveDisc(1,2)
    print(" \n \n luego de mover : \n \n")
    juegotest.printTowers()
    juegotest.moveDisc(2,3)
    print(" \n \n luego de mover : \n \n")
    juegotest.printTowers()
    juegotest.moveDisc(1,3)
    print(" \n \n luego de mover : \n \n")
    juegotest.printTowers()
    juegotest.moveDisc(3,2)
    print(" \n \n luego de mover : \n \n")
    juegotest.printTowers()



def main():
    listadiscos1 = listadiscos(listadiscos , 10)
    listadiscos2 = []
    listadiscos3 = []
    torre1 = Torre(listadiscos1 , "torre1")
    torre2 =  Torre(listadiscos2 ,"torre2")
    torre3 = Torre(listadiscos3 , "torre3")

    juego = TorresHanoi(torre1,torre2,torre3)

main()

Test()
#Cosas por hacer :

#hacer las reglas en pygame para que todo funcione
