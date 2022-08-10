import psycopg2
from .connection import connector

class Arts:
    def __init__(self, id):
        self.id=id
        self.conn = connector.getConn(self)

    def getTitle(self):




        cur = self.conn.cursor()
        cur.execute("SELECT * from ARTS where id =%s", [self.id])

        rows = cur.fetchall()

        for row in rows:
            rv = row[2]



        return rv
    def getTeaser(self):

        cur = self.conn.cursor()
        cur.execute("SELECT * from ARTS where id =%s", [self.id])

        rows = cur.fetchall()

        for row in rows:
            rv = row[3]



        return rv

    def check(self, login, password):
        cur = self.conn.cursor()
        cur.execute("SELECT * from arts_admin where login=%s and password =%s ",[login, password])
        if cur.rowcount == 0:
            return False
        else:
            return True

    def getArts(self, rv):
        cur = self.conn.cursor()
        cur.execute("SELECT * from Arts where id=%s",[2])
        rows = cur.fetchone()
        return rows[rv]

    def saveArts(self,title):
        cur = self.conn.cursor()
        try:
           cur.execute("UPDATE Arts set arts_title=%s where id=%s", [title,2])
           print("success..............")
        except:
           print("something went wrong")
        return ""




