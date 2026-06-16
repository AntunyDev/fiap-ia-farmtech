# 🤖 FarmTech Solutions — Fase 3: Modelagem de IA para Recomendação de Culturas Agrícolas

## 📋 Descrição do Projeto

Este repositório faz parte do PBL (Project-Based Learning) do curso de Inteligência Artificial, simulando o crescimento da startup fictícia **FarmTech Solutions**, uma consultoria de soluções para o agronegócio.

Nesta atividade (**Fase 3 — Capítulo 10**), foi realizada a análise de uma base de dados com informações de condições de solo e clima, relacionadas ao tipo de produto agrícola plantado, culminando no desenvolvimento de modelos preditivos de Machine Learning.

---

## 👥 Integrantes do Grupo

| Nome | RM |
|---|---|
| Antuny Marques | RM573852 |
| Tiago Gonçalves | RM570935 |
| Carlos Ribeiro | RM571449 |
| Anderson Sapucaia | RM572508 |
| Lucas Ribeiro | RM571668 |

---

## 🗂️ Estrutura do Repositório

```text
Cap_10/
├── AntunyMarques_RM573852_fase3_cap1.ipynb   ← Notebook principal com toda a análise
├── produtos_agricolas.csv               ← Dataset utilizado
└── README.md                            ← Documentação do módulo
```

---

## 🎯 Objetivo do Projeto

O projeto foi dividido em **quatro grandes etapas**:

1. **Análise Exploratória dos Dados (EDA)** — familiarização com o dataset e entendimento das variáveis.
2. **Análise Descritiva com Gráficos** — 11 visualizações com narrativa analítica.
3. **Perfil Ideal de Solo e Clima** — identificação das condições ideais e comparação com 3 culturas selecionadas.
4. **Modelos Preditivos de Machine Learning** — desenvolvimento e avaliação de 5 modelos com algoritmos distintos.

---

## 📂 Dataset

O arquivo `produtos_agricolas.csv` contém **2.200 amostras** de **22 culturas distintas** (100 amostras por cultura), com as seguintes variáveis:

| Variável | Descrição |
|---|---|
| `N` | Quantidade de Nitrogênio no solo |
| `P` | Quantidade de Fósforo no solo |
| `K` | Quantidade de Potássio no solo |
| `temperature` | Temperatura média da região (°C) |
| `humidity` | Umidade média do ar (%) |
| `ph` | pH do solo |
| `rainfall` | Precipitação pluviométrica (mm) |
| `label` | Tipo de cultura agrícola (variável alvo) |

> **Destaque:** A distribuição perfeitamente uniforme entre as 22 culturas é ideal para o treinamento de modelos de ML, eliminando o problema de classes desbalanceadas.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — linguagem principal
- **Pandas / NumPy** — manipulação e análise de dados
- **Matplotlib / Seaborn** — visualização de dados
- **Scikit-learn** — implementação dos modelos de Machine Learning

---

## 📊 Etapa de Análise Exploratória (EDA)

Foram criadas **11 visualizações** com narrativa analítica para explorar o comportamento das variáveis:

1. Distribuição de Produtos Agrícolas no Dataset
2. Distribuição da Temperatura
3. Matriz de Correlação entre Variáveis
4. Distribuição da Umidade
5. Distribuição do pH
6. Distribuição da Precipitação
7. Boxplot — Temperatura por Cultura
8. Boxplot — Umidade por Cultura
9. Relação Nitrogênio vs. Potássio por Cultura
10. Relação pH vs. Precipitação por Cultura
11. Análise de Outliers (IQR)

---

## 🤖 Modelos de Machine Learning

Foram desenvolvidos e avaliados **5 modelos preditivos** com algoritmos distintos:

| Modelo | Algoritmo |
|---|---|
| Modelo 1 | Regressão Logística |
| Modelo 2 | Árvore de Decisão |
| Modelo 3 | Random Forest |
| Modelo 4 | SVM (Support Vector Machine) |
| Modelo 5 | KNN (K-Nearest Neighbors) |

Cada modelo foi avaliado com as seguintes métricas:
- **Acurácia**
- **Precisão**
- **Recall**
- **F1-Score**
- **Matriz de Confusão**

---

## 📈 Principais Achados

- O dataset apresenta distribuição perfeitamente balanceada entre as 22 culturas, o que favorece o treinamento dos modelos.
- A temperatura apresenta distribuição aproximadamente normal, com concentração entre 20°C e 30°C.
- O **Random Forest** foi o modelo que obteve o melhor desempenho geral entre os cinco modelos avaliados.
- As variáveis de solo (N, P, K e pH) apresentam alta capacidade discriminativa entre as culturas.

---

## 🎥 Vídeo Demonstrativo

📺 [Link do vídeo no YouTube](https://youtu.be/po9MXINwsHw)

> O vídeo demonstra a execução do notebook, a análise exploratória dos dados, os modelos de Machine Learning treinados e os resultados obtidos.

---

## 📚 Referências

- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Crop Recommendation Dataset — Kaggle](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)
- Material didático do curso de Inteligência Artificial — FIAP

---

*FarmTech Solutions — Fase 3 | Cap. 10 | Curso de Inteligência Artificial*
