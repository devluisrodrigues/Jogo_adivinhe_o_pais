from random import choices
from dados import DADOS, EARTH_RADIUS
from dicas import escolhe_dica, mercado_dicas
from funcoes import esta_na_lista, haversine, normaliza, organiza_dic, sorteia_letra, sorteia_pais


print("\n\nBem-vindo ao Insper Países \n")
print("Versão desenvolvida por Luis e Leonardo \n")
print("Comandos: \n dica       - entra no mercado de dicas \n desisto    - desiste da rodada \n inventario - exibe dicas e posição \n")

#Sorteando um pais:
basenormal = normaliza(DADOS)
pais = sorteia_pais(basenormal)
print("Um país foi escolhido, tente adivinhar!")

#Armazenando informações:
#armazena tentativas e suas respectivas distancias
tentativas = {}
#armazenas as dicas fornecidas ao usuario
dicas = {}
#armazena as letras já sorteada na lista de letras da capital:
letras = []
#armazena as cores já sorteadas na lista de cores da bandeira:
draw = []

#Limpando cores da bandeira:
lixo = []
band = basenormal[pais]['bandeira']
cores = band
for cor, portcent in band.items():
    if portcent == 0:
        lixo.append(cor)
    if cor == 'outras':
        lixo.append(cor)
for valor in lixo:
    del cores[valor]

#Tentativas do jogador
t = 20
print(f"Voce tem {t} tentativas:")
print(pais)
jogada = input("Qual sera sua primeira jogada? ")

while t >= 1 and jogada != 'desisto':

    #JOGADOR ACERTOU
    if jogada == pais:
        print("\n Parabens Voce ganhou!!!!\n")
        print(f"O Pais escolhido era {pais}")
        break

    #JOGADOR QUER ABRIR O INVENTARIO
    elif jogada == "inventario":
        print("\n Seu inventario: \n")

    #JOGADOR DECIDIU COMPRAR UMA DICA
    elif jogada == "dica":
        opcoes = mercado_dicas(t)
        escolhida = int(input(f'Escolha uma dica: {opcoes}: '))

        if escolhida not in opcoes:
            print("Essa dica não está disponível no momento, tente novamente")
            print("Saindo do mercado de dicas")

        elif escolhida == 0:
            print("Saindo do mercado de dicas")

        elif escolhida == 1:
            print("Cor da bandeira")
            rgb = list(cores.keys())
            port = list(cores.values())
            if cores == {}:
                print("\nTodas as cores já foram forncidas")
                print("\nSaindo do mercado de dicas...")
            else:
                cor = choices(rgb,port)[0]
                print(cor)
                del cores[cor]
                draw.append(cor)
                dicas["Cor da bandeira: "] = draw

        elif escolhida == 2:
            if "Letra da capital:" not in dicas:
                letras = []
            ele = sorteia_letra(basenormal[pais]["capital"],letras)
            if "Letra da capital:" not in dicas:
                dicas["Letra da capital:"] = [ele]
                letras = [ele]
            else:
                dicas["Letra da capital:"].append(ele)
                letras.append(ele)
        
        elif escolhida == 3:
            if 'Area'not in dicas:
                dicas["Area"] = str(basenormal[pais]['area']) + " KM^2"
            else:
                print('Dica ja escolhida')
                print('Saindo do mercado de dicas')

        elif escolhida == 4:
            if 'Populacao' not in dicas:
                dicas['Populacao'] = basenormal[pais]['populacao']
            else:
                print('Dica ja escolhida')
                print('saindo do mercado de dicas')        

        elif escolhida == 5:
            if 'Continente' not  in dicas:
                dicas['Continente: '] = basenormal[pais]['continente']
            else:
                print('Dica ja escolhida')
                print('saindo do mercado de dicas') 

        print('\n Dicas:')
        for titulo, item in dicas.items():
            print(f"{titulo} {item}")
        print('\n')
            
        jogada = input("Qual será sua próxima jogada? ")
        
    #Jogador quer tentar um país:
    elif jogada in basenormal:
        #A tentativa estava na lista de paises, mas nao era o correto
        if jogada in tentativas.keys():
            print("\n Esse país já foi testado \n")
        else:
            t -= 1
            p1 = basenormal[pais]["geo"]["latitude"]
            l1 = basenormal[pais]["geo"]["longitude"]
            p2 = basenormal[jogada]["geo"]["latitude"]
            l2 = basenormal[jogada]["geo"]["longitude"]
            dist = haversine(EARTH_RADIUS,p1,l1,p2,l2)
            tentativas[jogada] = dist
            certo = organiza_dic(tentativas)
    
        for nome, dist in certo.items():
            print(nome, '--------', dist)
        print(f"Voce ainda tem {t} tentativas restantes! \n")
        jogada = input("Qual sera sua proxima tentativa?")


    #Tentativa INVÁLIDA:
    else:
        print("Sua tentativa e invalida, tente novamente.")
        jogada = input("Digite aqui sua proxima tentativa: ")