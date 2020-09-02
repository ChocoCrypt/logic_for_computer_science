##punto 1 del taller 1 de logica para cs

def dosporn(n):
    if(n == 0):
        # print('retorno 0')
        return(0)
    else:
         print("retorno" ,  2 + dosporn( n -1 ))
        return (2 + dosporn( n -1 ))

def main():
    print(dosporn(10))

main()
