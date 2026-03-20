---
layout: remark
title: Estruturas de seleção
---

{::nomarkdown}
template: inverse

# Estruturas de seleção (condicionais)

{% include_relative footer.txt %}

---

# Estruturas de seleção

As estruturas de seleção determinam, com base no valor de uma **condição** (verdadeira ou falsa)
se certas linhas de código serão executadas ou não.

Em Python, usamos as palavras-chave `if` (se), `else` (caso contrário) e `elif` (abreviação de *else if*)

---

# Seleção simples


<img src="./figs/fig-if-flow.png" alt="image" width="100%">

- Significado: se a `condicao` for verdadeira (`True`),  o `bloco de código` (sequência de instruções) é executado.

---

# if: seleção simples em Python

Do inglês, `if` significa **se**.

- Sintaxe:

```c++
if condicao:
    bloco de código
```

- Depois da condição deve vir um sinal de dois-pontos (`:`)
- A sequência de instruções deve estar indentada em relação à palavra `if` (isto é, deve estar mais à direita)

- Significado: o `bloco de código` (sequência de instruções) é executado somente se a `condicao` for verdadeira
---

# if

```python
idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Você não é adulto.")
    print("Favor trazer autorização do responsável.")
print("Programa finalizado.")
```

- Sempre que executar o programa, ele vai pedir sua idade e, ao final, sempre vai escrever `Programa finalizado.`
- Os dois primeiros `print`s, no entanto, só serão executados se você digitar um número menor que 18
- O bloco de código do `if` é delimitado pela indentação (espaços à esquerda)

