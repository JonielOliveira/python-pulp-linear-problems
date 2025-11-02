# 🧮 python-pulp-linear-problems

Este repositório contém exemplos de **problemas de Programação Linear (PL)** resolvidos em **Python** utilizando a biblioteca **[PuLP](https://coin-or.github.io/pulp/)**.  
Os problemas incluem casos de **maximização e minimização**, com **visualização gráfica** da região viável e da solução ótima.

O solver utilizado é o **CBC (COIN-OR Branch & Cut)**, que já vem embutido no PuLP — não sendo necessária nenhuma instalação adicional de solvers externos.

---

## 📂 Estrutura do projeto

```
python-pulp-linear-problems/
│
├── application/
│   ├── problem_a.py
│   ├── problem_b.py
│   ├── problem_c.py
│   ├── problem_d.py
│   ├── problem_e.py
│   ├── problem_f.py
│   ├── problem_g.py
│
├── docs/
│   └── listagraficopl.pdf ← enunciado dos problemas gráficos
│
├── requirements.txt       ← dependências do projeto
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🧰 Requisitos

- Python 3.9 ou superior  
- Pip atualizado (`python -m pip install --upgrade pip`)

---

## 🐍 Criando e ativando o ambiente virtual

Crie um ambiente isolado para o projeto (recomendado):

### Windows (PowerShell)
```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

> Após ativar o ambiente, você verá `(venv)` no início da linha do terminal.

---

## 📦 Instalando as dependências

Com o ambiente ativo, instale os pacotes necessários:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` inclui:
```
pulp
numpy
matplotlib
```

---

## ▶️ Executando os exemplos

Cada problema da lista está em um arquivo separado dentro da pasta `application/`.

Por exemplo, para rodar o problema **A**:
```bash
python application/problem_a.py
```

O programa exibirá:
- O **status da solução** (Ótimo, Inviável, etc.);
- Os **valores das variáveis** `x₁`, `x₂`;
- O **valor ótimo da função objetivo**;
- E um **gráfico** mostrando a região viável e o ponto ótimo.

---

## 📘 Material de apoio

O enunciado dos problemas está disponível em:
📄 [docs/listagraficopl.pdf](docs/listagraficopl.pdf)

---

## 🧠 Sobre o projeto

Este repositório tem caráter **educacional**, com foco em:
- Visualização de soluções gráficas de PL;
- Implementação prática do método CBC (COIN-OR Branch & Cut);
- Integração entre **modelagem matemática e programação**.

---
