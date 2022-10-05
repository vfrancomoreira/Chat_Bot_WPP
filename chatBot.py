from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from spacy.cli import download # Código para corrigir o bug

# Versão correta para funcionamento - 3.7.9

download("en_core_web_sm")

class ENGSM:
    ISO_639_1 = 'en_core_web_sm'

chatbot = ChatBot("Bot-Goes", tagger_language=ENGSM)

conversa = [
    "Olá",
    "Eai, tudo bem?",
    "Tudo!",
    "Vai a faculdade hoje?",
    "Sim",
    "Ótimo, bons estudos!",
]

trainer = ListTrainer(chatbot)
# Use a 'conversa' para 'treinar' o 'chatbot'
trainer.train(conversa)

while True:
    mensagem = input("Você: ")
    if mensagem == 'Tchau' or '':
        break
    resposta = chatbot.get_response(mensagem)
    print('Bot: ', resposta)

# Reinicia banco de dados que armazena as informações
# chatbot.storage.drop()