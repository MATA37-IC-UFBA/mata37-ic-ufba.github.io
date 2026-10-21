---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundColor: #f5f5f5
color: #333
---

# Números Complexos em Python
## Aplicações Práticas na Física e Engenharia

---

# O que é o tipo `complex`?

O Python possui suporte nativo para números complexos. Eles representam valores que possuem uma **parte real** e uma **parte imaginária**.

* **Sintaxe:** Utiliza a letra `j` (ou `J`) para indicar a unidade imaginária (convenção da Engenharia Elétrica).
* **Criação direta:** `z = 3 + 4j`
* **Função construtora:** `z = complex(3, 4)`

> **Nota:** Se a parte imaginária for `1`, escreva `1j` (apenas `j` causará erro de variável indefinida).

---

# Estrutura e Atributos Básicos

Todo objeto `complex` possui propriedades embutidas para acessar suas componentes e métodos para manipulação matemática.

```python
z = 2.5 - 7j

print(z.real)       # Saída: 2.5 (float)
print(z.imag)       # Saída: -7.0 (float)
print(z.conjugate())# Saída: (2.5+7j)
print(abs(z))       # Calcula o Módulo (Magnitude)
```

⚠️ **Restrição:** Operadores de ordenação como `>`, `<`, `>=`, `<=` **não funcionam** com números complexos (`TypeError`).

---

# Por que usar na Física?

Fenômenos ondulatórios e oscilações são modelados por senos e cossenos. Através da **Identidade de Euler**:

\[e^{j\theta} = \cos\theta + j\sin\theta\]

Transformamos equações diferenciais trigonométricas complexas em **exponenciais complexas**. Isso reduz operações algébricas pesadas a simples somas e multiplicações de fasores.

---

# Exemplo 1: Circuitos Elétricos AC

Em circuitos de corrente alternada, a oposição total à corrente é a **Impedância (\(Z\))**:
* \(\text{Parte Real (Z.real)} \rightarrow\) Resistência pura (\(R\))
* \(\text{Parte Imaginária (Z.imag)} \rightarrow\) Reatância (\(X\))

---

# Código: Impedância RLC em Série

```python
import cmath

frequencia = 60  # Hz
voltagem_pico = 220  # V
omega = 2 * cmath.pi * frequencia

R, L, C = 50.0, 0.15, 100e-6  # Componentes

X_L = omega * L
X_C = 1 / (omega * C)

# Impedância total (basta somar!)
Z_total = complex(R, X_L - X_C)
magnitude_Z = abs(Z_total)
fase_graus = cmath.phase(Z_total) * (180 / cmath.pi)

print(f"Impedância: {Z_total:.2f} Ohms")
print(f"Corrente Máxima: {voltagem_pico / magnitude_Z:.2f} A")
print(f"Defasagem: {fase_graus:.2f}°")
```

---

# Exemplo 2: Óptica e Ondas

Quando duas ondas se cruzam, ocorre o fenômeno da **superposição (interferência)**. 
Representando as ondas na forma polar (amplitude e fase), a biblioteca `cmath` ajuda a convertê-las e somá-las diretamente.

```python
import cmath

# Onda 1: Amplitude = 5, Fase = 0 rad
onda1 = cmath.rect(5, 0)

# Onda 2: Amplitude = 4, Fase = pi/3 rad (60°)
onda2 = cmath.rect(4, cmath.pi / 3)

# Superposição direta
onda_resultante = onda1 + onda2

print(f"Nova Amplitude: {abs(onda_resultante):.2f}")
print(f"Nova Fase: {cmath.phase(onda_resultante):.2f} rad")
```

---

# Outras Aplicações na Física

* **Mecânica Quântica:** A função de onda \(\Psi\) é complexa. A probabilidade espacial depende do produto pelo seu conjugado (`psi.conjugate()`).
* **Relatividade Restrita:** Uso de coordenadas imaginárias (\(ict\)) no espaço-tempo quadridimensional de Minkowski.
* **Processamento de Sinais:** Transformadas de Fourier para converter sinais do domínio do tempo para o domínio da frequência.


