---
layout: remark
title:
---

{::nomarkdown}
template: inverse


# Tuplas em Python

Estrutura de dados sequencial e imutável.

### O que é uma Tupla?

* **Definição**: Uma tupla é uma coleção de elementos ordenada e imutável.

* **Sintaxe**: Utiliza parênteses () para delimitar os elementos, separados por vírgula.

* **Casos de uso**: Ideal para dados que não devem ser alterados ao longo do programa (ex: coordenadas, configurações, dados de cadastro estáveis).

### Características Principais

* **Imutabilidade**: Uma vez criada, você não pode adicionar, remover ou alterar elementos.

* **Ordenada**: Mantém a ordem de inserção dos elementos.

* **Heterogênea**: Pode armazenar diferentes tipos de dados na mesma estrutura.

* **Indexada**: Permite acesso aos elementos através de índices (começando em 0).

### Criação de tuplas

python

# Tupla vazia
tupla_vazia = ()

# Tupla com múltiplos tipos de dados
coordenadas = (-23.5505, -46.6333, "São Paulo")

# ATENÇÃO: Tupla com um único elemento (requer vírgula)
tupla_unitaria = (42,)

### Acesso a elementos

O acesso funciona exatamente como nas listas, utilizando colchetes. 

python

cores = ("Vermelho", "Verde", "Azul")

print(cores[0])   # Saída: Vermelho
print(cores[-1])  # Saída: Azul (último elemento)

Use o código com cuidado.

### A Prova da Imutabilidade

Se tentarmos alterar um elemento, o Python retornará um erro do tipo TypeError. 

python

dimensoes = (1920, 1080)

# Isto vai gerar um erro:
dimensoes[0] = 2560
# TypeError: 'tuple' object does not support item assignment

Use o código com cuidado.

### Operações Comuns: Desempacotamento

Você pode extrair os valores de uma tupla diretamente para variáveis. 

python

dados_cliente = ("Ana Silva", 28, "Engenheira")

# Desempacotando a tupla

nome, idade, profissao = dados_cliente

print(nome)       # Saída: Ana Silva
print(idade)      # Saída: 28

Use o código com cuidado.

### Métodos Disponíveis

Por serem imutáveis, as tuplas possuem apenas dois métodos nativos: 

* count(valor): Conta quantas vezes um elemento aparece.
* index(valor): Retorna o índice da primeira ocorrência do elemento.

python

numeros = (1, 2, 3, 1, 4, 1)

print(numeros.count(1))  # Saída: 3
print(numeros.index(4))  # Saída: 4


### Resumo: Lista vs Tupla

CaracterísticaLista ([])Tupla (())
**Mutabilidade**
Mutável (Pode alterar)Imutável (Não altera)
**Performance**
Mais lentaMais rápida (Otimizada)
**Tamanho em Memória**
MaiorMenor
**Propósito**
Coleções dinâmicasDados fixos, constantes

{:/}

