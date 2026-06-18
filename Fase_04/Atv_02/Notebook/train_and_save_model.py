"""
Treina vários modelos no Seeds Dataset e salva o melhor modelo em joblib.
Uso: python Notebook/train_and_save_model.py
"""

from pathlib import Path
import numpy as np
import pandas as pd
from joblib import dump

from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

RANDOM_STATE = 42

colunas = [
    "area",
    "perimetro",
    "compacidade",
    "comprimento_nucleo",
    "largura_nucleo",
    "coeficiente_assimetria",
    "comprimento_sulco_nucleo",
    "classe",
]

caminho_possivel = Path("Notebook/seeds_dataset.txt")
if not caminho_possivel.exists():
    caminho_possivel = Path("seeds_dataset.txt")
if not caminho_possivel.exists():
    raise FileNotFoundError(
        "Arquivo seeds_dataset.txt não encontrado em Notebook/ ou na raiz do projeto."
    )

# Carrega dados
df = pd.read_csv(caminho_possivel, sep=r"\s+", header=None, names=colunas)

features = colunas[:-1]
target = "classe"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=RANDOM_STATE, stratify=y
)

# Modelos e pipelines
modelos = {
    "KNN": Pipeline([("scaler", StandardScaler()), ("model", KNeighborsClassifier())]),
    "SVM": Pipeline(
        [("scaler", StandardScaler()), ("model", SVC(random_state=RANDOM_STATE))]
    ),
    "RandomForest": Pipeline(
        [("model", RandomForestClassifier(random_state=RANDOM_STATE))]
    ),
    "NaiveBayes": Pipeline([("model", GaussianNB())]),
    "LogisticRegression": Pipeline(
        [
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)),
        ]
    ),
}

param_grid = {
    "KNN": {
        "model__n_neighbors": [3, 5, 7],
        "model__weights": ["uniform", "distance"],
    },
    "SVM": {
        "model__C": [0.1, 1, 10],
        "model__kernel": ["linear", "rbf"],
    },
    "RandomForest": {
        "model__n_estimators": [100, 200],
        "model__max_depth": [None, 5],
    },
    "NaiveBayes": {
        "model__var_smoothing": np.logspace(-12, -8, 3),
    },
    "LogisticRegression": {
        "model__C": [0.1, 1, 10],
    },
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

best_models = {}
results = []

for nome, pipeline in modelos.items():
    print(f"Buscando melhor {nome}...")
    grid = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid[nome],
        scoring="f1_macro",
        cv=cv,
        n_jobs=-1,
        verbose=0,
    )
    grid.fit(X_train, y_train)
    best = grid.best_estimator_
    y_pred = best.predict(X_test)
    f1 = f1_score(y_test, y_pred, average="macro")
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average="macro")
    rec = recall_score(y_test, y_pred, average="macro")

    best_models[nome] = best
    results.append(
        {
            "modelo": nome,
            "f1_macro": f1,
            "acuracia": acc,
            "precisao_macro": prec,
            "recall_macro": rec,
            "melhores_params": grid.best_params_,
        }
    )

# Seleciona melhor pelo f1_macro
results_df = pd.DataFrame(results).sort_values("f1_macro", ascending=False)
melhor = results_df.iloc[0]
melhor_nome = melhor["modelo"]
melhor_modelo = best_models[melhor_nome]

print("\nResultados por modelo:")
print(results_df.to_string(index=False))

# Salva o melhor modelo
saida = Path("Notebook/melhor_modelo.joblib")
dump(melhor_modelo, saida)
print(f"\nMelhor modelo: {melhor_nome} salvo em: {saida}")
