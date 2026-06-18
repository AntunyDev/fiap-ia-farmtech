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

Projeto acadêmico para a disciplina de Machine Learning — FIAP. Aplicação prática da metodologia CRISP-DM para construir, avaliar e otimizar modelos de classificação de variedades de trigo a partir de medidas físicas dos grãos.

</div>

---

## Índice

- [Visão Geral](#visão-geral)
- [Pré-requisitos Rápidos](#pré-requisitos-rápidos)
- [Instalação e Execução](#instalação-e-execução)
- [Arquivos Principais](#arquivos-principais)
- [Resumo da Metodologia](#resumo-da-metodologia)
- [Modelos e Métricas](#modelos-e-métricas)
- [Boas Práticas e Recomendações](#boas-práticas-e-recomendações)
- [Referências](#referências)
- [Autores](#autores)

---

## Visão Geral

Este repositório contém um notebook (`seeds_classification.ipynb`) que: coleta e pré-processa o *Seeds Dataset* (UCI), explora estatisticamente as variáveis, treina vários classificadores (KNN, SVM, Random Forest, Naive Bayes, Logistic Regression), otimiza hiperparâmetros via `GridSearchCV` e interpreta os resultados com foco no F1-score macro.

O objetivo prático é demonstrar uma pipeline reprodutível que poderia, com mais dados, ser integrada a uma ferramenta de apoio à classificação em cooperativas agrícolas.

---

## Pré-requisitos Rápidos

- Python 3.10+
- Recomendado: criar um ambiente virtual (`venv` ou `conda`)

Instale dependências principais:

```bash
pip install -r requirements.txt
```

Se não houver `requirements.txt`, instale diretamente:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter joblib
```

---

## Instalação e Execução

1. Abra um terminal na pasta do projeto.

2. (Opcional) Crie e ative um ambiente virtual:

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Instale dependências (veja seção anterior).

4. Execute o notebook:

```bash
jupyter notebook Notebook/seeds_classification.ipynb
```

5. Execute as células na ordem indicada. O notebook foi preparado para localizar `seeds_dataset.txt` quando executado a partir da raiz do projeto ou da pasta `Notebook`.

Dica rápida para aceleração de pesquisa de hiperparâmetros: o notebook já usa `n_jobs=-1` no `GridSearchCV`, de modo a aproveitar todos os núcleos disponíveis no treinamento.

```python
GridSearchCV(..., n_jobs=-1)
```

---

## Arquivos Principais

- `Notebook/seeds_classification.ipynb` — Notebook principal com análise completa e modelagem.
- `Notebook/seeds_dataset.txt` — Dados originais (formato UCI: colunas separadas por espaços).
- `README.md` — Documentação (este arquivo).

---

## Resumo da Metodologia

Seguiu-se o fluxo CRISP-DM: entendimento do negócio, entendimento dos dados, preparação, modelagem, avaliação e otimização/interpretação. Os passos fundamentais implementados no notebook:

- Carregamento e atribuição de nomes às colunas
- Checagem de valores ausentes e balanceamento das classes
- Estatísticas descritivas (média, mediana, desvio padrão)
- Visualizações: histogramas, boxplots, scatterplots, pairplot e matriz de correlação
- Separação estratificada treino/teste (70/30)
- Pipelines com `StandardScaler` para modelos sensíveis à escala
- Treinamento inicial de 5 algoritmos e avaliação com acurácia, precisão, recall e F1-score (macro)
- Otimização de hiperparâmetros com `GridSearchCV` (StratifiedKFold)

---

## Modelos e Métricas

Modelos incluídos: KNN, SVM, Random Forest, Naive Bayes (Gaussiano) e Regressão Logística. A métrica prioritária usada para seleção foi o **F1-score macro**, adequada para conjuntos balanceados e que mede o desempenho médio entre classes.

O notebook gera tabelas comparativas, gráficos de barras do F1-score, relatórios de classificação e matrizes de confusão para cada modelo (antes e depois da otimização).

---

## Boas Práticas e Recomendações

- Reprodutibilidade: salvar o modelo final com `joblib.dump(melhor_modelo, 'Notebook/melhor_modelo.joblib')`.
- Performance: use `n_jobs=-1` em `GridSearchCV` e `RandomizedSearchCV` para acelerar buscas em máquinas com múltiplos núcleos.
- Avaliação adicional: considerar validação cruzada externa (`cross_val_score`) e testes com novos dados de safra/região.
- Explicabilidade: analisar importância de características (para Random Forest) e considerar técnicas como SHAP para explicabilidade local.

Exemplo para salvar o modelo final:

```python
from joblib import dump
dump(melhor_modelo, 'Notebook/melhor_modelo.joblib')
```

Exemplo para carregar o modelo salvo:

```python
from joblib import load
melhor_modelo = load('Notebook/melhor_modelo.joblib')
```

---

## Referências

- UCI Machine Learning Repository — Seeds Dataset: https://archive.ics.uci.edu/dataset/236/seeds

---

## Autores

Equipe FIAP — Projeto acadêmico.

---

<div align="center">

*Desenvolvido com Machine Learning — FIAP*

</div>
