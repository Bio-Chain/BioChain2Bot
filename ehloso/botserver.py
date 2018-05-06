#!/usr/bin/python

from telegram.ext import Updater, MessageHandler, Filters
import os
from commands import Commands
from private import TOKEN, CHATID

class Bot:
    def __init__(self):
        self.commands = Commands(self)
        self.updater = Updater(token=TOKEN)
        self.bot = self.updater.bot
        self.updater.dispatcher.add_handler(
            MessageHandler(Filters.status_update.new_chat_members & Filters.chat(CHATID), self.commands.newMember)
        )
        self.updater.dispatcher.add_handler(
            MessageHandler(Filters.status_update.left_chat_member & Filters.chat(CHATID), self.commands.memberLeft)
        )
        self.updater.dispatcher.add_handler(
            CommandHandler('checkrepo', self.commands.checkrepo, Filters.chat(CHATID))
        )
        
        self.updater.dispatcher.add_error_handler(self.commands.error)
        self.updater.start_polling()
        print "Telegram Bot Running. Press enter to stop..."
        raw_input()
        self.stop()
        
    def stop(self):
        print "Telegram Bot is stopping. Please wait..."
        self.updater.stop()
        print "Bye!"
        os._exit(0)

    def __del__(self):
        self.updater.stop()

if __name__ == "__main__":
    Bot()
        
