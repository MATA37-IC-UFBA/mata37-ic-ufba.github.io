---
layout: remark
title: Tipos de dados
---

{::nomarkdown}
template: inverse

# Tipos de Dados

{% include_relative footer.txt %}

---

# Tipos

Um tipo em Python define a natureza de um dado (inteiro, real, etc.), 
determinando como ele é armazenado, processado e quais operações podem ser realizadas com tal dado. 

---

## Tipos Básicos

Os tipos de dados básicos em Python são os seguintes:

- `int` - número **inteiro** (incluindo positivos, negativos e zero). Ex.: `-5`
--

- `float` - número de **ponto flutuante** (decimal). Ex.: `3.14` (O separador decimal é o ponto)
--

- `bool` - valor **lógico** (`True` ou `False`)
--

- `str` - tipo **string** (cadeia de caracteres, texto). Ex.: `"Olá, pessoal!"` (aspas duplas) ou `'Olá, pessoal!'` (aspas simples)

--

O **tipo** determina as operações que podem ser realizadas. 

Exemplos:

- É possível subtrair números (`int` e `float`), mas não é possível subtrair strings
- Não se pode somar um inteiro a uma string

--

> Python possui outros tipos!

---

## Tipos em Python

A Python usa "tipagem dinâmica" e o interpretador identifica o tipo automaticamente.

### type(var)

Para saber o tipo de um valor ou variável (por exemplo, `x`), use `type(x)`.

--

```python
>>> type(1)  #=> class 'int'
<class 'int'>
>>> x = 1
>>> type(x)  #=> class 'int'
>>> y = 3.0
>>> type(y)  #=> class 'float'
```
---

## Conversão de tipos

Em alguns casos, pode-se converter um valor de um tipo para outro com **funções de conversão**:

- `int(valor)`
- `float(valor)`
- `bool(valor)`
- `str(valor)`

```python
x = "10"
y = 2
z = int(x) - y  # 10 - 2
```

---

# Conversão de tipos

```python
>>> x = 3
>>> float(x)   #=> 3.0
>>> str(x)     #=> "3"
>>> ano = "2001"
>>> int(ano)   #=> 2001
```

--

Na conversão de `float` para `int`, as casas decimais são descartadas.

```python
>>> x = 1.99

>>> int(x)   #=> 1
```

{:/}
