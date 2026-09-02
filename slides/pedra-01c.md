---
layout: remark
title: Entrada e Saída
---

{::nomarkdown}
template: inverse

# Entrada e Saída de Dados

{% include_relative footer.txt %}

---

# Entrada e Saída

Instruções de entrada e instruções de saída 
permitem a comunicação entre o programa e informações externas a ele.

Como **ler do teclado (entrada)**? Como  **escrever na tela (saída)**?

- Saída de dados: `print()`
- Entrada de dados: `input()`

---

# Saída de dados: `print`

- Para exibir (imprimir) um valor na tela, 
use a instrução `print(x)`, substituindo `x` pela expressão cujo resultado deve ser exibido.

Exemplos:

```python
print(5)
print(3.14 / 2)
print("O computador escolheu: papel")
```

---

# Imprimindo com número definido de casas decimais

- Para imprimir um valor com um determinado número de casas decimais, 
converta-o para string usando `f-strings`.

Exemplo:

```python
total = 1 / 7         #=> 0.14285714285714285
print(f'{total:.2f}') #=> 0.14
print(f'{total:.5f}') #=> 0.14286
```

---

# Imprimindo múltiplos valores na mesma linha

- Para exibir dois ou mais valores usar `f-strings` também.

Exemplo:

```python
a = 1
b = 2
c = 3
print(f'{a} {b} {c}') #=> 1 2 3
```

---

# Imprimindo múltiplos valores na mesma linha

Você pode passar para o `print` diversas expressões separadas por vírgulas. 

Exemplo:

```python
idade = 18
print("Eu tenho", idade, "anos")
```

Na saída, as expressões ficam separadas por um **espaço em branco**. 
Se quiser remover essa separação, adicione `sep=""`:

```python
ddd = 71
telefone = "5555-5555"
print("(", ddd, ") ", telefone, sep="")
```

---

# Evitando a quebra de linha

A princípio cada `print` escreve uma linha de texto. Exemplo:

```python
print("Oi, ")
print("pessoal!")
```

--

Se você quiser evitar a quebra de linha, use `end=""`. Exemplo:

```python
print("Oi, ", end="")
print("pessoal!")
```

---

template: inverse
# Entrada de dados
---

# Entrada: input()

- `input()` lê tudo o que o usuário digita até apertar *Enter* e retorna o texto digitado como uma string.

Exemplo:

```python
print("Qual é o seu nome?")
nome = input()
print("Oi", nome)
```

---
template: exercise
# Exemplo com input()

Qual a saída do programa a seguir, considerando como entradas os números 2 e 3?

```python
print("Digite o primeiro número:")
a = input()
print("Digite o segundo número:")
b = input()
print("Soma:", a + b)
```

--

O comando `input` sempre retorna uma string! 
Se necessário, você deve converter para o tipo desejado.

---

# Exemplo com input()

```python
print("Digite o primeiro número:")
a = float(input())
print("Digite o segundo número:")
b = float(input())
print("Soma:", a + b)
```

---

# Outro exemplo com input()

Programa que lê um número inteiro e imprime seu dobro:

```python
numero = int(input())
print(numero * 2)
```

---

# Lendo diversos valores na mesma linha

Programa que lê uma linha com três números inteiros, separados por espaço, e mostra a soma dos números:

```python
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
print(a + b + c)
```

--

- `split()` quebra uma _string_ em substrings, com base no delimitador  *espaço em branco*.

```
"1 2 3".split() # retorna ['1','2','3']
```

- No exemplo, deve-se converter cada substring para `int` antes de fazer a soma.

---

# Split() quebra uma _string_ em substrings

- `split()` considera um separador ou delimitador (pode ser diferente de *espaço em branco*).

Exemplo:
Programa que divide `cadeia` em duas substrings, considerando o caractere '.'

```python
>>> cadeia = "45.09"
>>> inteiro, decimal = cadeia.split('.')
>>> print(inteiro, decimal)  #=> 45 09
```

---

# Map() aplica uma função a elementos de uma lista.


```python
a, b, c = map(int,input().split())
print(a + b + c)
```

{:/}

