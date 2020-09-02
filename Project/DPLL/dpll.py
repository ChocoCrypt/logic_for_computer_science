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
