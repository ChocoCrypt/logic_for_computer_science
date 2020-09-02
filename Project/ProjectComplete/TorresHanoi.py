import pygame
import copy
from Tree import *
#a Tseitin tengo que ponerle la formula inorder

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


def codifica(f, c, Nf, Nc):
    # Funcion que codifica la fila f y columna c

    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf) - 1  + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1)  + "\nSe recibio " + str(c)

    n = Nc * f + c
    # print(u'Número a codificar:', n)
    return n

def codifica4(T, D, P, N , Nt, Nd, Np, Nn):
    # Funcion que codifica cuatro argumentos
    assert((T >= 0) and (T <= Nt - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nt - 1) + "\nSe recibio " + str(T)
    assert((D >= 0) and (D <= Nd - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nd - 1) + "\nSe recibio " + str(D)
    assert((P >= 0) and (P <= Np - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Np - 1)  + "\nSe recibio " + str(P)
    assert((N >= 0) and (N <= Nn - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nn - 1)  + "\nSe recibio " + str(N)
    v1 = codifica(T, D, Nt, Nd)
    v2 = codifica(v1, P, Nt * Nd, Np)
    v3 = codifica(v2, N, Nt*Nd*Np ,Nn)
    return v3

def decodifica4(x, Nt, Nd, Np, Nn):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    v2, N = decodifica(x, Nt*Nd*Np, Nn)
    v1, P = decodifica(v2, Nt * Nd , Np)
    T, D = decodifica(v1, Nt, Nd)

    return T, D, P,N

def decodifica(n, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla

    assert((n >= 0) and (n <= Nf * Nc - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(Nf * Nc - 1) + "\nSe recibio " + str(n)

    f = int(n / Nc)
    c = n % Nc
    return f, c

def Regla0(Nt,Nd,Np,Nn): # regla ayudada por Edgar
    #Un disco solo puede estar en una posición por turno
    Inicial_Regla = True
    for N in range(Nn):
        for D in range(Nd):
            for T in range(Nt):
                for P in range(Np): #hasta acá se recorre todo el arreglo y se empiezan a definir lasreglas

                    inicial_clau=True

                    for j in range(Nt):
                        for i in range(Np):
                            if not(i==0 and j==0):
                                if inicial_clau:
                                    inicial_clau=False
                                    clau=chr(256+codifica4((T+j)%Nt,D,(P+i)%Np,N,Nt,Nd,Np,Nn))
                                else:
                                    clau+=chr(256+codifica4((T+j)%Nt,D,(P+i)%Np,N,Nt,Nd,Np,Nn))+"O"
                            
#                    print("clau",clau)
                    if(Inicial_Regla):
                        Regla=clau+"-"+chr(256+codifica4(T,D,P,N,Nt,Nd,Np,Nn))+">"
                        Inicial_Regla = False
                    else:
                        Regla += clau+"-"+chr(256+codifica4(T,D,P,N,Nt,Nd,Np,Nn))+">" + "Y"


                        
    
    print(Regla)
    return Regla

def Regla1(Nt , Nd , Np , Nn): #no puede haber un disco mas grande sobre uno mas pequeño que el
    #sea  F > D , L >  P
    #si P(T,D,P,N ) > -P(T,F,L,N)
     Inicial_Regla = True
     clau = ""
     for N in range(Nn):
        for T in range(Nt):
            if(Inicial_Regla):
                Regla = chr(256 + codifica4 (T,1,1,N,Nt,Nd,Np,Nn))  + "-"

                Inicial_Regla = False
            else:
                 Regla += chr(256 + codifica4 (T,1,1,N,Nt,Nd,Np,Nn))  + "-" + "Y"

                    


     return Regla

def Regla2(Nt, Nd , Np , Nn): # si hay un disco sobre otro disco, no se puede mover
    #sea K > P
    #vi P(T,0,0,N) and P(T,1    ,1 , N ) >  P(T   , 0 , 0    , N+1)
    # > and  P(0,D,P,N)  P(0,0+i ,K , N )    P(T   , 0 , P    , N+1)
     initial_claus =  True
     for N in range(Nn -1):
        for T in range(Nt):
            if(initial_claus):
                initial_claus = False
                    # > and  P(T,0,0,N)  P(T,1   ,1 , N )    P(T   , 0 , 0    , N+1)
                clauaux =  chr(256 + codifica4(T,0,0,N+1,Nt, Nd, Np , Nn))+chr(256 + codifica4(T,  1,1,N, Nt, Nd, Np, Nn))+chr(256 + codifica4(T,0,0,N, Nt, Nd, Np , Nn)) + "Y" + ">"
            else:
                clauaux += chr(256 + codifica4(T,0,0,N+1,Nt, Nd, Np , Nn))+chr(256 + codifica4(T,  1,1,N, Nt, Nd, Np, Nn))+chr(256 + codifica4(T,0,0,N, Nt, Nd, Np , Nn)) + "Y" + ">"+ "Y"


                           
 #                   print("clau", clau)
     return clauaux
def Regla3(Nt, Nd, Np, Nn):   
    #sta es la regla que gana
    #se gana cuando todos los discos están ordenados correctamente en una torre diferente a la inicial
    #lo anterior es equivalente a decir que se gana cuando todos los discos están en una torre diferente a la inicial  
    #P(T,D,P,N) and P(T , D+1 , P+1 , N) and  p(T, D+1 , P+1 , N)

    Regla = clau +  chr(256 + codifica4(T,D,P,N , Nt , Nd , Np , Nn)) + "Y"    #así no estamos seguros si es que se escribe en polaco 

    return(Regla)

def Regla4(Nt, Nd , Np , Nn):
    #no puede haber dos discos en la misma posicion

    for N in range(Nn):
        for D in range(Nd):
            for T in range(Nt):
                for P in range(Np):   

                    clau_ini  = True 

                    for i in range(Nd):
                        if(i != 0 ):
                            if(clau_ini):
                                clau = chr(256 + codifica4(T , (D+i)%Nd , P, N, Nt, Nd , Np, Nn))
                            else:
                                clau += chr(256 + codifica4(T , (D+i)%Nd , P, N, Nt, Nd , Np, Nn)) + "O"
                                
                    Regla=clau+"-"+chr(256+codifica4(T,D,P,N,Nt,Nd,Np,Nn))+">"
    return(Regla)

                 
                      


                    





def Reglafinal(T,D, P, N):
    regla = Regla0(T,D,P,N) + "Y" + Regla1(T,D,P,N) + "Y" + Regla2(T,D,P,N) + "Y" + Regla3(T,D,P,N) + "Y" + Regla4(T,D,P,N)
    print(regla)
    return(regla)

def ReglafinalPolaca(T,D, P, N):
    regla = Regla0(T,D,P,N) + Regla1(T,D,P,N) +  Regla2(T,D,P,N)  + Regla3(T,D,P,N)  + Regla4(T,D,P,N) + "Y" + "Y" + "Y" + "Y"
    print(regla)
    return(regla)







def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B













def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(3000, 4000)]
    atomos = letrasProposicionalesA + letrasProposicionalesB
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    l = []
    pila = []
    i = -1
    s = A[0]
    while len(A) > 0:
        if s in atomos and len(pila) > 0 and pila[-1] == '-' :
            i += 1
            atomo = letrasProposicionalesB[i]
            pila = pila[:-1]
            pila.append(atomo)
            l.append(atomo + '=-' + s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
        elif s == ')':
            w = pila[-1]
            o = pila[-2]
            v = pila[-3]
            pila = pila[:len(pila)-4]
            i += 1
            atomo = letrasProposicionalesB[i]
            l.append(atomo + "=(" + v + o + w+")")
            s = atomo
        else:
            pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
    b = ''
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = letrasProposicionalesB[i]
    for x in l:
        y = enFNC(x)
        b += 'Y' + y
    b = atomo + b

    return b

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales
def Clausula(C):
    l = []
    while len(C)>0:
        s = C[0]
        if s == "O":
            C = C[1:]
        elif s == "-":
            literal = s + C[1]
            l.append(literal)
            C = C[2:]
        else:
            l.append(s)
            C = C[1:]
    return l

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):
    l = []
    i = 0
    while len(A)> 0:
        if i >= len(A):
            l.append(Clausula(A))
            A = []
        else:
            if A[i] == 'Y':
                l.append(Clausula(A[:i]))
                A = A[i+1:]
                i = 0
            else:
                i+=1
    return l

def clausulaU(S):
    for i in S:
        if(len(i)==1):
            return i[0]
    return '-1'

def neg(a):
    if len(a) == 1:
        l = "-" + a
    else:
        l = a[-1]
    return l


def unitPropagate(S, I):
    bool = True
    while bool:
        for k in S:
            if len(k) == 0:
                #return "Insatisfacible", {}
                break

        cont = 0
        for i in S:
            if len(i) == 1:
                cont += 1
                lit = i[0]
                if len(lit) == 1:
                    pp = lit
                    compl = "-" + lit
                    valor = 1

                elif(len(lit) == 2):
                    pp = lit[1]
                    compl = lit[1]
                    valor = 0

                for j in S:
                    if j != i:
                        if lit in j:
                            S.remove(j)
                I[pp] = valor
                S.remove(i)
                #print(i)


        if cont == 0:
            bool = False
        else:
            for k in S:
                if compl in k:
                    k.remove(compl)
    return S, I

def DPLL(s, i):
    void = []
    s, i = unitPropagate(s,i)
    if void in s:
        return "Insatisfacible", {}
    elif len(s) == 0:
        return "Satisfacible", i
    l = ""
    for y in s:
        for x in y:
            if x not in i.keys():
                l = x
    l_comp = neg(l)
    if l == "":
        return None
    Sp = copy.deepcopy(s)
    Sp = [n for n in Sp if l not in n]
    for q in Sp:
        if l_comp in q:
            q.remove(neg(l))
    Ip = copy.deepcopy(i)
    if l[0] == "-":
        Ip[l[1]] = 0
    else:
        Ip[l] = 1
    S1, I1 = DPLL(Sp, Ip)
    if S1 == "Satisfacible":
        return S1, I1
    else:
        Spp = copy.deepcopy(s)
        Spp = [q for q in Spp if neg(l) not in q]
        for h in Spp:
            if l in h:
                h.remove(l)
        Ipp = copy.deepcopy(i)
        if l[0] == "-":
            Ipp[l[1]] = 0
        else:
            Ipp[l] = 1
        return DPLL(Spp, Ipp)
   
    



def main():
    Nt=3
    Nd=2
    Np=2
    Nn=2

    #y=Regla3(Nt,Nd,Np,Nn)
    print("regla final :")
    final = Regla2(Nt, Nd, Np, Nn)
    finalstring = String2Tree(final)
    finalorder = Inorder(finalstring)
    print(finalorder)
    listacaracteres =[]
    for i in range(256,2999): # este for llena la lista
        listacaracteres.append(chr(i))
    
    for i in final:
        if(i in listacaracteres):
            T,D,P,N = decodifica4(ord(i) -256 ,Nt,Nd,Np,Nn)
            print(i , "torre : ", T , "disco" , D , "pos :", P , "turno" , N)

    #aca hay un problema porque al arbol tengo que darle la norma pero en notación inorder
    '''TS = Tseitin(final,listacaracteres) 
    print("Tseitin :")
    print(TS)
    finclaus = formaClausal(TS) 
    print("Forma Clausal")
    print(finclaus)


    dictVacio = {}
    
    resp = DPLL(finclaus,dictVacio)
    print("DPLL :")
    print(resp)
    respfinal = {}
    for i in resp[1]:
        if(i in listacaracteres):
            respfinal[i] = resp[1][i]


    print("\n \n \n" , respfinal)

    #ahora hay que decodificar las cosas
    #y luego hay que graficar la respuesta
 '''

main()

#Test()

