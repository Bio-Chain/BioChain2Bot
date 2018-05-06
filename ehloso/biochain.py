from chains import Chains
from database import Database

class Biochain:
    def __init__(self):
        self.chains=Chains()
        self.db=Database()
        for row in self.db.select("users"):
            self.chains.addLink(row["username"], row["follows"])
        self.current=self.chains.getLongestChain()
        
    def updateChain(self):
        for user in self.chains.getUsers():
            bios = self.getBio(user)
            for bio in bios:
                self.chains.addLink(user, bio)
        return self.chains.getLongestChain()
        
    def getBio(user, username):
        username=str(username)
        RE_USERNAME = re.compile(r'@([a-zA-Z][\w\d]{4,31})')
        r = requests.get("http://t.me/" + username)
        if not r.ok:
            raise NetworkException("NE for "+username)
        bio = RE_USERNAME.findall(r.text)
        bio.remove(username)
        return bio

class NetworkException(Exception):
    pass

if __name__ is "__main__":
    bc = Biochain()
    print bc.current
        