Visualize a execução do código no [Python Tutor](http://pythontutor.com/visualize.html)

---

# Indentação

`Indentar` significa inserir espaços em branco no início de uma linha de texto

- Bloco de código
  - Python usa indentação para determinar onde começa e onde termina um bloco de código
     - uma sequência de linhas com a mesma indentação (mesmo número de espaços) é um bloco de código
  
- Você pode usar espaços ou tabs, mas não misture os dois no mesmo código-fonte
- Se você indentar seu código errado, o interpretador vai emitir um `IndentationError`.

```python
# ERRADO!
if 1 < 2:
print("Menor")

# ERRADO!
  if 1 < 2:
print("Menor")

# ERRADO!
if idade < 18:
    print("Você não é adulto.")
     print("Favor trazer autorização do responsável.")
```

---

# Como escrever condições

Use os operadores relacionais:

- `>` - é maior que
- `<` - é menor que
- `>=` - é maior ou igual a (não escrever `=>`)
- `<=` - é menor ou igual a (não escrever `=<`)
- `==` - é igual a (não confundir com `=`)
- `!=` - é diferente de

---

# if: Outro exemplo

Na compra de um produto, dado o seu preço unitário e o número de unidades compradas, 
imprima o valor total da compra.
Se o número de unidades for superior a 10, o cliente ganha `5%` de desconto.

---

# if: Outro exemplo

Na compra de um produto, dado o seu preço unitário e o número de unidades compradas, 
imprima o valor total da compra.
Se o número de unidades for superior a 10, o cliente ganha `5%` de desconto.

```python
preco = float(input())
quantidade = int(input())

total = preco * quantidade
if quantidade > 10:
   total *= 0.95

print(total)
```

---
 

# if: Exemplo anterior comentado

```python
# Entrada
preco = float(input())
quantidade = int(input())

# Processamento
# 1. Calcula o valor total da compra
total = preco * quantidade

# 2. Calcula o desconto
if quantidade > 10:
  total = total * 0.95

# Saída
print(total)
```

---

# if: Mais um exemplo

Escreva um programa que, dado o ano atual, o ano de nascimento da pessoa, 
e sabendo se ela já fez aniversário no ano atual, imprime a idade da pessoa.

Entrada: ano atual, ano de nascimento, e a string `S` (se já fez aniversário no ano atual) ou `N` (caso contrário).

```python
# Entrada
ano_atual = int(input())
ano_nascimento = int(input())
nao_fez_aniversario = (input() == "N") # variável do tipo Bool

# Processamento
idade = ano_atual - ano_nascimento
if nao_fez_aniversario:
    idade = idade - 1

# Saída
print(idade)
```

---

# if

Considere agora o seguinte programa:

```python
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é adulto.")
if idade < 18:
    print("Você não é adulto.")
```

Note que as condições são complementares. 
Nesse caso, pode-se usar a estrutura `if-else`.

---

# if-else: seleção de dois ramos

Do inglês, `else` significa "senão", "caso contrário". O `else` nunca aparece sozinho; ele é parte da estrutura if-else.

Sintaxe:

```c++
if condicao:
    bloco1
else:
    bloco2
```

Semântica: se a `condicao` for verdadeira (True), executa `bloco1`; se for falsa (False), executa `bloco2`

---

# if-else

Exemplo:

```python
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é adulto.")
else:
    print("Você não é adulto.")
print("Fim")
```

---

# ifs aninhados

```python
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é adulto.")
else:
    if idade >= 12:
        print("Você é adolescente.")
    else:
        print("Você é criança.")
print("Fim")
```

---

# if-elif

Sintaxe:

```python
if cond1:
    bloco1
elif cond2:
    bloco2
elif condN:
    blocoN
else:     # o else é opcional
    blocoM   
```

Semântica: Executa o `bloco1` se a condição `cond1` for verdadeira; caso contrário, executa `bloco2` se a condição `cond2` for verdadeira, e assim por diante. Se todas as condições `cond1`...`condN` forem falsas, executa `blocoM`.

OBS.: Nessa estrutura, executa-se *apenas* o bloco de código que corresponde à *primeira* condição verdadeira (de cima pra baixo).

---

# if-elif

```python
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é adulto.")
elif idade >= 12:
    print("Você é adolescente.")
else:
    print("Você é criança.")
print("Fim")
```

---

# if-elif

Exemplo:

```python
nota = float(input())
if nota > 9.0:
    print("Excelente!")
elif nota > 7.0:
    print("Muito bom!")
elif nota > 5.0:
    print("Razoável!")
else:
    print("Estude mais!")
```

---

template: inverse

# Expressões lógicas (booleanas)

---

# Expressões lógicas

Uma `condição` usada no `if` ou no `else-if` é uma *expressão lógica*, isto é, 
uma expressão que retorna um valor do tipo `bool` -- *verdadeiro* (`True`) ou *falso* (`False`)

- Uma expressão que usa *operadores relacionais*  retorna um valor do tipo `bool` (`True` ou `False`)
   - `x > 10` 

- Uma expressão que usa *operadores lógicos* (_and_, _or_, _not_) retorna um valor do tipo `bool` (`True` ou `False`)
   - `(a > 0) and (a < 5)`

---

# Operadores relacionais

Um operador relacional é usado para fazer comparações entre os valores de duas expressões:

- `>` - é maior que
- `<` - é menor que
- `>=` - é maior ou igual a (não escrever `=>`)
- `<=` - é menor ou igual a (não escrever `=<`)
- `==` - é igual a (não confundir com `=`)
- `!=` - é diferente de

---

# Operadores relacionais

Exemplo:

```python
x = int(input())
if x > 0:            # greater than
  print("Positivo")
elif x < 0:          # less than
  print("Negativo")
if x % 2 == 1:       # equal
  print("Ímpar")
```

---

# Operadores lógicos

O operador lógico é usado para combinar expressões lógicas:

- `not` - não (negação)
- `and` - e (conjunção lógica)
- `or` - ou (disjunção lógica)

A ordem de precedência, da maior para menor, é:  `not`, `and`, `or`

Exemplo:

```python
x = int(input())
if not (x <= 0) and (x % 2 == 1): # operação `not` primeiro
  print("Positivo impar")
```

---

# Operadores lógicos

Exemplo:

```python
x, y = input().split()
x = int(x)
y = int(y)
# operação `and` é realizada antes de `or`
if y == 1 or x > 0 and x < 5: 
  print("Ok")
```

Por causa das regras de precedência, a expressão é equivalente a `(y == 1) or (x > 0 and x < 5)`.

---

# Avaliação em curto-circuito

Ao computar o resultado de uma expressão lógica com operadores `and` e `or`, o interpretador só avalia as subexpressões se necessário.

- `A and B`: se A for falso, a expressão B não é avaliada pois, qualquer que seja seu valor, a expressão `A and B` é falsa
- `A or B`: se A for verdadeiro, a expressão B não é avaliada pois, qualquer que seja seu valor, a expressão `A or B` é verdadeira

---

# Exemplo: obrigatoriedade de votação

```python
# Programa que lê a idade de uma pessoa e mostra uma mensagem
# indicando a possibilidade e obrigatoriedade do voto
#
# Menor de 18 anos: Não vota
# 16 ou 17 anos: Voto facultativo
# 18 a 69 anos: Voto obrigatório
# 70 anos ou maior: Voto facultativo

idade = int(input())
if idade >= 16:
  if idade >= 18 and idade <= 70:
    print("Voto obrigatório")
  else:
    print("Voto facultativo")
else:
    print("Não pode votar")
```

{:/}
