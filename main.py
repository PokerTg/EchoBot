import telebot
from telebot import types
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot("***TOKEN***")

@bot.message_handler(commands=['start'])
def start(m):
  cid = m.chat.id
  markup = types.InlineKeyboardButton()
  markup.add(types.InlineKeyboardButton('English', callback_data='English'),types.InlineKeyboardButton("فارسی",callback_data='Persian'))
  bot.send_message(cid, '***TEXT***',reply_markup=markup,parse_mode="Markdown")
  
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
  if call.message:
    if call.data == 'English':
      markupen = types.InlineKeyboardButton()
      markupen.add(types.InlineKeyboardButton("Change language", callback_data="cl")
      bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="***TEXT***"parse_mode="Markdown",reply_markup=markupen)
  if call.message:
    if call.data == 'cl':'
    markupcl = types.InlineKeayboardButton()
    markup.add(types.InlineKeyboardButton('English', callback_data='English'),types.InlineKeyboardButton("فارسی",callback_data='Persian'))
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="***TEXT***"parse_mode="Markdown",reply_markup=markupen)
