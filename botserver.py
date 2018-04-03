#!/usr/bin/python

from telegram.ext import Updater, MessageHandler, Filters
import socket
import sys
import os
import commands
from private import *
from chain import Chain

class Bot:
    def __init__(self):
        self.botInit()
        self.chain = Chain(self.bot, "chain")
        #TODO Better port/host input
        port = 12345
        host = socket.gethostname()
        self.server = socket.socket()
        self.server.bind((host, port))
        self.server.listen(5)
        print "Socket Server active"
        while True:
            conn, addr = self.server.accept()
            print 'Connection from ', addr
            #TODO Implement some security
            data = conn.recv(1024)
            resp = self.clientInput(data)
            conn.send(resp)
            conn.close()
            
    def botInit(self):
        self.updater = Updater(token=TOKEN)
        self.bot = self.updater.bot
        self.updater.dispatcher.add_handler(MessageHandler(Filters.chat(CHATID) & Filters.command & (~Filters.forwarded), self.telegramInput))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, self.telegramNewMember))
        self.updater.dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, self.telegramMemberLeft))
        self.updater.dispatcher.add_error_handler(self.telegramError)
        self.updater.start_polling()
        print "Telegram Bot active"
    
    def telegramInput(self, bot, update):
        reload(commands)
        message = update.message
        command_split = message.text[1:].split(' ')
        command_args = command_split[1:] or []
        command = command_split[0].lower().split('@')
        command.append(bot.username)
        print "Telegram Command: ", command[0]
        if command[1].lower() != bot.username.lower():
            # this command is not for us
            return
        try:
            getattr(commands, 'cmd_' + command[0].lower())(update=update, bot=self, args=command_args)
        except AttributeError:
            commands.cmd_unknown(update=update, bot=self)
    
    def telegramNewMember(self, bot, update):
        reload(commands)
        print "New Member"
        commands.cmd_newMember(update=update, bot=self)
        
    def telegramMemberLeft(self, bot, update):
        reload(commands)
        print "Member Left"
        commands.cmd_memberLeft(update=update, bot=self)
        
    def telegramError(self, bot, update, error):
        reload(commands)
        print "Error"
        commands.cmd_error(update=update, bot=self, args=[error])
        
    def clientInput(self, data):
        reload(commands)
        command_split = data.split(' ')
        command_args = command_split[1:] or []
        command = command_split[0].lower()
        print "Client Command: ", command
        try:
            return getattr(commands, 'cmd_' + command)(bot=self, args=command_args)
        except AttributeError:
            return commands.cmd_unknown(bot=self)
    
    def __del__(self):
        self.updater.stop()
        self.server.close()

def exit():
    print 'Bye Bye!'
    try:
        sys.exit(0)
    except:
        os._exit(0)

if __name__ == "__main__":
    try:
        Bot()
    except KeyboardInterrupt:
        exit()
    except:
        try:
            while True:
                pass
        except:
            exit()
        
