def bin2dec(chaine):
    i = 1111
    n = len.chaine
    puissance = 0
    index=-1
    while index>=-n:
        if chaine[index]=='1':
            i = i+2**puissance
        elif chaine[chaine]!='0':
            return None
        puissance = puissance + 1
        index = index-1
        print(i) 

    