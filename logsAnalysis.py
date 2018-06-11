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


# Who are the most popular article aurthors of all time?
query2 = """
         SELECT authors.name, COUNT(*) AS views
         FROM articles
         INNER JOIN authors ON articles.author = authors.id
         INNER JOIN log ON log.path ILIKE CONCAT('%', articles.slug, '%')
         WHERE log.status ILIKE '%200%'
         GROUP BY authors.name
         ORDER BY views DESC
         LIMIT 3;
         """


def pop_aut(cursor):
    cursor.execute(query2)


# On which days did more than 1% of requests lead to errors?
query3 = """
         WITH requests AS (
            SELECT  time::date AS day, COUNT(*)
            FROM log
            GROUP BY time::date
            ORDER BY time::date
            ), errors AS (
            SELECT time::date AS day, COUNT(*)
            FROM log
            WHERE status = '404 NOT FOUND'
            GROUP BY time::date
            ORDER BY time::date
            ), rate_error AS (
            SELECT requests.day,
            errors.count::float/requests.count::float * 100
            AS percent_error
            FROM requests, errors
            WHERE requests.day = errors.day
            )
            SELECT *
            FROM rate_error
            WHERE percent_error > 1;
         """


def error_days(cursor):
    cursor.execute(query3)


