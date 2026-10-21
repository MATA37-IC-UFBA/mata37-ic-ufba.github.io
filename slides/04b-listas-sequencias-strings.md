---
layout: remark
title:
---

{::nomarkdown}
template: inverse

# Listas, Sequências e Strings

São estruturas de dados fundamentais em python.

---

## Definições e Exemplos

### O que é uma Sequência?

* **Definição**: Uma sequência é um termo genérico para uma coleção ordenada de elementos onde cada item possui uma posição fixa (índice).

* **Características**:
  * O acesso aos elementos é feito via indexação (ex: `seq[0]`).
  * Podem ser mutáveis ou imutáveis.

* **Exemplos genéricos**: 
  * Progressões aritméticas (1, 3, 5, 7...)
  * Histórico de logs de um sistema.

---

### O que é uma Lista?

* **Definição**: Uma coleção ordenada e mutável de elementos que podem ser de tipos diferentes.

* **Características**:
  * Permite adicionar, remover e modificar elementos diretamente.
  * Dinâmica: aumenta ou diminui de tamanho automaticamente.

* **Exemplo em Python**:
  ```python
  carrinho = ["notebook", "mouse", 3, True]
  carrinho.append("teclado")  # Modificação permitida
  ```

---

### O que é uma String?

* **Definição**: Uma sequência imutável de caracteres usada para representar texto.

* **Características**:
  * Cada elemento é estritamente um caractere (letra, número, símbolo ou espaço).
  * Não pode ser alterada diretamente após a criação.

* **Exemplo em Python**:

  ```python
  mensagem = "Olá, Mundo!"
  # mensagem[0] = "o" -> Gera um erro (imutável)
  nova_mensagem = mensagem.replace("Olá", "Oi")
  ```

---

## Pontos em Comum e Diferenças

---

### Pontos em Comum

* **Ordenação**: Todos mantêm a ordem exata em que os elementos foram inseridos.

* **Indexação**: Permitem acessar itens específicos usando índices numéricos baseados em zero.

* **Fatiamento (Slicing)**: Suportam a extração de subpartes (ex: `dados[1:4]`).

* **Iterabilidade**: Podem ser percorridos facilmente usando laços de repetição (`for item in colecao:`).

---

## Tabela Comparativa

| Característica | Sequência (Conceito) | Lista | String |
| :--- | :--- | :--- | :--- |
| **Mutabilidade** | Depende do tipo | Mutável 🟢 | Imutável 🔴 |
| **Tipos de Dados** | Qualquer tipo | Heterogênea (mistos) | Apenas Caracteres |
| **Uso Principal** | Abstração teórica | Coleções dinâmicas | Textos e Mensagens |
| **Consumo de Memória**| Variável | Geralmente maior | Otimizado para texto |

---

## Recomendações de Uso

### Use Listas se:

* Os dados precisam ser **alterados, ordenados ou atualizados** frequentemente.
* Você precisa armazenar uma coleção de objetos complexos ou tipos variados.

### Use Strings se:

* O objetivo for manipulação de **texto, leitura de arquivos ou exibição de mensagens**.
* Você precisa de chaves seguras para dicionários/mapeamentos (devido à imutabilidade).

---

## Resumo de Boas Práticas

* **Imutabilidade traz segurança**: Prefira estruturas imutáveis (como strings ou tuplas) quando os dados não devem mudar, evitando bugs colaterais.

* **Evite mutação excessiva em laços**: Modificar uma lista enquanto itera sobre ela pode causar comportamentos inesperados.

* **Performance**: Para textos longos, concatenar strings repetidamente cria novos objetos na memória. Nesses casos, prefira agrupar os pedaços em uma lista e usar métodos de junção (como `.join()`).


{:/}


