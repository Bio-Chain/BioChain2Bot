import core
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
###bot is the Bot class in bot.py

def welcome(bot, user):
    core.sendMessage(bot.bot, "Welcome! Please add @" + last + " in your bio!", 
                     rules_btn=InlineKeyboardMarkup(
                         [[InlineKeyboardButton(text='Read Rules',
                                               url='t.me/Bio_Chain_2_Rules')]]))
    
