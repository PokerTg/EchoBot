import teebot

bot = telebot.TeleBot("***TOKEN***")

@bot.message_handler(commands=['start'])
def start(m):
  cid = m.chat.id
  bot.send_message(cid, "slm")

bot.polling()
