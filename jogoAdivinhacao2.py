def guess_game():
    from random import randint

    iniciando_jogo()

    numero_secreto = randint(1, 100)
    numero_tentativas = 0
    total_pontos = 1000

    numero_tentativas_loop = escolha_dificuldade()

    for rodada in range(1, numero_tentativas_loop + 1):

        print(f'\nRodada {rodada} de {numero_tentativas_loop}:')

        chute_usuario = int(input("Digite um número entre 1 e 100: "))

        print(f'Voce digitou o número: {chute_usuario}')

        if (chute_usuario < 1 or chute_usuario > 100):
            print("Você deve digitar um número entre 1 e 100!!")
            continue

        acertou = (chute_usuario == numero_secreto)
        chute_foi_maior = (chute_usuario > numero_secreto)
        chute_foi_menor = (chute_usuario < numero_secreto)

        if (acertou):
            print(f"Parabéns!!! Você acertou e fez {total_pontos} pontos =)")
            break
        else:
            if (chute_foi_maior):
                print("O número informado é maior que o número secreto =(")
                if (rodada == numero_tentativas):
                    print(f'O número secreto era: {numero_secreto}')
                    print(f'Você fez {total_pontos} pontos')

            elif (chute_foi_menor):
                print("O número informado é menor que o número secreto =(")
                if (rodada == numero_tentativas):
                    print(f'O número secreto era: {numero_secreto}')
                    print(f'Você fez {total_pontos} pontos')

            pontos_perdidos = abs(numero_secreto - chute_usuario)
            total_pontos = (total_pontos - pontos_perdidos)

    print("\nFim de Jogo")

def iniciando_jogo():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def escolha_dificuldade():
    dificuldade = input("Informe a dificuldade desejada: (1) Facil, (2) Medio, (3) Difícil: ").lower().strip()

    confirmacao_dificuldade = ("1", "2", "3", "facil", "medio", "dificil")

    while (dificuldade not in confirmacao_dificuldade):
        dificuldade = input("Dificuldade não encontrada. Insira uma dificuldade válida: ")

    dificuldade_facil = dificuldade == "1" or dificuldade == "facil"
    dificuldade_media = dificuldade == "2" or dificuldade == "medio"
    dificuldade_dificil = dificuldade == "3" or dificuldade == "dificil"

    if (dificuldade_facil):
        print(f"\nDificuldade escolhida: Facil")
    else:
        if (dificuldade_media):
            print(f"\nDificuldade escolhida: Média")
        elif (dificuldade_dificil):
            print(f"\nDificuldade escolhida: Difícil")

    if dificuldade_facil:
        numero_tentativas = 20
    elif dificuldade_media:
        numero_tentativas = 10
    elif dificuldade_dificil:
        numero_tentativas = 5

    return numero_tentativas

def jogar_novamente():
    jogar_novamente = input("Deseja jogar novamente? (S/N)\n").upper()

    confirmacao = ["SIM", "S"]
    negacao = ["N", "NAO"]

    while jogar_novamente not in confirmacao and jogar_novamente not in negacao:
        print("Comando inválido")
        jogar_novamente = input("Deseja continuar jogando? (S/N) ").upper()

    if jogar_novamente in confirmacao:
        print("\n")
        guess_game()
    if jogar_novamente in negacao:
        print("Encerrando jogo da Adivinhação")


if(__name__ == "__main__"):
    guess_game()
