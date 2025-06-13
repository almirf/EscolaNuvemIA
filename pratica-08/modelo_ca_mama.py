# Importação das bibliotecas do projeto
from sklearn.datasets import load_breast_cancer

# Dataset de CA de mama
from sklearn.ensemble import RandomForestClassifier # Algoritmo do Random Forest

from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

# Funcao para dividir o conjunto de dados
from sklearn.model_selection import train_test_split

# Carregar o dataset de CA de mama
data = load_breast_cancer()

"""
O dataset possúi características (data.data) e rótulos (data.target).
data.data: matriz com as 30 características para cada uma das amostras
data.target: vetor 0 (maligno) ou 1 (benigno) para cada amostra
Dividir os dados em conjuntos de treino (70%) e de teste (30%).
X_train e X_test: características de treino e de teste
y_train e y_test: rótulos para treino e teste
random_state=42, garantir que a reprodutibilidade dos resultados
"""

X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3, random_state=42)

# Iniciar o modelo com os parametros padrao
model = RandomForestClassifier(random_state=42)

# Treinamento do modelo
model.fit(X_train, y_train)

# Fazer previsao do modelo com os dados de teste
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:,1]

# Calculo das métricas de avaliacao
precision = precision_score(y_test, y_pred)  # Precisão: TP / (TP + FP)
recall = recall_score(y_test, y_pred) # Recall (Sensibilidade): TP / (TP + FN)
f1 = f1_score(y_test, y_pred) # F1-Score: 2*(precision*recall)/(precision+recall)
auc = roc_auc_score(y_test, y_pred_proba) # Area da curva ROC

print(f"A métrica Precision é: {precision:.5f}")
print(f"A métrica Recall é: {recall:.5f}")
print(f"A métrica F1-Score é: {f1:.5f}")
print(f"A métrica AUC-ROC é: {auc:.5f}")
