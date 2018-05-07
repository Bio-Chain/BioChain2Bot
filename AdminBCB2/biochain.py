import re
import requests
from private import CHATNAME
from database import Database
from collections import defaultdict

class Biochain:
    def __init__(self, commands):
        self.commands = commands
        self.database = Database()
        
    def getBio(self, username):
        RE_USERNAME = re.compile(r'@([a-zA-Z][\w\d]{4,31})')
        r = requests.get("http://t.me/" + username)
        if not r.ok:
            print("Networking Error: " + r.status_code)
            return False
        bio = RE_USERNAME.findall(r.text)
        bio = [x.lower() for x in set(list(filter(lambda x: x != username and x != "Telegram", bio)))]
        print username, "'s bio: ", bio
        return bio
        
    def addMember(self, id, username=False, follows=False):
        values={"user_id":id}
        if username:
            values["username"]=username.lower()
        if follows:
            values["follows"]=follows.lower()
        return self.database.insert("users", values)
    
    def removeMember(self, id=False, username=False):
        values={}
        if id is not False:
            values["user_id"]=id
        if username is not False:
            values["username"]=username.lower()
        return self.database.remove("users", values)
    
    def getChain(self):
        firstuser = CHATNAME
        chain = [firstuser]
        while True:
            select = self.database.select("users", {"follows":firstuser})
            if len(select) == 0:
                return chain
            else:
                chain = [select[0]["username"]] + chain
                firstuser = select[0]["username"]
    
    def update(self):
        chain = self.getChain()
        print chain
        actuallen = 0
        chainmsg = ""
        broken = []
        for i in range(0, len(chain)-1):
            if chain[i+1] not in self.getBio(chain[i]):
                actuallen = 0
                broken.append({chain[i]:chain[i+1]})
                chainmsg = chainmsg+chain[i]+" X "
            else:
                actuallen = actuallen+1
                chainmsg = chainmsg+chain[i]+" -> "
        if len(chain)-1 == actuallen:
            chainmsg = "Length: "+str(actuallen)+"\n"+chainmsg+"bio_chain_2"
        else:
            chainmsg = "Potential Length: "+str(len(chain)-1)+"\nActual Length: "+str(actuallen)+"\n"+chainmsg+"bio_chain_2"
        print "chain ", chainmsg
        self.commands.send(chainmsg)
        for b in broken:
            self.commands.send("@"+b+" point your bio to: "+broken[b])
                
    def updateUser(self, id, user):
        pass

if __name__ == "__main__":
    bc=Biochain(0)
    bc.update()
