---
layout: remark
title: Variáveis, Constantes
---

{::nomarkdown}
template: inverse

# Variáveis e Constantes

{% include_relative footer.txt %}

---

## Variáveis

Variáveis são usadas para guardar informações dentro de um programa.

Uma variável possui:

- um **nome** (chamado de identificador da variável)
- um **valor** de um determinado **tipo**

O valor da variável pode mudar durante a execução do programa.

---

## Atribuição

Para **atribuir** um **valor** a uma variável, usa-se `=` 

Exemplos:

```python
>>> idade = 18

>>> x = 2 * 3

>>> y = idade + x

>>> y = y + 1
```

Lê-se: `idade` **recebe** e guarda o valor `18`

OBS.: `>>>` indica que estamos usando o modo shell. Não digite `>>>`!

---

## Atribuições compostas

Atribuições compostas modificam o valor de uma variável 
por meio de uma operação matemática. 
Elas são apenas formas mais sucintas de escrever certas atribuições. 
Usa-se `+=` (incremento), `-=` (decremento), `*=` e `/=`. 

- Exemplos

| atribuição composta |      é equivalente a       |
|---------------------|----------------------------|
| `x += 3`            | `x = x + 3`                |
| `x += y * 2`        | `x = x + y * 2`            |
| `preco -= desconto` | `preco = preco - desconto` |
| `num /= 2`          | `num = num / 2`            |
| `a *= b + 1`        | `a = a * (b + 1)`          |

---

# Constantes

Uma constante é uma variável especial cujo valor 
**não deve ser alterado** após a sua definição inicial. 

Exemplo:
```python

>>> PI = 3.14

```

Como Python não possui um mecanismo nativo para proibir 
a reatribuição de valores, utiliza-se a **convenção** 
de nomear constantes em letras maiúsculas.

---

## Identificador

O **identificador** é o  nome de uma variável ou constante em Python 

- pode conter letras (A-Z, a-z), dígitos (0-9) e underscore (`_`)
- **não pode** começar com um dígito

Exemplos:

> `idade`, `x2`, `anoNascimento`, `mes_nascimento`, `_abc`, `PI`

--

Python diferencia maiúsculas e minúsculas nos identificadores. 
Assim, `idade`, `Idade`, `IDADE` e `iDaDe` são 4 identificadores diferentes, 
que representam 4 variáveis diferentes.

--

Há **palavras reservadas** que não podem ser usadas para nomears variáveis:
- `if`, `for`, `while`, entre outras.

---

## Literais

Um literal em Python é um valor fixo, 
constante e escrito diretamente no código fonte, 
que não muda durante a execução do programa. 
Eles representam dados primitivos, como números, texto (strings), etc.

Exemplos:

> 25, 1000, 66.67, "total", "Olá, pessoal!"


{:/}
