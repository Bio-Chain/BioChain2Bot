from chains import Chains
from database import Database

class Biochain:
    def __init__(self):
        self.chains=Chains()
        self.db=Database()
        for row in self.db.select("users"):
            self.chains.addLink(row["username"], row["follows"])
        self.current=self.chains.getLongestChain()
        
if __name__ is "__main__":
    bc = Biochain()
    print bc.current
        
