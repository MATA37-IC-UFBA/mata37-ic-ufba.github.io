---
layout: remark
title:
---

{::nomarkdown}
template: inverse

# Funções em Python

{% include_relative footer.txt %}

---

<img src="./figs-function/Funcoes-01.png" width="100%">

---
## Funções simples 

<img src="./figs-function/Funcoes-02.png" width="100%">

---
<img src="./figs-function/Funcoes-03.png" width="100%">

---
## Funções com parâmetros

<img src="./figs-function/Funcoes-04.png" width="100%">

---
<img src="./figs-function/Funcoes-05.png" width="100%">

---
<img src="./figs-function/Funcoes-06.png" width="100%">

---
## Funções que retornam um valor

<img src="./figs-function/Funcoes-07.png" width="100%">

---
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


