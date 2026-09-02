## Especificação Técnica do Jogo

Esta especificação define o comportamento e as regras do jogo Pedra, Papel e Tesoura para implementação e validação do sistema.

## 1. Visão Geral

O programa é um jogo de console.
O usuário joga contra o computador. 
O sistema deve validar a entrada do usuário, 
gerar uma escolha aleatória para o computador, 
determinar o vencedor da rodada com base nas regras estabelecidas.

## 2. Regras de Negócio (Matriz de Decisão)

A tabela abaixo define o resultado do ponto de vista do Jogador,
comparando a sua escolha (Entrada Jogador) com a escolha da máquina (Entrada Computador).

| Entrada Jogador | Entrada Computador | Resultado Espetado (Saída) | Texto Explicativo Exibido |
|---|---|---|---|
| Qualquer uma | Igual à do jogador | Empate | "Empate!" |
| pedra | tesoura | Jogador | "Você ganhou!" |
| pedra | papel | Computador | "O computador!" |
| papel | pedra | Jogador | "Você ganhou!" |
| papel | tesoura | Computador | "O computador ganhou!" |
| tesoura | papel | Jogador | "Você ganhou!" |
| tesoura | pedra | Computador | "O computador ganhou!" |

------------------------------
## Tabela de Cenários de Testes (Entradas e Saídas)

Esta tabela serve como guia para a criação de testes de caixa preta (manuais ou automatizados), 
cobrindo fluxos normais e exceções.

| ID | Tipo de Fluxo | Entrada do Jogador (input) | Escolha do Computador (random) | Saída Esperada no Console / Comportamento |
|---|---|---|---|---|
| TC-01 | Fluxo Normal (Vitoria) | "tesoura" | "papel" | Exibe vitória do jogador. |
| TC-02 | Fluxo Normal (Derrota) | "papel" | "tesoura" | Exibe vitória do computador. |
| TC-03 | Fluxo Normal (Empate) | "pedra" | "pedra" | Exibe mensagem de empate. |
| TC-04 | Caixa Alta (Normalização) | "PEDRA" | "tesoura" | Converte para "pedra". Exibe vitória do jogador. |
| TC-05 | Espaços em Branco | " pedra " | "tesoura" | Remove espaços (.strip()). Exibe vitória do jogador. |
| TC-06 | Entrada Inválida | "fogo" | (Não avaliado) | Exibe "Opção inválida!". |
| TC-07 | Entrada Vazia | "" | (Não avaliado) | Exibe "Opção inválida!". |

------------------------------
## Requisitos de Sistema

* Interface: Linha de comando (CLI).
* Case Sensitivity: O sistema deve aceitar entradas em maiúsculo ou minúsculo e tratá-las de forma idêntica.
* Robustez: Entradas inválidas não podem quebrar ou fechar o programa de forma abrupta; o sistema deve exibir uma mensagem de erro amigável.

