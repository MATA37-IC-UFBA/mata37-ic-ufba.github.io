---
layout: remark
title:
---

{::nomarkdown}
template: inverse

# Funções em Python

{% include_relative footer.txt %}

---
## Funções

Funções são blocos de código que podem ser chamados em outros pontos do programa. 

- Na `chamada de função` (_function call_), a execução prossegue no primeiro comando
de seu bloco de código.

- Na chamada de função, pode-se passar valores para uso durante sua execução. 

- Ao final de sua execução, a função pode retornar um valor
e o controle retorna para o `chamador` (_caller_).

Python fornece várias funções prontas para serem usadas: input(), sqrt(), len(), int()... 

---

## Exemplos de chamada de função

- Chamada de Funções pré-definidas

```python
>>> x = sqrt(9)
>>> len([0,1,2,3,4])
>>> int(2.0)
```

- Bibliotecas de funções
   - uso de `import`

```python
import random

random.randint(0, 60) 
```

---
## Funções simples 

### Programa (sem funções)

<img src="./figs-function/Funcoes-02.png" width="100%">

---
### Função definida pelo programador

<img src="./figs-function/Funcoes-03.png" width="100%">

---
## Funções com parâmetros

- Impressão do título pode ser definida como função.
- Nome da seção do cardápio pode ser passado na chamada da função.

<img src="./figs-function/Funcoes-04.png" width="100%">

---
## Função imprimeTitulo(texto)

<img src="./figs-function/Funcoes-05.png" width="100%">

---
<img src="./figs-function/Funcoes-06.png" width="100%">

---
## Funções que retornam um valor

<img src="./figs-function/Funcoes-07.png" width="100%">

---
# Função preco_grande(preco)

<img src="./figs-function/Funcoes-08.png" width="100%">

---

## Outros exemplos

<img src="./figs-function/Funcoes-09.png" width="100%">

---
<img src="./figs-function/Funcoes-10.png" width="100%">

---
<img src="./figs-function/Funcoes-11.png" width="100%">

---

## Variáveis locais


`Variáveis locais` a uma função são
as variáveis definidas no corpo de tal função 
e só podem ser acessadas pelo código interno à função.

<img src="./figs-function/Funcoes-12.png" width="95%">

[Rode o exemplo](https://pythontutor.com/visualize.html).

---

## Variáveis globais

`Variáveis globais` de um programa são aquelas definidas fora de todas as funções.
- O valor de uma variável global pode ser acessado dentro do corpo de qualquer função.

<img src="./figs-function/Funcoes-13.png" width="95%">

---

## Variáveis globais

O valor de uma variável global `não pode ser modificado` em uma função Python,
exceto se a mesma for declarada como `global` no corpo da função.

<img src="./figs-function/Funcoes-14.png" width="95%">

[Rode o exemplo](https://pythontutor.com/visualize.html).

---

## Sobre o uso de variáveis globais

Usar variáveis globais é muitas vezes considerado **má prática de programação**.

- Em geral, recomenda-se passar valores como parâmetros e receber valores como retorno da função.

Se `uma função não usa variáveis globais`, 
a chamada da função contém as informações necessárias 
para tratá-la como módulo independente e `caixa-preta` (black box).

Se `uma função usa variáveis globais`, 
é necessário conhecer melhor a função, as variáveis globais que ela usa 
e as que pode alterar.


{:/}


