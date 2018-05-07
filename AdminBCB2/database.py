from private import HOST, USER, PASSWD, DB
import MySQLdb, MySQLdb.cursors

class Database:
    def __init__(self):
        self.database = MySQLdb.connect(HOST,USER,PASSWD,DB,cursorclass=MySQLdb.cursors.DictCursor)
        self.cursor = self.database.cursor()
        
    def select(self, table, where=False):
        query="SELECT * FROM "+table
        if where is not False:
            where=', '.join([x+" = '"+str(where[x])+"'" for x in where.keys()])
            query = query + " WHERE " + where
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def insert(self, table, vals):
        coloums = []
        values = []
        for col in vals.keys():
            coloums.append(col)
            values.append("'"+str(vals[col])+"'")
        coloums = ', '.join(coloums)
        values = ', '.join(values)
        try:
            self.cursor.execute("""INSERT INTO %s (%s) VALUES (%s)""" % (table,coloums,values))
            self.database.commit()
            return True
        except:     
            self.database.rollback()
            return False
        
    def update (self, table, set, where):
        set = ', '.join([x+" = "+str(set[x]) for x in set.keys()])
        try:
            self.cursor.execute ("""UPDATE %s SET %s WHERE %s""" % (table, set, where))
            self.database.commit()
            return True
        except:
            self.database.rollback()
            return False

    def remove(self, table, where):
        where = ', '.join([x+" = '"+str(where[x])+"'" for x in where.keys()])
        try:
            self.cursor.execute("DELETE FROM %s WHERE %s" % (table, where))
            self.database.commit()
            return True
        except:
            self.database.rollback()
            return False
        
if __name__ == "__main__":
    db=Database()
    print db.select("users")
    print db.insert("users", {"user_id":1})
    print db.select("users")
    print db.update("users", {"user_id":2}, "user_id = 1")
    print db.select("users")
    print db.remove("users", "user_id = 2")
    print db.select("users")
