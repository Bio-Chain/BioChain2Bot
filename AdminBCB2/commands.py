from private import CHATID
from database import Database

class Commands:
    def __init__(self, pybot):
        self.bot = pybot.updater.bot
        self.database = Database()
    
    def newMembers(self, bot, update):
        print "New Member"
        for member in update.message.new_chat_members:
            self.checkMember(member.id)
        
    def checkMember(self, id):
        members = [x["user_id"] for x in self.database.select("users")]
        if id in members:
            self.bot.restrict_chat_member(CHATID, id)
        else:
            self.bot.kick_chat_member(CHATID, id)
