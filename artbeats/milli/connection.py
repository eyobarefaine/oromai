import psycopg2
class connector :
   def __init__(self):
      self
   def getConn(self):
    conn = psycopg2.connect(database="artbeats", user="eyob", password="m1ll10n", host="0.0.0.0", port="5432")
    return conn


