import status
import astro_logging
import trivia


def op_a():
    i = astro_logging.logging()
    return i()


def op_b():
    i = status.status()
    return i()


def op_c():
    i = trivia.get_questions()
    return i()


def op_d():
    i = quit()
    return i()


def get_options():
    while True:
        option = input(
            "What would you like to do? \n\tA. Access logging\n\tB. View current status.\n\tC. Play a game of "
            "Trivia\n\tD. Quit ").strip().lower()
        if option not in ['a', 'b', 'c', 'd']:
            print("Invalid choice")
            continue
        else:
            break
    option_dict = {'a': op_a, 'b': op_b, 'c': op_c, 'd': op_d}

    def execute(args):
        func = option_dict.get(args, 'null')
        return func()
    execute(option)


if __name__ == "__main__":
    get_options()
