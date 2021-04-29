import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def insert_log(conn, message):
    """
    Create a new task
    :param conn:
    :param message:
    :return:
    """

    sql = ''' INSERT INTO log(astronaut_name, content) VALUES (?,?)'''
    cur = conn.cursor()
    cur.execute(sql, message)
    conn.commit()
    return cur.lastrowid


def new_log(conn):
    astronaut_name = input("Who is making this log? ")
    content = input("What is the content? ")
    log_message = (astronaut_name, content)
    row_id = insert_log(conn, log_message)
    print(row_id)
