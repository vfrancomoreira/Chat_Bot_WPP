from chatterbot import ChatBot
bot = ChatBot('HAL3000')

user = input('Você: ')

resposta = bot.get_response(user)
print(f'Bot: {resposta}')
