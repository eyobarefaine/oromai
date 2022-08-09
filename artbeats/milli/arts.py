import psycopg2
from .connection import connector
class Arts:
    def __init__(self, id):
        self.id=id
        self.conn = connector.getConn(self)

    def getTitle(self):

        #conn = psycopg2.connect(database="artbeats", user="eyob", password="m1ll10n", host="0.0.0.0", port="5432")

        cur = self.conn.cursor()
        cur.execute("SELECT * from ARTS where id =%s", [self.id])

        rows = cur.fetchall()

        for row in rows:
            rv = row[2]

        self.conn.close()

        return rv
    def getTeaser(self):

        cur = self.conn.cursor()
        cur.execute("SELECT * from ARTS where id =%s", [self.id])

        rows = cur.fetchall()

        for row in rows:
            rv = row[3]

        self.conn.close()

        return rv

    def check(self, login, password):
        cur = self.conn.cursor()
        cur.execute("SELECT * from arts_admin where login=%s and password =%s ",[login, password])
        if cur.rowcount == 0:
            return False
        else:
            return True



