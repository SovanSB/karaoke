# -*- coding: utf-8 -*-
import config
import telebot
import time
from telebot import types
from random import shuffle
from array import array


bot = telebot.TeleBot(config.token)
user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None


@bot.message_handler(commands=['help', 'start'])
def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Popular')
        msg = bot.reply_to(message, 'Choose the track', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')






def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        my_array = ['first', 'rebecca', 'allard', 'last']
        verifier = True
        if (sex == u'Popular'):
            chat_id = message.chat.id
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)            
            x = 0
            for char in my_array:
                if (verifier):
                    x+=1
                    markup.add(str(x) + " " + char)
                #bot.send_message(chat_id, str(x) + " " + char)            
            msg = bot.reply_to(message, 'Choose the track', reply_markup=markup)
            bot.register_next_step_handler(msg, after_song_is_chosen)
        else:
            raise Exception()
    except Exception as e:
        bot.reply_to(message, e)
    

def after_song_is_chosen(message):
    try:
        bot.reply_to(message, "You chose: " + message.text)
    except Exception as e:
        bot.reply_to(message, e)

        
    

##printing array with numbers
##my_array = ['first', 'rebecca', 'allard', 'last']
##        if (sex == u'Popular'):
##            x = 0
##            for char in my_array:
##                bot.send_message(chat_id, str(x) + " " + char)                
##                x+=1
##        else:
##            raise Exception()

bot.polling()
