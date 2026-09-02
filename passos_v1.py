# passo 1

import random

opcoes = ["pedra", "papel", "tesoura"]

# passo 2

jogador = input("Escolha pedra, papel ou tesoura: ").lower()

if jogador not in opcoes:
    print("Jogada inválida!")

# passo 3

computador = random.choice(opcoes)
print(f"O computador escolheu: {computador}")

# passo 4

if jogador == computador:
    print("Empate!")
elif (jogador == "pedra" and computador == "tesoura") or \
     (jogador == "papel" and computador == "pedra") or \
     (jogador == "tesoura" and computador == "papel"):
    print("Você ganhou!")
else:
    print("Você perdeu!")


