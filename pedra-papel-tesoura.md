Aqui está o passo a passo para construir o jogo Pedra, Papel e Tesoura no terminal:

## Estrutura do Jogo
O projeto pode ser dividido em 5 etapas principais:

   1. Importar a biblioteca: Usar o módulo random para a escolha do computador.
   2. Pegar a escolha do jogador: Receber a entrada de texto e padronizar.
   3. Gerar a escolha do computador: Sortear aleatoriamente entre pedra, papel ou tesoura.
   4. Comparar as escolhas: Aplicar as regras do jogo usando condicionais (if/elif/else).
   5. Criar o loop do jogo: Permitir que o usuário jogue múltiplas rodadas.

------------------------------
## Passo a Passo do Código## Passo 1: Importação e Configuração
Importe o módulo necessário e crie uma lista com as opções válidas.

import random
opcoes = ["pedra", "papel", "tesoura"]

## Passo 2: Entrada do Usuário
Peça a jogada do usuário. Use .lower() para evitar erros com letras maiúsculas.

jogador = input("Escolha pedra, papel ou tesoura: ").lower()
if jogador not in opcoes:
    print("Jogada inválida!")

## Passo 3: Jogada do Computador
Use random.choice() para o computador escolher um item da lista de forma justa.

computador = random.choice(opcoes)
print(f"O computador escolheu: {computador}")

## Passo 4: Lógica de Vitória
Compare as duas escolhas para determinar o resultado da rodada.

if jogador == computador:
    print("Empate!")elif (jogador == "pedra" and computador == "tesoura") or \     (jogador == "papel" and computador == "pedra") or \     (jogador == "tesoura" and computador == "papel"):
    print("Você ganhou!")else:
    print("Você perdeu!")

## Passo 5: Criar o Loop Principal (Opcional)

Coloque tudo dentro de um loop while True para jogar quantas vezes quiser até decidir sair.

