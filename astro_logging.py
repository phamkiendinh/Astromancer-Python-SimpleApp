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

    def op_a():
        print("The log number is {}".format(db_connection.new_log(conn)))

    def op_b():
        db_connection.get_log(conn)

    option_dict = {'a': op_a, 'b': op_b}

    def execute(args):
        func = option_dict.get(args, 'null')
        return func()

    execute(option)


if __name__ == '__main__':
    logging()
