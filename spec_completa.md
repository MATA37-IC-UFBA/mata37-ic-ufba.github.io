## Especificação Técnica do Jogo

Esta especificação define o comportamento e as regras do jogo Pedra, Papel, Tesoura, Lagarto, Spock para implementação e validação do sistema.

## 1. Visão Geral

O programa é um jogo de console baseado em turnos. 
O usuário joga contra o computador. 
O sistema deve validar a entrada do usuário, 
gerar uma escolha aleatória para o computador, 
determinar o vencedor da rodada com base nas regras estabelecidas 
e manter um placar acumulativo até que o usuário decida encerrar.

## 2. Regras de Negócio (Matriz de Decisão)

A tabela abaixo define o resultado do ponto de vista do Jogador,
comparando a sua escolha (Entrada Jogador) com a escolha da máquina (Entrada Computador).

| Entrada Jogador | Entrada Computador | Resultado Espetado (Saída) | Texto Explicativo Exibido |
|---|---|---|---|
| Qualquer uma | Igual à do jogador | Empate | "Empate nesta rodada!" |
| pedra | tesoura / lagarto | Jogador | "Você ganhou esta rodada!" |
| pedra | papel / spock | Computador | "O computador ganhou esta rodada!" |
| papel | pedra / spock | Jogador | "Você ganhou esta rodada!" |
| papel | tesoura / lagarto | Computador | "O computador ganhou esta rodada!" |
| tesoura | papel / lagarto | Jogador | "Você ganhou esta rodada!" |
| tesoura | pedra / spock | Computador | "O computador ganhou esta rodada!" |
| lagarto | spock / papel | Jogador | "Você ganhou esta rodada!" |
| lagarto | pedra / tesoura | Computador | "O computador ganhou esta rodada!" |
| spock | pedra / tesoura | Jogador | "Você ganhou esta rodada!" |
| spock | papel / lagarto | Computador | "O computador ganhou esta rodada!" |

------------------------------
## Tabela de Cenários de Testes (Entradas e Saídas)
Esta tabela serve como guia para a criação de testes de caixa preta (manuais ou automatizados), 
cobrindo fluxos normais, exceções e encerramento.

| ID | Tipo de Fluxo | Entrada do Jogador (input) | Escolha do Computador (random) | Saída Esperada no Console / Comportamento |
|---|---|---|---|---|
| TC-01 | Fluxo Normal (Vitória) | "spock" | "pedra" | Exibe vitória do jogador e soma +1 no placar dele. |
| TC-02 | Fluxo Normal (Derrota) | "papel" | "tesoura" | Exibe vitória do computador e soma +1 no placar dele. |
| TC-03 | Fluxo Normal (Empate) | "lagarto" | "lagarto" | Exibe mensagem de empate. Placar não se altera. |
| TC-04 | Caixa Alta (Normalização) | "SPOCK" | "tesoura" | Converte para "spock". Registra vitória do jogador. |
| TC-05 | Espaços em Branco | " pedra " | "lagarto" | Remove espaços (.strip()). Registra vitória do jogador. |
| TC-06 | Entrada Inválida | "fogo" | (Não avaliado) | Exibe "Opção inválida! Tente novamente.". Pede nova entrada. |
| TC-07 | Entrada Vazia | "" | (Não avaliado) | Exibe "Opção inválida! Tente novamente.". Pede nova entrada. |
| TC-08 | Encerramento | "sair" | (Não avaliado) | Encerra o loop do jogo. Exibe o placar final e para a execução. |

------------------------------
## Requisitos de Sistema

* Interface: Linha de comando (CLI).
* Case Sensitivity: O sistema deve aceitar entradas em maiúsculo ou minúsculo e tratá-las de forma idêntica.
* Robustez: Entradas inválidas não podem quebrar ou fechar o programa de forma abrupta; o sistema deve exibir uma mensagem de erro amigável e solicitar uma nova jogada.
* Persistência de Dados: O placar deve se manter ativo na memória enquanto o programa estiver rodando.

