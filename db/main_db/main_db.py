import psycopg2

conn = psycopg2.connect(dbname="", user="", password="", host="...", port="")
cursor = conn.cursor()
cursor.execute('select * from ')
records = cursor.fetchall()
print(records)
cursor.close()
conn.close()
