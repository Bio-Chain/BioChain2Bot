#!/usr/bin/python

from telegram.ext import Updater, MessageHandler, CommandHandler, Filters
from private import TOKEN, CHATID
import os
from commands import Commands

class Bot:
    def __init__(self):
        self.updater = Updater(token=TOKEN)
        self.commands = Commands(self)
        self.updater.dispatcher.add_handler(
            CommandHandler('update', self.commands.update, Filters.chat(CHATID))
        )
        self.updater.dispatcher.add_handler(
            CommandHandler('updateme', self.commands.updateme, Filters.chat(CHATID))
        )
        self.updater.dispatcher.add_handler(
            MessageHandler(Filters.status_update.new_chat_members & Filters.chat(CHATID), self.commands.newMembers)
        )
        self.updater.dispatcher.add_handler(
            MessageHandler(Filters.status_update.left_chat_member & Filters.chat(CHATID), self.commands.memberLeft)
        )
        self.updater.start_polling()
        print "Telegram Bot Running. Press enter to stop..."
        raw_input()
        self.stop()
        
    def stop(self):
        print "Telegram Bot is stopping. Please wait..."
        self.updater.stop()
        os._exit(0)
        
if __name__ == "__main__":
    Bot()
    
