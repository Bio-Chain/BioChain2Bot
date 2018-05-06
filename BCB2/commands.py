from biochain import Biochain
from private import CHATID

class Commands:
    def __init__(self, pybot):
        self.pybot = pybot
        self.biochain = Biochain(self)
    
    def update(self, bot, update):
        print "/update"
        self.biochain.update()
        
    def updateme(self, bot, update):
        print "/updateme"
        self.biochain.updateuser(update.message.from_user.id, update.message.from_user.username)
    
    def newMembers(self, bot, update):
        print "New Member"
        for member in update.message.new_chat_members:
            if member.is_bot:
                continue
            elif hasattr(member, "username"):
                self.biochain.addMember(id=member.id, username=member.username)
            else:
                self.biochain.addMember(id=member)
            
    def memberLeft(self, bot, update):
        print "Member Left"
        self.biochain.removeMember(id=update.left_chat_member.id)
        
    def send(self, msg):
        self.pybot.updater.bot.send_message(CHATID, msg)
        
