def choose_game():

    from forca import hangman_game
    from jogoAdivinhacao2 import guess_game

    print("\n******************************")
    print("******Escolha o seu jogo******")
    print("******************************\n")

    print("(1) para Jogo da forca ou (2) para Jogo da adivinhação")
    jogo_escolhido = int(input("Informe o jogo desejado: "))

    while jogo_escolhido != 1 and jogo_escolhido != 2:
        jogo_escolhido = int(input("\nJogo não encontrado. Insira o número do jogo que deseja jogar: "))

    if jogo_escolhido == 1:
        print("Jogando jogo da forca!!")
        hangman_game()

    elif jogo_escolhido == 2:
        print("Jogando jogo da adivinhação")
        guess_game()


if __name__ == "__main__":
    choose_game()
