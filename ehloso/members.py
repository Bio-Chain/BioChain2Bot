from database import Database

class Members:
    def __init__(self):
        self.database = Database()
        self.members = self.database.select("users")
        for i in range(0, len(self.members)):
            self.members[i]["id"] = int(self.members[i]["id"])
        
    def get(self):
        return self.members
    
    def add(self, id, username=False):
        values={"user_id": str(id)}
        if username is not False:
            values["username"]=str(username)
        if self.database.insert("users", values):
            self.members.append({"id":id,"username":str(username)})
            return True
        else:
            return False
        
    def remove(self, id=False, username=False):
        if id is not False:
            if self.database.remove("users", "id == "+str(id)):
                for i in range(0, len(self.members)):
                    if self.members[i]["id"] == id:
                        self.members.pop(i)
                        return True
        if username is not False:
            if self.database.remove("users", "username == "+str(username)):
                for i in range(0, len(self.members)):
                    if self.members[i]["username"] == str(username):
                        self.members.pop(i)
                        return True
        return False
    
    def update(self, id, username):
        self.remove(id)
        self.add(id, username)
        
