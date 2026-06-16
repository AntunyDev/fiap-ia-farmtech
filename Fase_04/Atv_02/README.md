<div align="center">

# 🌾 Da Terra ao Código

### Automatizando a Classificação de Grãos com Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter_Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen?style=for-the-badge)

<br>

*Projeto acadêmico desenvolvido para a disciplina de Machine Learning da **FIAP**, aplicando a metodologia **CRISP-DM** na construção de modelos capazes de classificar variedades de grãos de trigo a partir de características físicas.*

---

</div>

## 📋 Índice

- [Contexto](#-contexto)
- [Equipe](#-equipe)
- [Objetivo](#-objetivo)
- [Dataset](#-dataset)
- [Metodologia CRISP-DM](#-metodologia-crisp-dm)
- [Modelos Utilizados](#-modelos-utilizados)
- [Métricas de Avaliação](#-métricas-de-avaliação)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Executar](#-como-executar)
- [Principais Análises Realizadas](#-principais-análises-realizadas)
- [Resultado Esperado](#-resultado-esperado)
- [Conclusão](#-conclusão)
- [Referência](#-referência)

---

## 🌱 Contexto

Em cooperativas agrícolas de pequeno porte, a classificação dos grãos muitas vezes é feita **manualmente por especialistas**. Embora esse processo seja importante, ele pode ser demorado, subjetivo e sujeito a inconsistências.

A proposta deste trabalho é demonstrar como **algoritmos de aprendizado de máquina** podem apoiar essa tarefa, automatizando a classificação e oferecendo resultados mais **rápidos e padronizados**.

---

## 👥 Equipe

<div align="center">

| RM | Integrante |
|:---:|:---|
| `RM573852` | Antuny |
| `RM570935` | Tiago |
| `RM571449` | Carlos |
| `RM572508` | Lucas |
| `RM571668` | Anderson |

</div>

---

## 🎯 Objetivo

Desenvolver, avaliar e comparar modelos de classificação para identificar **três variedades de trigo**:

<div align="center">

| Variedade | Descrição |
|:---:|:---|
| 🌾 **Kama** | Variedade de trigo com características físicas específicas |
| 🌹 **Rosa** | Variedade com perfil morfológico distinto |
| 🍁 **Canadian** | Variedade canadense com atributos diferenciados |

</div>

Para isso, o projeto realiza:

- ✅ Análise e pré-processamento dos dados
- ✅ Exploração estatística e visual das características
- ✅ Separação dos dados em treino e teste
- ✅ Treinamento de diferentes algoritmos de classificação
- ✅ Avaliação por métricas de desempenho
- ✅ Otimização de hiperparâmetros com Grid Search
- ✅ Interpretação dos resultados no contexto agrícola

---

## 📊 Dataset

O conjunto de dados utilizado é o **Seeds Dataset**, disponível no [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/236/seeds).

> **210 amostras** de grãos de trigo, distribuídas igualmente entre três variedades. Cada amostra possui **7 atributos físicos** e uma **classe alvo**.

### Atributos

| # | Atributo | Descrição |
|:---:|:---|:---|
| 1 | **Área** | Medida da área do grão |
| 2 | **Perímetro** | Comprimento do contorno do grão |
| 3 | **Compacidade** | Medida relacionada ao formato do grão |
| 4 | **Comprimento do núcleo** | Comprimento do eixo principal do núcleo |
| 5 | **Largura do núcleo** | Comprimento do eixo secundário do núcleo |
| 6 | **Coef. de assimetria** | Medida da assimetria do grão |
| 7 | **Comprimento do sulco** | Comprimento do sulco central do grão |
| — | **Classe** | Variedade do trigo (Kama, Rosa, Canadian) |

---

## 🔄 Metodologia CRISP-DM

O notebook segue a metodologia **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*), uma abordagem consolidada em projetos de ciência de dados.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   1. Entendimento     2. Entendimento     3. Preparação         │
│      do Negócio  ──▶     dos Dados   ──▶    dos Dados           │
│                                                                 │
│         ▲                                       │               │
│         │                                       ▼               │
│                                                                 │
│   6. Otimização e     5. Avaliação        4. Modelagem          │
│      Interpretação ◀──   dos Modelos  ◀──                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

<details>
<summary><strong>📌 Detalhamento das Etapas</strong></summary>

<br>

| Etapa | Descrição |
|:---|:---|
| **1. Entendimento do negócio** | Definição do problema: automatizar a classificação de grãos para apoiar cooperativas agrícolas. |
| **2. Entendimento dos dados** | Carregamento do dataset, visualização inicial, identificação das classes e análise da estrutura das variáveis. |
| **3. Preparação dos dados** | Verificação de valores ausentes, separação entre variáveis explicativas e variável alvo, divisão treino/teste e padronização. |
| **4. Modelagem** | Treinamento de diferentes algoritmos de classificação. |
| **5. Avaliação** | Comparação dos modelos por acurácia, precisão, recall, F1-score e matrizes de confusão. |
| **6. Otimização e interpretação** | Ajuste de hiperparâmetros com Grid Search e análise dos resultados obtidos. |

</details>

---

## 🤖 Modelos Utilizados

Foram implementados e comparados **cinco algoritmos** de classificação:

| Algoritmo | Sigla | Requer Padronização? |
|:---|:---:|:---:|
| K-Nearest Neighbors | KNN | ✅ Sim |
| Support Vector Machine | SVM | ✅ Sim |
| Random Forest | RF | ❌ Não |
| Naive Bayes Gaussiano | GNB | ❌ Não |
| Regressão Logística | LR | ✅ Sim |

> **Nota:** Os modelos sensíveis à escala (KNN, SVM e Regressão Logística) foram treinados com padronização das variáveis por meio do `StandardScaler`.

---

## 📈 Métricas de Avaliação

| Métrica | Descrição |
|:---|:---|
| **Acurácia** | Proporção total de classificações corretas |
| **Precisão (macro)** | Média da precisão entre as classes |
| **Recall (macro)** | Média do recall entre as classes |
| **F1-score (macro)** | Média do equilíbrio entre precisão e recall |
| **Matriz de confusão** | Visualização dos acertos e erros por classe |

> 💡 O uso do **F1-score macro** é importante porque avalia o desempenho médio entre todas as variedades, evitando que a análise dependa apenas da acurácia geral.

---

## 📁 Estrutura do Projeto

```
📦 ATV_02/
 ┣ 📄 README.md                          # Documentação do projeto
 ┗ 📂 seeds/
   ┣ 📓 seeds_classification.ipynb       # Notebook principal (análise + modelagem)
   ┗ 📄 seeds_dataset.txt                # Dataset utilizado
```

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.10 ou superior
- Jupyter Notebook

### Passo a passo

**1.** Clone o repositório ou baixe os arquivos do projeto.

**2.** Instale as dependências necessárias:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

**3.** Inicie o Jupyter Notebook:

```bash
jupyter notebook seeds/seeds_classification.ipynb
```

**4.** Execute as células **em ordem**, do início ao fim.

> 📌 O notebook foi preparado para encontrar o arquivo `seeds_dataset.txt` tanto quando executado dentro da pasta `seeds` quanto a partir da raiz do projeto.

---

## 🔍 Principais Análises Realizadas

<div align="center">

| Categoria | Análises |
|:---|:---|
| **Exploração Inicial** | Primeiras linhas do dataset, estatísticas descritivas (média, mediana, desvio padrão) |
| **Distribuição** | Análise da distribuição das classes, histogramas das características |
| **Visualizações** | Boxplots por variedade, gráficos de dispersão, matriz de correlação |
| **Pré-processamento** | Verificação de valores ausentes, avaliação de escalonamento |
| **Modelagem** | Treinamento e comparação dos modelos, otimização com Grid Search |
| **Resultados** | Interpretação final e insights para o contexto agrícola |

</div>

---

## 📊 Resultado Esperado

Ao final da execução, o notebook apresenta:

- 📋 Tabela comparativa dos modelos base
- 📄 Relatórios de classificação por algoritmo
- 🔲 Matrizes de confusão
- ⚡ Comparação após otimização com Grid Search
- 🏆 Indicação do **melhor modelo** segundo o F1-score macro
- 💬 Discussão dos insights obtidos

---

## 💡 Conclusão

O projeto demonstra que técnicas de **Machine Learning** podem ser aplicadas para apoiar a classificação de grãos de trigo com base em características físicas. Mesmo utilizando um dataset pequeno, os modelos conseguem identificar **padrões relevantes** entre as variedades.

> Para uso real em cooperativas agrícolas, seria recomendado **ampliar a base de dados** com novas amostras, coletadas em diferentes regiões, safras e condições de produção. Ainda assim, o estudo mostra o potencial da **automação como ferramenta de apoio à tomada de decisão** no setor agrícola.

---

## 📚 Referência

- UCI Machine Learning Repository. **Seeds Dataset**. Disponível em: <https://archive.ics.uci.edu/dataset/236/seeds>

---

<div align="center">

*Desenvolvido com 🌾 para a disciplina de Machine Learning — FIAP 2025*

</div>
