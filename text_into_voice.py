import telebot
import os
from dotenv import load_dotenv
from telebot import types as ty
import db
from gtts_ import speech_

path = os.path.join(os.path.dirname(__file__), 'env')
load_dotenv(path)

tb = telebot.TeleBot(os.getenv('TOKEN'))


@tb.message_handler(commands=['start'])
def start_(m):
    key_ = ty.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    key_.row('voice', 'audio')
    db.create_user(m.from_user.id)
    tb.send_message(chat_id=m.chat.id, text='Hi!', reply_markup=key_)


@tb.message_handler(func=lambda message: True)
def mes_(m):
    if m.text in ['voice', 'audio']:

        db.change_state(m.from_user.id, format_='audio' if m.text == 'audio' else 'OGG')
        tb.send_message(chat_id=m.chat.id, text='Okay!, send me some text!')

    else:
        audio = speech_(m.text)
        key_ = ty.ReplyKeyboardMarkup(
            resize_keyboard=True, one_time_keyboard=True
        )
        key_.row('voice', 'audio')
        state_ = db.give_state(m.from_user.id)
        if  state_ == 'OGG':

            tb.send_voice(chat_id=m.chat.id, voice=audio, reply_markup=key_)
            db.change_state(m.from_user.id)
            
        elif state_ == 'audio':

            tb.send_audio(chat_id=m.chat.id, audio=audio, reply_markup=key_)
            db.change_state(m.from_user.id)


tb.polling(none_stop=True)
