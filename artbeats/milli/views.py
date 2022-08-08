from django.http import HttpResponse
from django.template import loader
import psycopg2

def index(request):
  conn = psycopg2.connect(database="artbeats", user="eyob", password="m1ll10n", host="0.0.0.0", port="5432")

  cur = conn.cursor()
  cur.execute("SELECT * from ARTS")

  rows = cur.fetchall()
  for row in rows:
    print(row[0])

  conn.close()
  template = loader.get_template('index.html')
  context = {
    'title': 'Milli Artbeats Page'
  }
  return HttpResponse(template.render(context,request))