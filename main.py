import telebot
from telebot import types
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot("***TOKEN***")

@bot.message_handler(commands=['start'])
def start(m):
  cid = m.chat.id
  markup = types.InlineKeyboardButton()
  markup.add(types.InlineKeyboardButton('English', callback_data='English'),types.InlineKeyboardButton("فارسی",callback_data='Persian'))
  bot.send_message(cid, 'Choose your language:\n\nزبان خود را انتخاب کنید:'reply_markup=markup)
