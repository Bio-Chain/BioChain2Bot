from file_string import FileString

class Chain:
    def __init__(self, bot, filename):
        self.bot = bot
        self.filename
    
    def getChain(self):
        return FileString(self.filename)
    
    def getLast(self):
        return FileStrin(self.filename).getLines()[-1]
    
    def checkChain(self):
        chain = self.getChain().getLines()
        i=1
        broken=[]
        while i < len(chain):
            if chain[i-1] not in core.getBio(chain[i]):
                broken.append(chain[i])
            i=i+1
        return broken

    def add(self, name):
        self.getChain.append(name)
        return True
        
    def remove(self, name):
        chain = self.getChain().getLines()
        try:
            chain.remove(name)
            self.getChain().write(' '.join(chain))
            return True
        except ValueError:
            return False
        
