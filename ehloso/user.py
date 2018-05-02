class User:
    def __init__(self, username):
        self.username = username
        self.nexts = []
        self.prevs = []
    
    def addNext(self, user):
        self.nexts.append(user)
        
    def addPrev(self, user):
        self.prevs.append(user)
        
    def isStart(self):
        if len(self.prevs) is 0:
            return True
        else:
            return False
        
    def isEnd(self):
        if len(self.nexts) is 0:
            return True
        else:
            return False
        
    def getNextChains(self):
        for user in self.nexts:
            for chain in user.getNextChains():
                if self.username not in chain:
                    yield [user.username] + [chain]
    
    def getPrevChains(self):
        for user in self.prevs:
            for chain in user.getPrevChains():
                if self.username not in chain:
                    yield [chain] + [user.username]
                    
