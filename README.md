<div align="center">

<img src="https://raw.githubusercontent.com/agodoi/templateFiapVfinal/main/assets/logo-fiap.png" alt="FIAP Logo" width="160">

<br><br>

# 🌱 FarmTech Solutions

### Repositório Acadêmico — Curso de Inteligência Artificial

![FIAP](https://img.shields.io/badge/FIAP-Inteligência_Artificial-ED1C24?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJ3aGl0ZSI+PHBhdGggZD0iTTEyIDNMMSA5bDExIDZsMTEtNkwxMiAzeiIvPjxwYXRoIGQ9Ik0xIDE1bDExIDYgMTEtNiIvPjwvc3ZnPg==&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Oracle](https://img.shields.io/badge/Oracle_DB-F80000?style=for-the-badge&logo=oracle&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-2ea44f?style=for-the-badge)

<br>

*Repositório central que reúne todas as entregas e projetos da disciplina de **Inteligência Artificial** da FIAP, sob o tema **FarmTech Solutions** — uma startup fictícia de consultoria em soluções tecnológicas para o agronegócio.*

---

</div>

## 📖 Sobre o Projeto

O **FarmTech Solutions** é um projeto acadêmico de **PBL (Project-Based Learning)** que simula a jornada de uma startup de AgroTech. Ao longo de diversas fases, o projeto evolui desde análise de dados agrícolas básica até a aplicação de técnicas avançadas de Machine Learning, passando por sistemas de gestão com banco de dados e sensoriamento IoT.

Cada fase do curso adiciona novas competências e tecnologias, refletindo a progressão do aprendizado e a maturidade da solução proposta.

---

## 👥 Equipe

<div align="center">

| Integrante | RM |
|:---|:---:|
| **Antuny Marques** | `RM573852` |
| **Tiago Gonçalves** | `RM570935` |
| **Carlos Ribeiro** | `RM571449` |
| **Lucas Ribeiro** | `RM572508` |
| **Anderson Sapucaia** | `RM571668` |

</div>

---

## 🗺️ Mapa de Fases

```
  Fase 01                Fase 02                Fase 03                Fase 04
┌──────────┐         ┌──────────┐          ┌──────────┐          ┌──────────┐
│  Python   │         │  Python  │          │  Oracle  │          │  Machine │
│  R Lang   │  ───▶   │  Oracle  │   ───▶   │   SQL    │   ───▶   │ Learning │
│  CSV/API  │         │  Rich UI │          │  IoT     │          │ CRISP-DM │
└──────────┘         └──────────┘          └──────────┘          └──────────┘
  Fundamentos          Gestão                Banco de               Modelagem
  de Dados             Agrícola              Dados                  Preditiva
```

---

## 📂 Estrutura do Repositório

```
FarmTech/
│
├── 📄 README.md                ← Você está aqui
│
├── 📁 Fase_01/
│   └── 📁 Atv_01/             # Análise de Dados Agrícolas
│       ├── 📁 IA_CAP1/
│       │   ├── python/         # Sistema CRUD em Python
│       │   ├── r/              # Análise estatística com R
│       │   └── data/           # Dados CSV
│       └── 📄 README.md
│
├── 📁 Fase_02/
│   └── 📁 Atv_02/             # FarmTech Cana — Gestão de Colheitas
│       ├── 📁 src/             # Código fonte principal
│       ├── 📁 config/          # Configurações e .env
│       ├── 📁 documents/       # Dados JSON e logs
│       ├── 📁 scripts/         # Scripts auxiliares
│       ├── 📁 assets/          # Recursos visuais
│       └── 📄 README.md
│
├── 📁 Fase_03/
│   └── 📁 Atv_01/             # Banco de Dados Oracle
│       ├── 📁 meugit/          # Consultas SQL e dados
│       └── 📄 README.md
│
└── 📁 Fase_04/
    └── 📁 Atv_02/             # Machine Learning — Classificação de Grãos
        ├── 📁 seeds/           # Notebook e dataset
        └── 📄 README.md
```

---

## 🚀 Fases do Projeto

<details>
<summary><b>📗 Fase 01 — Fundamentos: Análise de Dados Agrícolas</b></summary>

<br>

> **Diretório:** [`Fase_01/Atv_01`](./Fase_01/Atv_01)

Sistema de gerenciamento de plantações e análise de dados agrícolas, integrando Python e R para criar uma base sólida de manipulação e visualização de dados do campo.

**🔧 Tecnologias:** Python · R · CSV · API Meteorológica

**✨ Destaques:**
- CRUD completo de plantações
- Cálculo de manejo de insumos agrícolas
- Exportação de dados para CSV
- Consulta de dados meteorológicos via API em tempo real
- Análise estatística com linguagem R

</details>

---

<details>
<summary><b>📘 Fase 02 — Gestão: FarmTech Cana — Inteligência na Gestão de Colheitas</b></summary>

<br>

> **Diretório:** [`Fase_02/Atv_02`](./Fase_02/Atv_02)

Evolução do projeto com foco na gestão inteligente de colheitas mecanizadas de cana-de-açúcar, abordando a problemática real de **perdas na colheita** — que podem ultrapassar 15% na colheita mecânica, gerando prejuízos de R$ 20 milhões/ano só em São Paulo.

**🔧 Tecnologias:** Python · Oracle Database · Rich (UI) · JSON

**✨ Destaques:**
- Monitoramento de produtividade (esperada vs. real)
- Cálculo automático de perdas e prejuízo financeiro
- Sistema de alertas para desvios operacionais
- Interface visual com tema AgroTech (Rich framework)
- Persistência dupla: JSON (local) + Oracle Database (corporativo)
- Logs de auditoria e validação rigorosa de entradas

</details>

---

<details>
<summary><b>📙 Fase 03 — Dados: Banco de Dados Oracle com Sensores IoT</b></summary>

<br>

> **Diretório:** [`Fase_03/Atv_01`](./Fase_03/Atv_01)

Integração dos dados coletados por sensores agrícolas (IoT) da fase anterior em um banco de dados relacional Oracle, com criação de tabelas, importação de dados e execução de consultas analíticas para extrair insights sobre o solo.

**🔧 Tecnologias:** Oracle Database XE · Oracle SQL Developer · SQL · Python

**✨ Destaques:**
- Importação de 40 registros de sensores de solo (umidade, pH, NPK, precipitação)
- 10 consultas SQL analíticas para insights do solo
- Migração de tipo de dados para maior precisão (pH inteiro → decimal)
- Análise de irrigação vs. precipitação
- Detecção de casos críticos (baixa umidade, solo ácido)
- 🎥 [Vídeo demonstrativo no YouTube](https://youtu.be/lCSyHjeVvOY)

</details>

---

<details>
<summary><b>📕 Fase 04 — Modelagem: Machine Learning para Classificação de Grãos</b></summary>

<br>

> **Diretório:** [`Fase_04/Atv_02`](./Fase_04/Atv_02)

Aplicação de algoritmos de aprendizado de máquina seguindo a metodologia **CRISP-DM** para automatizar a classificação de variedades de trigo (Kama, Rosa e Canadian) a partir de características físicas dos grãos.

**🔧 Tecnologias:** Python · Jupyter Notebook · scikit-learn · Pandas · NumPy · Matplotlib · Seaborn

**✨ Destaques:**
- 5 algoritmos comparados: KNN, SVM, Random Forest, Naive Bayes, Regressão Logística
- Dataset UCI Seeds (210 amostras, 7 atributos)
- Otimização com Grid Search
- Métricas completas: Acurácia, Precisão, Recall, F1-score, Matriz de Confusão
- Análise exploratória com visualizações (boxplots, dispersão, correlação)

</details>

---

## 🛠️ Stack Tecnológica

<div align="center">

| Categoria | Tecnologias |
|:---|:---|
| **Linguagens** | Python 3.10+ · R · SQL |
| **Banco de Dados** | Oracle Database XE · Oracle SQL Developer |
| **Machine Learning** | scikit-learn · Pandas · NumPy |
| **Visualização** | Matplotlib · Seaborn · Rich |
| **Dados & APIs** | CSV · JSON · API Meteorológica |
| **Ferramentas** | Jupyter Notebook · Git/GitHub |

</div>

---

## 📊 Evolução do Aprendizado

```
                 ┌──────────────────────────────────────────────────────────┐
                 │              JORNADA FARMTECH SOLUTIONS                  │
                 └──────────────────────────────────────────────────────────┘

  ▓▓▓▓░░░░░░░░░░░░   Fase 01 → Fundamentos (Python, R, APIs)
  ▓▓▓▓▓▓▓▓░░░░░░░░   Fase 02 → Gestão (CRUD, Oracle, Rich UI)
  ▓▓▓▓▓▓▓▓▓▓▓▓░░░░   Fase 03 → Dados (SQL, IoT, Sensores)
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   Fase 04 → Modelagem (ML, CRISP-DM, scikit-learn)
```

---

## 📚 Contexto Acadêmico

| | |
|:---|:---|
| **Instituição** | FIAP — Faculdade de Informática e Administração Paulista |
| **Curso** | Inteligência Artificial |
| **Metodologia** | PBL — Project-Based Learning |
| **Tema Central** | FarmTech Solutions — Consultoria AgroTech |

---

## 📝 Como Navegar

1. Cada **Fase** possui seu próprio diretório com atividades independentes
2. Cada **Atividade** contém seu próprio `README.md` com instruções detalhadas
3. Para executar qualquer projeto, acesse o diretório correspondente e siga as instruções do README local

---

<div align="center">

### 🌾 *"Da terra ao código — Transformando dados agrícolas em decisões inteligentes."*

<br>

Desenvolvido com 💚 para a FIAP — Curso de Inteligência Artificial

<br>

<img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" height="22"> <img src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" height="22">

<sub>Este projeto está licenciado sob <a href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International</a></sub>

</div>
