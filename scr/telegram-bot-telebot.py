
# pip install telebot
import telebot

TOKEN = ""
bot = telebot.TeleBot(TOKEN, parse_mode="MarkDown")


# открпавка сообщения текстового сообщения через команды
# к примеру команда /start
@bot.message_handler(commands=["start"], content_types=["text"])
def start_message(message):

    bot.send_message(message.chat.id, "Привет")
    
