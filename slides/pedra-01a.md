---
layout: remark
title: Variáveis, Constantes, Tipos de dados e Operadores
---

{::nomarkdown}
template: inverse

# Variáveis, Constantes e Tipos

{% include_relative footer.txt %}

---

# Variáveis

Variáveis são usadas para guardar informações dentro de um programa.

Uma variável possui...

- um **nome** (chamado de identificador da variável)
- um **valor** de um determinado **tipo**

O valor da variável pode mudar durante a execução do programa.

---

# Atribuição

Para **atribuir** um **valor** a uma variável, usa-se `=` 

Exemplos:

```python
>>> idade = 18
>>> x = 2 * 3
>>> y = idade + x
>>> jogador = "pedra"
>>> computador = "papel"
```

OBS.: `>>>` indica que estamos usando o modo shell. Não digite `>>>`!

---

# Identificador

O nome de uma variável (**identificador**) em Python 

- pode conter letras (A-Z, a-z), dígitos (0-9) e underscore (`_`)
- **não pode** começar com um dígito

Exemplos:

> `idade`, `jogador`, `x2`, `anoNascimento`, `mes_nascimento`, `_abc`, `PI`

--

Python diferencia maiúsculas e minúsculas nos identificadores. 
- `idade`, `Idade`, `IDADE` e `iDaDe` são 4 identificadores que representam 4 variáveis diferentes.

--

Existem palavras reservadas que não podem ser usadas para nomear variáveis, tais como `if`, `while`, entre outras.

---

# Literais

Um literal em Python é um valor fixo, constante e escrito diretamente no código fonte, 
que não muda durante a execução do programa. 
Eles representam dados primitivos, como números, texto (strings), etc.

Exemplos:

> 25, 1000, 66.67, "tesoura", "Olá, pessoal!"

---

template: inverse
# Tipos de dados

---

# Tipos

Um tipo em Python define a natureza de um dado (inteiro, real, etc.), 
determinando como ele é armazenado, processado e quais operações podem ser realizadas com tal dado. 

---

# Tipos

Os tipos de dados básicos em Python são os seguintes:

- `int` - número **inteiro** (incluindo positivos, negativos e zero). Ex.: `-5`
--

- `float` - número de **ponto flutuante** (decimal). Ex.: `3.14` (O separador decimal é o ponto)
--

- `bool` - valor **lógico** (`True` ou `False`)
--

- `str` - tipo **string** (cadeia de caracteres, texto). 
Ex.: `"papel"` (aspas duplas) ou `'papel'` (aspas simples)

--

O **tipo** determina as operações que podem ser realizadas. 

Exemplos:

- É possível subtrair números (`int` e `float`), mas não é possível subtrair strings
- Não se pode somar um inteiro a uma string

--

> Python possui outros tipos!

---

# Tipos em Python

Python usa "tipagem dinâmica" e o interpretador identifica o tipo automaticamente.

```python
>>> x = 1
```

## type()

Para saber o tipo de um valor (por exemplo, `1`) 
ou variável (por exemplo, `x`), use `type()`.

---

## type(valor)

```python
>>> type(1)  #=> class 'int'
<class 'int'>
>>> type(3.0)  #=> class 'float'
>>> type("tesoura")  #=> class 'str'
```
---

## type(variavel)

```python
>>> x = 1
>>> type(x)  #=> class 'int'
>>> y = 3.0
>>> type(y)  #=> class 'float'
>>> jogador = "tesoura"
>>> type(jogador)  #=> class 'str'
```
---

# Conversão de tipos

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
