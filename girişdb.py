import sqlite3

class database():
    def __init__(self):
        self.connection()

    def connection(self):
        self.connect =sqlite3.connect("database.db")
        self.cursor =self.connect.cursor()
        code = "CREATE TABLE IF NOT EXISTS DATABASE( username TEXT, password TEXT)"
        self.cursor.execute(code)
        self.connect.commit()

    def disconnect(self):
        self.connect.close()

    def controlu(self,username):
        #sadece kullanıcı adını kontrol eder
        code = "SELECT username FROM DATABASE"
        self.cursor.execute(code)
        users = self.cursor.fetchall()
        for i in users:
            if(username == i):
                return True
        return False
    def controlp(self,username,password):
        #kullanıcıyı kontrol eder
        code = "SELECT * FROM DATABASE"
        self.cursor.execute(code)
        list = self.cursor.fetchall()
        for i,j in list:
            if(i == username and j == password):
                return True
        return False
    def adduser(self,username,password):
        self.cursor.execute("INSERT INTO DATABASE VALUE({},{})".format(username, password))
        self.connect.commit()




