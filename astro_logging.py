import db_connection

db_file = r"db"

conn = db_connection.create_connection(db_file)


def logging():
    while True:
        option = input("What do you want to do?\n\tA. Create new log\n\tB. View previous log?").lower().strip()
        if option in ['a', 'b']:
            break
        else:
            print("Invalid option")
            continue

