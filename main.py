#-*- coding: utf-8-*-
import telebot
from telebot import types
import time
from time import sleep
import json
reload(sys)
sys.setdefaultencoding("utf-8")

bot = telebot.TeleBot("***TOKEN***")

@bot.message_handler(commands=['start'])
def start(m):
    cid = m.chat.id
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton('English', callback_data='English'),types.InlineKeyboardButton("فارسی", callback_data='Persian'))
	bot.send_message(cid, '*Choose your language:*\n\n*زبان خود را انتخاب کنید:*', parse_mode="Markdown",reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def start_callback(call):
	if call.message:
		if call.data == 'Englsih':
			markup1 = types.InlineKeyboardMarkup()
			markup1.add(types.InlineKeyboardButton('\xE2\x97\x80\xEF\xB8\x8F Return', callback_data='back'))
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="***ENGLISH TEXT***",parse_mode="Markdown", reply_markup=markup)
