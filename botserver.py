#!/usr/bin/python

from telegram.ext import Updater, MessageHandler, Filters
import socket
import sys
import os
import commands
import private

class Bot:
    def __init__(self):
        self.botInit()
        #TODO Better port/host input
        port = 12345
        host = socket.gethostname()
        server = socket.socket()
        server.bind((host, port))
        server.listen(5)
        while True:
            conn, addr = server.accept()
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
    
    def telegramInput(self, bot, update):
        message = update.message
        command_split = message.text[1:].split(' ')
        command_args = command_split[1:] or []
        command = command_split[0].lower().split('@')
        directed = bool(command[1:])
        command.append(bot.username)
        if command[1].lower() != bot.username.lower():
            # this command is not for us
            return
        try:
            getattr(commands, 'cmd_' + command[0].lower())(update=update, bot=self, args=command_args)
        except AttributeError:
            if directed:
                commands.cmd_unknown(update=update, bot=self)
    
    def telegramNewMember(self, bot, update):
        commands.cmd_newMember(update=update, bot=self)
        
    def telegramMemberLeft(self, bot, update):
        commands.cmd_memberLeft(update=update, bot=self)
        
    def telegramError(self, bot, update, error):
        commands.cmd_error(update=update, bot=self, args=[error])
        
    def clientInput(self, data):
        command_split = data.split(' ')
        command_args = command_split[1:] or []
        command = command_split[0].lower()
        try:
            return getattr(commands, 'cmd_' + command)(bot=self, args=command_args)
        except AttributeError:
            return commands.cmd_unknown(bot=self)
    
    def __del__(self):
        self.updater.stop()

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
        
