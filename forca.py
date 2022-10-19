def hangman_game():

    iniciacao_jogo()

    palavra_secreta = escolhendo_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(f'\n{letras_acertadas}\n')

    while (not enforcou and not acertou):

        chute = solicitar_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            print(f'Você tem {7 - (erros + 1)} tentativas restantes')
            erros += 1
            desenha_forca(erros)


        acertou = ("" not in letras_acertadas)
        enforcou = erros == 7

        if (enforcou):
            break
        if (acertou):
            break

        print(f'{letras_acertadas}\n')

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim de jogo")

    jogar_novamente()

def iniciacao_jogo():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def escolhendo_palavra_secreta():
    from random import randrange
    arquivo = open("texto.txt", "r")

    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["" for letra in palavra]

def solicitar_chute():
    chute_usuario = input("Insira uma letra: ").strip().upper()
    return chute_usuario

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if letra == chute:
            letras_acertadas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()

def imprime_mensagem_perdedor(palavra_secreta):
    print(f"Que pena você foi enforcado!!")
    print(f"A palavra secreta era: {palavra_secreta.capitalize()}")
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def jogar_novamente():
    jogar_novamente = input("Deseja jogar novamente? (S/N)\n").upper()

    confirmacao = ["SIM", "S"]
    negacao = ["N", "NAO"]

    while jogar_novamente not in confirmacao and jogar_novamente not in negacao:
        print("Comando inválido")
        jogar_novamente = input("Deseja continuar jogando? (S/N) ").upper()

    if jogar_novamente in confirmacao:
        print("\n")
        hangman_game()
    if jogar_novamente in negacao:
        print("Encerrando jogo da forca")


if (__name__ == "__main__"):
    hangman_game()