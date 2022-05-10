from dados import DADOS, EARTH_RADIUS
from funcoes import esta_na_lista, haversine, normaliza, organiza_dic, sorteia_pais


print("\n\nBem-vindo ao Insper Países \n")
print("Versão desenvolvida por Luis e Leonardo \n")
print("Comandos: \n dica       - entra no mercado de dicas \n desisto    - desiste da rodada \n inventario - exibe dicas e posição \n")

#Sorteando um pais:
basenormal = normaliza(DADOS)
pais = sorteia_pais(basenormal)
print("Um país foi escolhido, tente adivinhar!")

#Armazenando informações:
tentativas = {}


#Tentativas do jogador
t = 20
print(f"Voce tem {t} tentativas:")
print(pais)
jogada = input("Qual sera sua primeira jogada? ")

while t >= 1 and jogada != 'desisto':
    #JOGADOR ACERTOU
    if jogada == pais:
        print("Parabens Voce ganhou!!!!\n")
        print(f"O Pais escolhido era {pais}")
        break

    #JOGADOR QUER ABRIR O INVENTARIO
    elif jogada == "inventario":
        print("\n Seu inventario: \n")

    #JOGADOR DECIDIU COMPRAR UMA DICA
    elif jogada == "Dica":
        print("Mercado de dicas")

    #Jogador quer tentar um país:
    elif esta_na_lista(jogada,basenormal):
        #A tentativa estava na lista de paises, mas nao era o correto
        if jogada in tentativas.keys():
            print("\n Esse país já foi testado \n")
            jogada = input("Qual será sua proxima tentativa? ")
        else:
            t -= 1
            p1 = basenormal[pais]["geo"]["latitude"]
            l1 = basenormal[pais]["geo"]["longitude"]
            p2 = basenormal[jogada]["geo"]["latitude"]
            l2 = basenormal[jogada]["geo"]["longitude"]
            dist = haversine(EARTH_RADIUS,p1,l1,p2,l2)
            tentativas[jogada] = dist
            certo = organiza_dic(tentativas)
    
        for pais, dist in certo.items():
            print(pais, '--------', dist)
        print(f"Voce ainda tem {t} tentativas restantes! \n")
        jogada = input("Qual sera sua proxima tentativa?")


    #Tentativa INVÁLIDA:
    else:
        print("Sua tentativa e invalida, tente novamente.")
        jogada = input("Digite aqui sua proxima tentativa: ")