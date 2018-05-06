from collections import defaultdict

class User:
    def __init__(self, username):
        self.username = username
        self.nexts = defaultdict(int)
        self.prevs = defaultdict(int)
    
    def killLinks(self, user):
        for user in self.nexts.keys():
            self.nexts[user]=0
        for user in self.prevs.keys():
            self.prevs[user]=0
    
    def addNext(self, user):
        user=self.getUser(str(user))
        self.nexts[user]=1
        return True
        
    def addPrev(self, user):
        user=self.getUser(str(user))
        self.prevs[user]=1
        return True
        
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
        for user in [x for x in self.nexts.keys() if self.nexts[x] is 1]:
            for chain in user.getNextChains():
                if self.username not in chain:
                    yield [str(user)] + [chain]
    
    def getPrevChains(self):
        for user in [x for x in self.prevs.keys() if self.prevs[x] is 1]:
            for chain in user.getPrevChains():
                if self.username not in chain:
                    yield [chain] + [str(user)]
                    
    def __str__(self):
        return self.username
