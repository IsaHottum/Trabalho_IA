import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Carregar os dados de treinamento
data = {
    "Aparência do tempo": ["Nublado", "Nublado", "Nublado", "Nublado", "Chuvoso", "Chuvoso", "Chuvoso", "Chuvoso", "Ensolarado", "Ensolarado", "Ensolarado", "Ensolarado"],
    "Temperatura Numérica": [28, 18, 22, 27, 21, 20, 18, 24, 29, 27, 22, 21],
    "Temperatura Nominal": ["Quente", "Frio", "Ameno", "Quente", "Ameno", "Frio", "Frio", "Ameno", "Quente", "Quente", "Ameno", "Frio"],
    "Umidade Percentual": [86, 65, 90, 75, 96, 80, 70, 80, 85, 90, 95, 70],
    "Umidade Nominal": ["Alta", "Normal", "Alta", "Normal", "Alta", "Normal", "Normal", "Normal", "Alta", "Alta", "Alta", "Normal"],
    "Vento": ["Não", "Sim", "Sim", "Não", "Não", "Não", "Sim", "Não", "Não", "Sim", "Não", "Sim"],
    "Jogar?": ["Sim", "Sim", "Sim", "Sim", "Sim", "Sim", "Não", "Sim", "Não", "Não", "Não", "Sim"]
}

df = pd.DataFrame(data)

# Codificar as variáveis categóricas
label_encoders = {}
for column in df.select_dtypes(include="object"):
    label_encoders[column] = LabelEncoder()
    df[column] = label_encoders[column].fit_transform(df[column])

# Separar os dados de treinamento e teste
X_train = df.drop(columns=["Jogar?"])
y_train = df["Jogar?"]

# Construir e treinar o modelo de árvore de decisão
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Dados de teste
data_test = {
    "Aparência do tempo": ["Ensolarado", "Chuvoso"],
    "Temperatura Numérica": [24, 17],
    "Temperatura Nominal": ["Ameno", "Ameno"],
    "Umidade Percentual": [70, 91],
    "Umidade Nominal": ["Normal", "Alta"],
    "Vento": ["Sim", "Sim"]
}

df_test = pd.DataFrame(data_test)

# Codificar as variáveis categóricas para os dados de teste
for column in df_test.select_dtypes(include="object"):
    df_test[column] = label_encoders[column].transform(df_test[column])

# Prever os resultados
predictions = model.predict(df_test)

# Decodificar os resultados
predictions = label_encoders["Jogar?"].inverse_transform(predictions)

# Exibir os resultados
for i, prediction in enumerate(predictions):
    print(f"Para o caso {i+1}, a previsão é: {prediction}")
