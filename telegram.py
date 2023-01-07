from telebot import TeleBot
from credentials import BOT_TOKEN, CHAT_ID


bot = TeleBot(BOT_TOKEN, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	user_name: str = message.from_user.first_name
	bot.reply_to(message, f'Hi {user_name}, how are you doing?')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


bot.send_message(CHAT_ID, 'Bot launched')
bot.infinity_polling()
