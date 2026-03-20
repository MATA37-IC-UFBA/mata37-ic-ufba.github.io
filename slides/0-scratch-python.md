---
layout: remark
title: Introdução à Programação com Python
---

{::nomarkdown}
template: inverse

# Exemplos

{% include_relative footer.txt %}

---

# Desenhar quadrado

- 4 lados, todos com mesmo comprimento
- Ângulos internos: 90 graus


## Algoritmo

- vá para uma posição central no papel
- coloque a caneta sobre o papel
- risque 2cm
- gire 90 graus
- risque 2cm
- gire 90 graus
- risque 2cm
- gire 90 graus
- risque 2cm
- gire 90 graus


---

# Scratch IDE

<img src="./figs/scratch-ide.png" width="100%">

---

# Desenhar Quadrado (1)

<img src="./figs/scratch2.png" width="30%">

---

# Desenhar Quadrado (2)


<img src="./figs/scratch1.png" width="40%">

---

# Desenhar Quadrado (3)

<img src="./figs/scratch-cat.png" width="80%">


---


# Desenhar Quadrado com Turtle (1)

```python
from turtle import *

home()
setx(-100)
sety(50)
clearscreen()
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
x = input()
```

---

# Desenhar Quadrado com Turtle (2)

```python
from turtle import *

home()
setx(-100)
sety(50)
clearscreen()
for i in range(4):
   right(90)
   forward(100)
x = input()
```

{:/}
