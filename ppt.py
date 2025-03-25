#Pedra papel ou tesoura
import random

respostas ={"s", "n"}
jogo = ("pedra", "papel", "tesoura")

while True:
    jpoint = 0
    cpoint = 0
    while True:
        computador = random.choice(jogo)
        jogador = input("Escolha ente pedra, papel ou tesoura").strip().lower()
        if jogador in jogo:
            print("O computador escolheu: ", computador)
            if jogador == computador:
              print("Empate")
              break
            elif (jogador == "pedra" and computador == "tesoura") or \
                 (jogador == "papel" and computador == "pedra") or \
                 (jogador == "tesoura" and computador == "papel"):
                    print("Jogador ganhou a rodada!")
                    jpoint = jpoint + 1
            else:
              print("Computador ganhou a rodada!")
              cpoint = cpoint + 1
            break
        else:
            print("Digite um das opções corretamente.")
    while True:
        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar in respostas:
            break
        print("Digite uma das opções corretamente.")

    if continuar == "n":
        print("Obrigado por usar o programa!")
        print(f"O computador fez {cpoint} pontos e você {jpoint} pontos!")
        if cpoint > jpoint:
            print("Computador venceu!!!!")
        elif cpoint == jpoint:
            print("Empate!!!")
        else:
            print("Jogador venceu!!!!")
        break