import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# Dados de treinamento
train_data = {
    'email': ['email1', 'email2', 'email3', 'email4', 'email5', 'email6', 'email7', 'email8', 'email9', 'email10', 'email11', 'email12', 'email13', 'email14', 'email15', 'email16', 'email17', 'email18', 'email19', 'email20', 'email21', 'email22', 'email23', 'email24', 'email25'],
    'texto': ['email de propaganda', 'oferta imperdível', 'promoção relâmpago', 'notificação de entrega', 'email importante', 'desconto exclusivo', 'aviso de pagamento pendente', 'newsletter semanal', 'última chance de compra', 'alerta de segurança', 'lembrete de pagamento', 'novidades da loja', 'confirmação de compra', 'confirmar cadastro', 'atualização de cadastro', 'oferta especial para clientes', 'convite para evento', 'sorteio de prêmios', 'recibo de pagamento', 'email de boas-vindas', 'oferta relâmpago', 'anúncio importante', 'novidades do site', 'comunicado urgente', 'email promocional'],
    'spam': [1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1]
}

# Criar DataFrame com os dados de treinamento
train_df = pd.DataFrame(train_data)

# Separar os recursos (X) e os rótulos (y)
X_train_text = train_df['texto']
y_train = train_df['spam']

# Vetorizar os dados de texto
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train_text)

# Construir e treinar o modelo Random Forest
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Dados de teste
test_data = {
    'email': ['email26', 'email27', 'email28', 'email29', 'email30'],
    'texto': ['lembrete', 'oferta imperdível', 'informativo', 'alerta de segurança', 'última chance de compra']
}

# Criar DataFrame com os dados de teste
test_df = pd.DataFrame(test_data)

# Vetorizar os dados de texto dos testes
X_test = vectorizer.transform(test_df['texto'])

# Fazer previsões para os dados de teste
predictions = model.predict(X_test)

# Exibir as previsões
print("Previsões para os dados de teste:")
for email, prediction in zip(test_df['email'], predictions):
    print(f"{email}: {'Spam' if prediction == 1 else 'Não Spam'}")
