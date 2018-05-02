from private import HOST, USER, PASSWD, DB
import MySQLdb, MySQLdb.cursors

class Database:
    def __init__(self):
        self.db = MySQLdb.connect(HOST,USER,PASSWD,DB)
        self.cursor = self.db.cursor(dictionary=True)
        
    def select(self, table, where=False):
        query="SELECT * FROM "+table
        if where is not False:
            query = query + " WHERE " + where
        self.cursor.execute(query)
        return self.fetchall()
    
    def insert(self, table, values):
        try:
            coloums = []
            values = []
            for col in values.keys():
                coloums.append(col)
                values.append("'"+values[col]+"'")
            coloums = coloums.join(", ")
            values = values.join(", ")
            self.cursor.execute("""INSERT INTO %s (%s) VALUES (%s)""",(table,coloums,values))
            self.db.commit()
            return True
        except:     
            db.rollback()
            return False

if __name__ is "__main__":
    db = Database()
    db.inset(users, {"user_id":123, "username":"test", "follows":"testfollow"})
    print db.select("users", "username LIKE test")
    
