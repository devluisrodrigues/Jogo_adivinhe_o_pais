from funcoes import sorteia_letra


def mercado_dicas(t):
    opcoes = []
    dicas = {}
    dicas[4] = ["Cor da Bandeira -- custa 4 tentativas",1]
    dicas[3] = ["Letra da capital - custa 3 tentativas",2]
    dicas[6] = ["Área             - custa 6 tentativas",3]
    dicas[5] = ["População        - custa 5 tentativas",4]
    dicas[7] = ["Continente       - custa 7 tentativas",5]
    dicas[0] = ["Sem dica",0]
    for nome, info in dicas.items():
        if t > nome:
            opcoes.append(info[1])
            print(f'{info[1]}.{info[0]}')  
    return opcoes

letras = []
def escolhe_dica(basenormal,pais,escolhida, dicas,letras):
    elif jogada == "dica":
        opcoes = mercado_dicas(t)
        escolhida = int(input(f'Escolha uma dica: {opcoes}'))
        if escolhida not in opcoes:
            print("Essa dica não está disponível no momento, tente novamente")
            print("Saindo do mercado de dicas")
        elif escolhida == 0:
            print("Saindo do mercado de dicas")
        elif escolhida == 1:
            print("Cor da bandeira")
        elif escolhida == 2:
            ele = sorteia_letra(basenormal[pais]["capital"],letras)
            if "Letra da capital:" not in dicas:
                dicas["Letra da capital:"] = [ele]
                letras = [ele]

            else:
                dicas["Letra da capital:"].append(ele)
                letras.append(ele)
        
        elif escolhida == 3:
            if 'Area'not in dicas:
                dicas["Area"] = basenormal[pais]['area']
            else:
                print('Dica ja escolhida')
                print('Saindo do mercado de dicas')

        elif escolhida == 4:
            if 'Populacao' not in dicas:
                dicas['Populacao'] = basenormal[pais]['populacao']
            else:
                print('Dica ja escolhida')
                print('saindo do mercado de dicas')
 
        for titulo, item in dicas.items():
            print(f"{titulo} {item}")
        jogada = input("Qual será sua próxima jogada? ")    