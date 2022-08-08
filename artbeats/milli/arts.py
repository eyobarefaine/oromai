import psycopg2
class Arts:
    def __init__(self, id):
        self.id=id


    def getTitle(self):
        conn = psycopg2.connect(database="artbeats", user="eyob", password="m1ll10n", host="0.0.0.0", port="5432")

        cur = conn.cursor()
        cur.execute("SELECT * from ARTS where id =%s", [self.id])

        rows = cur.fetchall()

        for row in rows:
            rv = row[2]

        conn.close()

        return rv
    def getTeaser(self):
        conn = psycopg2.connect(database="artbeats", user="eyob", password="m1ll10n", host="0.0.0.0", port="5432")

        cur = conn.cursor()
        cur.execute("SELECT * from ARTS where id =%s", [self.id])

        rows = cur.fetchall()

        for row in rows:
            rv = row[3]

        conn.close()

        return rv
