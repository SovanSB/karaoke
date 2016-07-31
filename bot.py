# -*- coding: utf-8 -*-
import config
import telebot
import time
from telebot import types
from random import shuffle
from array import array


bot = telebot.TeleBot(config.token)
user_dict = {'verifier': 'True'}
song_dict = {'saved': 'BQADAgADmwADQwjCDvJYaFVLGOVhAg', 'allard': 'BQADAgADmQADQwjCDmGENRjiYpxCAg', 'last': 'BQADAgADmgADQwjCDpbjSwJaW-qIAg', 'rebecca': 'BQADAgADmAADQwjCDmeL1_QqIzn4Ag', 'first': 'BQADAgADlwADQwjCDqrF79xlTL1dAg', 'beatles_minus': 'BQADAgADnAADQwjCDh3oEBwncGIoAg'}

    #'beatles_beep1': 'BQADAgADgwADQwjCDvuLATG6vGR7Ag', 'last': 'BQADAgADggADQwjCDi4KY1l6lRFLAg', 'saved': 'BQADAgADfgADQwjCDp9prPdAo_oTAg', 'Amber3': 'BQADAgADWQADQwjCDkA6Jautl_5MAg', 'Beatles2': 'BQADAgADawADQwjCDgexoI6odrsAAQI', 'allard': 'BQADAgADgQADQwjCDmShucx0N776Ag', 'first': 'BQADAgADfwADQwjCDjurv3e4xyhiAg', 'rebecca': 'BQADAgADgAADQwjCDjOjHyXaw5VKAg'}
#{'rebecca': 'BQADAgADaAADQwjCDt5vQxKhjsZpAg', 'last': 'BQADAgADagADQwjCDkjbBXe85WzFAg', 'Beatles2': 'BQADAgADawADQwjCDgexoI6odrsAAQI', 'first': 'BQADAgADZwADQwjCDlhT5C3hAkowAg', 'Amber3': 'BQADAgADWQADQwjCDkA6Jautl_5MAg', 'allard': 'BQADAgADaQADQwjCDnVN-Qcx8LzdAg', 'saved': 'BQADAgADZgADQwjCDmWGQq_fFeLjAg'}
#{'first': 'BQADAgADVQADQwjCDkPxv20-mXpLAg', 'Amber3': 'BQADAgADWQADQwjCDkA6Jautl_5MAg', 'allard': 'BQADAgADVwADQwjCDvqfYfU18-qWAg', 'rebecca': 'BQADAgADVgADQwjCDqoc0kLO5QzHAg', 'saved': 'BQADAgADVAADQwjCDkrX_HHBOQlYAg', 'last': 'BQADAgADWAADQwjCDlUqDHuKNvZZAg'}#{'last': 'BQADAgADLwADQwjCDgsQlvjobSeMAg', 'allard': 'BQADAgADLgADQwjCDi3QMiDPVY1rAg', 'rebecca': 'BQADAgADLQADQwjCDt41a8LhdLusAg', 'first': 'BQADAgADLAADQwjCDmAvA2xNJiU9Ag', 'saved': 'BQADAgADKwADQwjCDlRfdL4abcAuAg'}#{'last': 'BQADAgADFwADQwjCDsiklDwuuwbuAg', 'first': 'BQADAgADFAADQwjCDvl53sy_RAtjAg', 'rebecca': 'BQADAgADFQADQwjCDr6FHYUtlXd0Ag', 'allard': 'BQADAgADFgADQwjCDrKbvh-1WfqkAg'}


words_array = ['Yesterday', 'all my troubles seemed so far away','Now it looks as though they\'re here to stay','Oh, I believe', 'in yesterday'
               ,'Suddenly','I\'m not half the man','I used to be',
               'There\'s a shadow','hanging over me',
               'Oh, yesterday','came suddenly',
               'Why she','had to go',
               'I don\'t know','she wouldn\'t say','I said','something wrong, now I long','for yesterday',
               'Yesterday','love was such an easy game','to play','Now I need a place to hide',
               'away. Oh, I believe','in yesterday','Why she','had to go, I don\'t know','she wouldn\'t say',
               'I said ','something wrong, now I long','for yesterday','Yesterday','love was such an easy game','to play',
               'Now I need a place to hide','away','Oh,','I believe','in yesterday','Mm mm mm mm mm mm mm']
#delay_array = [4.2, 8.098, 13.0, 16.768, 19.32, 21.80, 24.32, 27.32, 30.32, 34.32]
delay_array = [4.4, 7.82, 12.66, 16.85, 19.53, 22.10, 25.40, 27.32, 30.28, 31.46,34.32,36.72,39.19]
correction = 0.8

my_array = ['first', 'rebecca', 'allard', 'last','saved', 'beatles_minus']


class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None


@bot.message_handler(commands=['start'])
def process_start(message):
    try:
        chat_id = message.chat.id               
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Popular', 'Some Crap')
        msg = bot.reply_to(message, 'Choose the track', reply_markup=markup)
        bot.register_next_step_handler(msg, process_choose_category)
    except Exception as e:
        bot.reply_to(message, e)






