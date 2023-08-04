#n -> total de peças
#m -> numero maximo de tirar peças
#k%(m+1) = 0 -> k=peças a tirar do lado do computador, pra sempre ganhar o jogo


#if n%(m+1) == 0: print("Você começa!")
#else: print("Computador começa!")

def verificar_peças(n):
    if n == 1:
        print("Agora resta apenas " + str(n) + "peça no tabuleiro.")
    else:
        print("Agora restam " + str(n) + " peças no tabuleiro.")

def partida():
    n = int(input("Digite o número de peças: "))
    m = int(input("Digite o número máximo de peças que se pode retirar: "))
    vitoria = 0

    if (n%(m+1) == 0):
        print("Você começa!")
        while n > 0:
            n = n - usuario_escolhe_jogada(n,m)
            usuario_ultima = True
            computador_ultima = False
            if n > 0:
                n = n - computador_escolhe_jogada(n,m)
                usuario_ultima = False
                computador_ultima = True
            verificar_peças(n)

        if(computador_ultima == True):
            print("Computador venceu!")
        elif(usuario_ultima == True):
            print("Você venceu!")
        
    else:
        print("Computador começa!")
        while n > 0:
            n = n - computador_escolhe_jogada(n,m)
            usuario_ultima = False
            computador_ultima = True
            verificar_peças(n)
            if n > 0:
                n = n - usuario_escolhe_jogada(n,m)
                usuario_ultima = True
                computador_ultima = False

        if(computador_ultima == True):
            print("Computador venceu!")
            vitoria = 0
        elif(usuario_ultima == True):
            print("Você venceu!")
            vitoria = 1
        return vitoria


def computador_escolhe_jogada(n,m):
    retirar_computador = 0
    while n%(m+1) != 0:
        n = n + retirar_computador
        retirar_computador += 1
        if retirar_computador > m:
            retirar_computador = m
        n = n - retirar_computador
    print("O computador tirou " + str(retirar_computador) + " peça(s).")
    return retirar_computador

def usuario_escolhe_jogada(n,m):
    verificar_usuario = False

    while verificar_usuario == False:
        try:
            retirar_usuario = int(input("Quantas peças você vai tirar? "))
            if retirar_usuario < 0 or retirar_usuario > m:
                print("Oops! Jogada inválida! Tente de novo.")
            else:
                verificar_usuario = True
        except:
            print("Oops! Jogada inválida! Tente de novo.")
    print("Você retirou " + str(retirar_usuario) + " peça(s)")
    return retirar_usuario

"""    while retirar_usuario < 0 or type(retirar_usuario != int):
        
        if type(retirar_usuario != int) retirar_usuario < 0 or type(retirar_usuario != int):
            print("Formato digitado inválido, tente novamente!")
        else:
            retirar_usuario = int(retirar_usuario)
    return retirar_usuario"""

def campeonato():
    k = 1
    computador_ganha = 0
    usuario_ganha = 0
    while k < 4:
        print("*** Rodada " + str(k) + " ****")
        vitoria = partida()
        if vitoria == 0:
            computador_ganha += 1
        elif vitoria == 1:
            usuario_ganha += 1
        k += 1
    print("**** Final do campeonato! ****")
    print("Placar: Você " + str(usuario_ganha) + " X " + str(computador_ganha) + " Computador")
    return 0


opcao = 0
while opcao != 1 and opcao != 2:
    try:

        opcao = int(input("Bem-vindo ao jogo do NIM! Escolha: \n1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
    except:
        print("Tente digitar novamente uma das opções listadas.")
if opcao == 1:
    partida()
elif opcao ==2:
    campeonato()