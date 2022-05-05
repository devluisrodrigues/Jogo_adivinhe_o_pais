from dados import DADOS
from funcoes import sorteia_pais


print("\n\nBem-vindo ao Insper Países \n")
print("Versão desenvolvida por Luis e Leonardo \n")
print("Comandos: \n dica       - entra no mercado de dicas \n desisto    - desiste da rodada \n inventario - exibe sua posição \n")

#Sorteando um pais:
pais = sorteia_pais(DADOS)
print(pais)