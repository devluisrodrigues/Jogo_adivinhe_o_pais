from dados import DADOS
from funcoes import esta_na_lista, normaliza, sorteia_pais


print("\n\nBem-vindo ao Insper Países \n")
print("Versão desenvolvida por Luis e Leonardo \n")
print("Comandos: \n dica       - entra no mercado de dicas \n desisto    - desiste da rodada \n inventario - abre o inventario \n")

#Sorteando um pais:
basenormal = normaliza(DADOS)
pais = sorteia_pais(basenormal)
print("Um país foi escolhido, tente adivinhar!")

#Armazenando informações:
tentativas = {}


#Tentativas do jogador
jogada = input("Qual sera sua primeira jogada? ")
t = 20
print(f"Voce tem {t} tentativas:")
print(pais)

while t >= 1 and jogada != 'desisto':
    #JOGADOR ACERTOU
    if jogada == pais:
        print("Parabens Voce ganhou!!!!\n")
        print(f"O Pais escolhido era {pais}")
        break

    #JOGADOR QUER ABRIR O INVENTARIO
    elif jogada == "inventario":
        print("\n Seu inventario: \n")

    elif jogada == "Dica":
        print("Mercado de dicas")

    #Jogador que tentar um pais:
    elif esta_na_lista(jogada,basenormal):
        #A tentativa estava na lista de paises, mas nao era o correto
        if jogada in tentativas.keys():
            print("\n Esse país já foi testado \n")
            jogada = input("Qual será sua proxima tentativa? ")
        else:
            t -= 1

    #Tentativa INVALIDA:
    else:
        print("Sua tentativa e invalida, tente novamente.")
        jogada = input("Digite aqui sua proxima tentativa: ")