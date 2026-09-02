import random

# Dicionário onde a CHAVE ganha dos VALORES da lista
REGRAS_VITORIA = {
    "pedra": ["tesoura", "lagarto"],
    "papel": ["pedra", "spock"],
    "tesoura": ["papel", "lagarto"],
    "lagarto": ["spock", "papel"],
    "spock": ["pedra", "tesoura"]
}

def determinar_vencedor(jogador, computador):
    """Retorna o resultado da rodada com as novas regras."""
    if jogador == computador:
        return "Empate"
    
    # Verifica se a escolha do computador está na lista de derrotados pelo jogador
    if computador in REGRAS_VITORIA[jogador]:
        return "Jogador"
    
    return "Computador"

def jogar():
    """Executa o loop principal do jogo com 5 opções."""
    opcoes = list(REGRAS_VITORIA.keys())
    placar_jogador = 0
    placar_computador = 0

    print("=== Pedra, Papel, Tesoura, Lagarto, Spock! ===")
    print("Digite 'sair' para encerrar.\n")

    while True:
        jogador = input("Escolha pedra, papel, tesoura, lagarto ou spock: ").lower().strip()

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

if __name__ == "__main__":
    jogar()


