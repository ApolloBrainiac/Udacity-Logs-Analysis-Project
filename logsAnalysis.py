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


# What are the three most popular articles of all time?
query1 = """
         SELECT articles.title, COUNT(*) AS views
         FROM articles
         INNER JOIN log ON log.path ILIKE CONCAT('%', articles.slug, '%')
         WHERE log.status ILIKE '%200%'
         GROUP BY articles.title
         ORDER BY views DESC
         LIMIT 3;
         """


def pop_art(cursor):
    cursor.execute(query1)