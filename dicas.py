
def mercado_dicas(t,escolhida):
    print("\n")
    opcoes = []
    dicas = {}
    print('MERCADO DE DICAS:')
    print("------------------------------------------------------------")
    dicas[4] = ["Cor da Bandeira -- custa 4 tentativas",1]
    dicas[3] = ["Letra da capital - custa 3 tentativas",2]
    dicas[6] = ["Área             - custa 6 tentativas",3]
    dicas[5] = ["População        - custa 5 tentativas",4]
    dicas[7] = ["Continente       - custa 7 tentativas",5]
    dicas[0] = ["Sem dica",0]

    if "Continente: " in escolhida:
        del dicas[7]
    
    if 'Populacao: ' in escolhida:
        del dicas[5]
    
    if "Area: " in escolhida:
        del dicas[6]

    for nome, info in dicas.items():
        if t > nome:
            opcoes.append(info[1])
            print(f'{info[1]}.{info[0]}')
    print("------------------------------------------------------------")
  
    return opcoes
