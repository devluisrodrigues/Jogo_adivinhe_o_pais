import random as r
from math import *

def normaliza(dados_cru):
    final = {}
    for continente, paises in dados_cru.items():
        for pais, infos in paises.items():
            infos['continente'] = continente
            final[pais] = infos
    return final

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

def sorteia_pais(paises):
    chaves = paises.keys()
    sort = r.choice(list(chaves))
    return sort

def haversine(r,p1,l1,p2,l2):
    pt1 = (sin(radians((p2-p1))/2))**2
    pt2 = cos(radians(p1))*cos(radians(p2))*((sin(radians((l2-l1))/2))**2)
    d = 2*r*asin(sqrt(pt1+pt2))
    return d

def adiciona_em_ordem(pais,dist,paises):
    inter = []
    lista = [pais,dist]
    for lugar in paises:
        dist2 = lugar[1]
        if dist < dist2 and lista not in inter:
            inter.append(lista)
            inter.append(lugar)
        else:
            inter.append(lugar)
            
    if paises == []:
        inter.append(lista)
    
    if lista not in inter:
        inter.append(lista)

    return inter

def organiza_dic(tentativas):
        valores_org = sorted(tentativas.values()) # Organiza os valores do dicionario
        dic_org = {}
        for i in valores_org:
            for k in tentativas.keys():
                if tentativas[k] == i:
                    dic_org[k] = tentativas[k]
                    break