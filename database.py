import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    host="db",
    user="postgres",
    password="postgres",
    port="5432"
)

def get_cursor():
    global conn
    return conn.cursor()