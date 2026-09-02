import random

def determinar_vencedor(jogador, computador):
    """Retorna o resultado da rodada com base nas escolhas."""
    if jogador == computador:
        return "Empate"
    
    # Condições onde o jogador ganha
    if (jogador == "pedra" and computador == "tesoura") or \
       (jogador == "papel" and computador == "pedra") or \
       (jogador == "tesoura" and computador == "papel"):
        return "Jogador"
    
    return "Computador"

def jogar():
    """Executa o loop principal do jogo no terminal."""
    opcoes = ["pedra", "papel", "tesoura"]
    placar_jogador = 0
    placar_computador = 0

    print("=== Bem-vindo ao Pedra, Papel e Tesoura! ===")
    print("Digite 'sair' a qualquer momento para encerrar.\n")

    while True:
        jogador = input("Escolha pedra, papel ou tesoura: ").lower().strip()

        if jogador == "sair":
            print("\nObrigado por jogar!")
            print(f"Placar Final - Você: {placar_jogador} | Computador: {placar_computador}")
            break

        if jogador not in opcoes:
            print("Opção inválida! Tente novamente.\n")
            continue

        computador = random.choice(opcoes)
        print(f"O computador escolheu: {computador}")

        resultado = determinar_vencedor(jogador, computador)

        if resultado == "Empate":
            print("Empate nesta rodada!\n")
        elif resultado == "Jogador":
            print("Você ganhou esta rodada!\n")
            placar_jogador += 1
        else:
            print("O computador ganhou esta rodada!\n")
            placar_computador += 1

        print(f"Placar atual - Você: {placar_jogador} | Computador: {placar_computador}\n")

# Garante que o jogo só roda se o arquivo for executado diretamente
if __name__ == "__main__":
    jogar()


