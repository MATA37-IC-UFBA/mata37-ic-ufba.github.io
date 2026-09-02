# programa pedra, papel e tesoura

import random
opcoes = ["pedra", "papel", "tesoura"]

jogador = input("Escolha pedra, papel ou tesoura: ").lower()
if jogador not in opcoes:
    print("Jogada inválida!")

computador = random.choice(opcoes)
print(f"O computador escolheu: {computador}")

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você ganhou!")
else:
    print("Você perdeu!")

# Coloque tudo dentro de um loop while True para jogar quantas vezes quiser até decidir sair.

