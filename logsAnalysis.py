import psycopg2


def db_connect():
    # Connects to DB and returns DB cursor
    try:
        conn = psycopg2.connect("dbname=news")
        cursor = conn.cursor()
    except:
        print("Failed to connect to database.")
        return None
    else:
        return cursor


