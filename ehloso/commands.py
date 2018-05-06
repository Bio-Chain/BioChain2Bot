import subprocess
import MySQLdb
import subprocess
from private import CHATID

class Commands:
    def __init__(self, pybot):
        self.pybot=pybot
        
    def checkrepo(self, bot, update):
        p=subprocess.Popen("git pull", stdout=subprocess.PIPE, shell=True)
        stdo, err = p.communicate()
        self.sendMessage(stdo)

    def newMember(self, bot, update):
        pass
    
    def memberLeft(self, bot, update):
        pass
    
    def sendMessage(self, text):
        self.pybot.updater.bot.sendMessage(
            chat_id=CHATID,
            text=text,
            parse_mode='markdown'
        )
