from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Definindo as saudações
saudacoes_usuario = ["oi", "olá", "eae", "opa"]
saudacoes_bot = ["Olá!", "Oi, como posso ajudar?", "Oi, tudo bem?", "Olá, o que você gostaria de saber?"]

# Perguntas e respostas específicas
pergunta_resposta = {
    "o site foi desenvolvido por quem?": "O site foi desenvolvido pelas alunas: Aline Bertoldo Sales e Isabela Aparecida Hottum.",
    "quais ferramentas as alunas usaram?": "As alunas usaram as seguintes inteligências: Chat GPT, Copiloto, Quillbot e Adobe FireFly.",
    "qual foi a coisa mais estranha que aconteceu durante o trabalho?": "A coisa mais estranha aconteceu quando perguntamos ao Copiloto como ele se via. A inteligência respondeu que não tinha olhos, então não tinha consciência sobre sua aparência. E em seguida respondeu: 'É melhor mudarmos de assunto, não acha?'"
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    mensagem = request.form['mensagem'].strip().lower()

    if mensagem in saudacoes_usuario:
        resposta_bot = random.choice(saudacoes_bot)
    else:
        resposta_bot = pergunta_resposta.get(mensagem, "Desculpe, eu não entendi. Poderia repetir, por favor?")

    return resposta_bot

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
