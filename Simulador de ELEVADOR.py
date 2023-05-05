import time

piso0 =0
piso =piso0

while True:
    escolha_piso = int(input("\nEscolha o piso? "))
    if escolha_piso >= 12:
        while escolha_piso >= 11:
            print("O Prédio só tem 11 andares!")
            escolha_piso = int(input("Escolha o piso? "))
    if piso == escolha_piso:
        print("\nEstá no mesmo piso que escolheu")
        #  1 < 5
    elif escolha_piso < piso:
        print("Porta a Fechar")
        time.sleep(1)
        print("Vai começar a Descer!")
        for cont in range(piso,escolha_piso-1,-1):
            time.sleep(1)
            print(cont)
        piso = escolha_piso
        print("Porta a Abrir")
        # 5 > 1
    elif escolha_piso > piso:
        print("Porta a Fechar")
        time.sleep(1)
        print("Vai começar a subir!")
        for cont in range(piso, escolha_piso + 1):
            time.sleep(1)
            print(cont)
        piso = escolha_piso
        print("Porta a Abrir")
    else:
        print("Erro!")