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


def select_log(conn, amount):
    """
    Create a new task
    :param conn:
    :param amount:
    :return:
    """

    sql = '''SELECT * FROM log
ORDER BY timestamp desc
LIMIT ? '''
    cur = conn.cursor()
    cur.execute(sql, amount)
    result = cur.fetchall()
    return result


def new_log(conn):
    astronaut_name = input("Who is making this log? ")
    content = input("What is the content? ")
    log_message = (astronaut_name, content)
    row_id = insert_log(conn, log_message)
    print(row_id)


def get_log(conn):
    number_of_logs = input("How many logs do you want to retrieve? ")
    logs = select_log(conn, number_of_logs)
    for log in logs:
        print("Log number {} by {} on {}: {}".format(log[0], log[1], log[3], log[2]))
