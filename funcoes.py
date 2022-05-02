import random as r
from turtle import clear
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

clear
for i in range(30000):
    print(sorteia_letra('paralelipedo-amarelo-alemao-bonitinho',['c','p','n','h']))