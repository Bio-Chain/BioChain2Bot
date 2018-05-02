from user import User
from private import CHATNAME

class Chains:
    def __init__(self, users=[], current=[]):
        self.users = [User(x) for x in users]
        
    def hasUser(self, username):
        for user in self.users:
            if user.username is username:
                return True
        return False
        
    def getUser(self, username):
        for user in self.users:
            if user.username is username:
                return user
        return False
        
    def addUser(self, username):
        if self.hasUser(username) is false:
            user = User(username)
            self.users.append(user)
            return user
        else:
            return False
        
    def addLink(self, username, followname):
        user = self.getUser(username) or self.addUser(username)
        follow = self.getUser(followname) or self.addUser(followname)
        user.addNext(follow)
        follow.addPrev(user)
        return True
    
    def getEndUsers(self, f=lambda x: return True):
        ends = []
        for user in self.users:
            if user.isEnd() and f(user):
                ends.append(user)
        return ends
    
    def getStartUsers(self, f=lambda x: return True):
        starts = []
        for user in self.users:
            if user.isStart() and f(user):
                starts.append(user)
        return starts
    
    def getLongestChain(self):
        longest = []
        for chain in self.getAllChains():
            if len(longest) < len(chain):
                longest = chain
        if longest is []:
            return False
        else:
            return longest
        
    def getAllChains(self):
        chat = self.getUser(CHATNAME)
        if chat is False:
            return []
        else:
            return chat.getPrevChains()
    