def process_choose_category(message):
    try:
        chat_id = message.chat.id
        if (message.text is None):
            msg = bot.reply_to(message, 'Choose the track', reply_markup=markup)
            bot.register_next_step_handler(msg, process_start)
            return
            
        choose = message.text
        
        
        #add_songs_to_dict(message)
        if (choose == u'Popular'):
            chat_id = message.chat.id
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)            
            x = 0
            for char in my_array:
                if (verifier):
                    x+=1
                    #time.sleep(0.1)
                    #bot.send_message(chat_id, str(x) + " " + char)  
                    markup.add(char)                    
                    #markup.add(str(x) + " " + char)
                #bot.send_message(chat_id, str(x) + " " + char)            
            msg = bot.reply_to(message, 'Choose the track', reply_markup=markup)
            #print(song_dict)
            bot.register_next_step_handler(msg, after_song_is_chosen)
        else:
            if (choose == u'Some Crap'):
                markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                markup.add('Popular', 'Some Crap')
                msg = bot.reply_to(message, 'Choose the track', reply_markup=markup)
                msg = bot.reply_to(message, 'We don\'t have crap.', reply_markup=markup)
                bot.register_next_step_handler(msg, process_choose_category)
            else:
                raise Exception()
    except Exception as e:
        bot.reply_to(message, e)
    

def after_song_is_chosen(message):
    try:
        #song_dict['rebecca'] = 'BQADAgADCgADQwjCDjQKgMQTctO-Ag'
        #rebecca BQADAgADCgADQwjCDjQKgMQTctO-Ag
        #audio = open('music/' + message.text +'.mp3', 'rb')
        #audio = open('music/' + message.text +'.mp3', 'rb')
        #audio = open('http://promodj.com/download/5971262/Dj%20Impuls-%D0%9F%D1%80%D0%B8%D1%8F%D1%82%D0%BD%D1%8B%D0%B9%20%D0%B2%D0%B5%D1%87%D0%B5%D1%80%20%28promodj.com%29.mp3')
        res = bot.send_audio(message.chat.id, song_dict[message.text]);
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Start lyrics')        
        msg = bot.reply_to(message, 'Start the song and press this button', reply_markup=markup)
        bot.register_next_step_handler(msg, after_song_is_delivered)
        
        #print(res)
        #bot.reply_to(message, "You chose: " + message.text)
    except Exception as e:
        bot.reply_to(message, e)

verifier = True
def after_song_is_delivered(message):
    try:        
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.row('Stop')
        msg = bot.reply_to(message, 'Press here to stop the lyrics', reply_markup=markup)
        bot.register_next_step_handler(msg, after_stop_is_pressed)
        i = 0
        start_time = time.clock()
        
        previous_current = start_time
        prev = 0
        
        #print((user_dict['verifier'] == 'True') & (i < len(words_array)))
        while ((user_dict['verifier'] == 'True') & (i < len(words_array))):
            current_time = time.clock()
            
            if (i == 0):
                previous_current = current_time
         #   print(delay_array[i] - correction - prev - (current_time - start_time - prev))
            time.sleep(delay_array[i] - correction - prev - (current_time - start_time - prev))
            if (user_dict['verifier'] == 'True'):
                bot.send_message(message.chat.id, words_array[i])
                prev = delay_array[i]
                i+=1
                if (len(delay_array) == i):                
                    bot.send_message(message.chat.id, 'Lyrics ended')
                    break
            
            
            
            
        enable_verifier()
##        for char in words_array:
##            if (False != check_verifier):
##                bot.send_message(message.chat.id, char + " " +str(verifier))
##                time.sleep(2)
            
            
    except Exception as e:
        bot.reply_to(message, e)

def disable_verifier():
    user_dict['verifier'] = 'False'
    
def enable_verifier():
    user_dict['verifier'] = 'True'

def after_stop_is_pressed(message):
    disable_verifier()
    try:
        chat_id = message.chat.id               
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Popular', 'Some Crap')        
        msg = bot.reply_to(message, 'Choose the track', reply_markup=markup)
        bot.register_next_step_handler(msg, process_choose_category)
    except Exception as e:
        bot.reply_to(message, e)
#    process_age_step(message)


    

##printing array with numbers
##my_array = ['first', 'rebecca', 'allard', 'last']
##        if (sex == u'Popular'):
##            x = 0
##            for char in my_array:
##                bot.send_message(chat_id, str(x) + " " + char)                
##                x+=1
##        else:
##            raise Exception()



def add_songs_to_dict(message):
    try:
        #updates = bot.get_updates()
        #updates = bot.get_updates(1234,100,200)
        #my_array = ['saved','first', 'rebecca', 'allard', 'last', 'beatles_beep1']        
        x = 0
        for char in my_array:
            audio = open('music/' + char +'.mp3', 'rb')        
            res = bot.send_audio(message.chat.id, audio, 100, 'eternnoir', 'pyTelegram');
            song_dict[char] = res.audio.file_id
            print(res)
        print(song_dict)
    except Exception as e:
        bot.reply_to(message, e)
        
## printing song_dictionary for uploaded
##for char in my_array:
##                if (verifier):
##                    x+=1
##                    markup.add(char)
##                    audio = open('music/' + char +'.mp3', 'rb')        
##                    res = bot.send_audio(message.chat.id, audio);
##                    song_dict[char] = res.audio.file_id
##                    print(res)
##                    #markup.add(str(x) + " " + char)
##                #bot.send_message(chat_id, str(x) + " " + char)            
##            msg = bot.reply_to(message, 'Choose the track', reply_markup=markup)
##            print(song_dict)



bot.polling()
