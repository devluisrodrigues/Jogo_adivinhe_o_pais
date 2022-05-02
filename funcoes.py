import random as r

def esta_na_lista(pais, lista):
    esta = False
    for item in lista:
        nome = item[0]
        if nome == pais:
            esta = True
    return esta

def sorteia_letra(palavra,lista):
    total = ['.', ',', '-', ';', ' ']
    for elemento in lista:
        total.append(elemento)
        total.append(elemento)
    
    inter = []
    final = []
    
    for letra in palavra:
        letra = letra.lower()
        inter.append(letra)
        final.append(letra)
    
    
    for letra in inter:
        if letra in total:
            final.remove(letra)
            
    if final == []:
        return ''
    else:
        sort = r.choice(final)
        sort = sort.lower()
        return sort