#Colore as linhas do terminal
from colorama import Fore
#Sorteia um valor de uma lista
from random import choices
#Acessa o banco de dados para o funcionamento do exercicio
from dados import DADOS, EARTH_RADIUS
#Codigo separado para o mercado de dicas
from dicas import  mercado_dicas
#Acessa as funcoes requisitadas
from funcoes import esta_na_lista, haversine, normaliza, organiza_dic, sorteia_letra, sorteia_pais
#Funcao separada para colorir o numero de tentativas restantes
from tentativas import tentativas_res

#Da inicio ao loop do jogo, irá se repetir até o usuário digitar n
dnv = True
while dnv == True:
    print("\n\nBem-vindo ao Insper Países \n")
    print(Fore.GREEN + "Versão desenvolvida por Luis e Leonardo \n" + Fore.RESET)
    print("Comandos: \n dica       - entra no mercado de dicas \n desisto    - desiste da rodada \n inventario - exibe dicas e posição \n")

    #Sorteando um pais:
    ganhou = False
    basenormal = normaliza(DADOS)
    pais = sorteia_pais(basenormal)
    print("Um país foi escolhido, tente adivinhar!")

    #Armazenando informações:
    #armazena tentativas e suas respectivas distancias
    tentativas = {}
    certo = {}
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

    #Tentativas do jogador:
    t = 20
    print("Voce tem " + Fore.LIGHTMAGENTA_EX + f"{t}" +Fore.RESET + " tentativas:")
    jogada = input("Qual sera sua primeira jogada? ")
    jogada = jogada.lower()

    while t >= 1 and jogada != 'desisto':
        #JOGADOR ACERTOU
        if jogada == pais:
            print(Fore.LIGHTGREEN_EX + "\n Parabens Voce ganhou!!!!\n")
            print(f"  O Pais escolhido era {pais}" + Fore.RESET)
            ganhou = True
            break

        #JOGADOR QUER ABRIR O INVENTARIO
        elif jogada == "inventario":
            print("\n Seu inventario: ")

            #Dicas que o usuario possui:
            print(' Dicas:')
            for titulo, item in dicas.items():
                print(f"{titulo} {item}")
            print('\n')

            #Tentativas que o usuário fez
            print(' Tentativas:')
            for nome, dist in certo.items():
                if dist <= 1000:
                    print(Fore.LIGHTGREEN_EX + f"{nome}", '--------', f"{dist}" + Fore.RESET)
                elif dist <= 2000:
                    print(Fore.GREEN + f"{nome}", '--------', f"{dist}" + Fore.RESET)
                elif dist <= 3000:
                    print(Fore.LIGHTYELLOW_EX + f"{nome}", '--------', f"{dist}" + Fore.RESET)
                elif dist <= 5000:
                    print(Fore.RED + f"{nome}", '--------', f"{dist}" + Fore.RESET)
                elif dist <= 10000:
                    print(Fore.MAGENTA + f"{nome}", '--------', f"{dist}" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLACK_EX + f"{nome}", '--------', f"{dist}" + Fore.RESET)

            print(tentativas_res(t))
            jogada = input("Qual sera sua proxima tentativa?")
            jogada = jogada.lower()

        #JOGADOR DECIDIU COMPRAR UMA DICA
        elif jogada == "dica":
            opcoes = mercado_dicas(t,dicas)
            escolhida = int(input(f'Escolha uma dica: {opcoes}: '))

            #Conferir o mercado de dicas, cada dica terá um preco e uma info diferente para ajudar o usuario

            if escolhida not in opcoes:
                print("Essa dica não está disponível no momento, tente novamente")
                print("Saindo do mercado de dicas")

            elif escolhida == 0:
                print("Saindo do mercado de dicas")

            elif escolhida == 1 and t > 4:
                print("Cor da bandeira")
                rgb = list(cores.keys())
                port = list(cores.values())
                if cores == {}:
                    print("\nTodas as cores já foram fornecidas")
                    print("\nSaindo do mercado de dicas...")
                else:
                    cor = choices(rgb,port)[0]
                    del cores[cor]
                    draw.append(cor)
                    dicas["Cor da bandeira: "] = draw
                    t -= 4

            elif escolhida == 2 and t > 3:
                if "Letra da capital:" not in dicas:
                    letras = []
                ele = sorteia_letra(basenormal[pais]["capital"],letras)
                if "Letra da capital:" not in dicas:
                    dicas["Letra da capital:"] = [ele]
                    letras = [ele]
                    t -= 3
                elif ele == '':
                    print("\nTodas as letras da capital já foram sorteadas")
                    print("Saindo do mercado de dicas")
                else:
                    dicas["Letra da capital:"].append(ele)
                    letras.append(ele)
                    t -= 3
            
            elif escolhida == 3 and t > 6:
                if 'Area: 'not in dicas:
                    dicas["Area: "] = str(basenormal[pais]['area']) + " KM^2"
                    t -= 6
                else:
                    print('Dica ja escolhida')
                    print('Saindo do mercado de dicas')

            elif escolhida == 4 and t > 5:
                if 'Populacao: ' not in dicas:
                    dicas['Populacao: '] = str(basenormal[pais]['populacao']) + ' Habitantes'
                    t -= 5
                else:
                    print('Dica ja escolhida')
                    print('saindo do mercado de dicas')        

            elif escolhida == 5 and t > 7:
                if 'Continente: ' not  in dicas:
                    dicas['Continente: '] = basenormal[pais]['continente']
                    t -= 7
                else:
                    print('Dica ja escolhida')
                    print('saindo do mercado de dicas') 
            
            else:
                print("Essa dica não está disponível no momento, tente novamente")
                print("Saindo do mercado de dicas")
            print('\n Dicas:')
            for titulo, item in dicas.items():
                print(f"{titulo} {item}")

            print(tentativas_res(t))
                
            jogada = input("Qual será sua próxima jogada? ")
            jogada = jogada.lower()
        
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
            print("\n")
            for nome, dist in certo.items():
                if dist <= 1000:
                    print(Fore.LIGHTGREEN_EX + f"{nome}", '--------', f"{dist}" + Fore.RESET)
                elif dist <= 2000:
                    print(Fore.GREEN + f"{nome}", '--------', f"{dist}" + Fore.RESET)
                elif dist <= 3000:
                    print(Fore.LIGHTYELLOW_EX + f"{nome}", '--------', f"{dist}" + Fore.RESET)
                elif dist <= 5000:
                    print(Fore.RED + f"{nome}", '--------', f"{dist}" + Fore.RESET)
                elif dist <= 10000:
                    print(Fore.MAGENTA + f"{nome}", '--------', f"{dist}" + Fore.RESET)
                else:
                    print(Fore.LIGHTBLACK_EX + f"{nome}", '--------', f"{dist}" + Fore.RESET)

            if t>0:
                print(tentativas_res(t))
                jogada = input("Qual sera sua proxima tentativa?")
                jogada = jogada.lower()


        #Tentativa INVÁLIDA:
        else:
            print("Sua tentativa e invalida, tente novamente.")
            jogada = input("Digite aqui sua proxima tentativa: ")
            jogada = jogada.lower()

    #Usuario nao foi capaz de acertar o pais
    if not ganhou:
        print(Fore.LIGHTRED_EX+"\n Suas tentativas esgotaram, voce perdeu \n"+ Fore.RESET)
        print(f"O pais sorteado era {pais}")

    #Apos o fim da rodada, programa pergunta ao usuario se ele deseja uma nova tentativa, caso não, finaliza o loop do jogo.
    perg = input("Voce deseja jogar novamente? [s/n] ")
    if perg == 's':
        dnv = True
    else:
        dnv = False

print("\n Obrigado por jogar")
print(' Ate a proxima =) \n')