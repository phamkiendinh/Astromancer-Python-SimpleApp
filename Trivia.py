import requests
import base64
import random


def decode_utf(entry):
    input_bytes = entry.encode('ascii')
    base64_bytes = base64.b64decode(input_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message


def get_questions():
    num = 0
    while True:
        try:
            num = int(input("Welcome to Trivia, how many questions would you like to play?(Max 10) ").strip())
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        break
    request = requests.get('https://opentdb.com/api.php?amount={}&type=multiple&encode=base64'.format(num))
    result = request.json()['results']
    correct_count = 0
    for i in range(num):
        questions = result[i]
        category = decode_utf(questions['category'])
        difficulty = decode_utf(questions['difficulty'])
        question = questions['question']
        correct_answer = questions['correct_answer']
        answers = questions['incorrect_answers'] + [correct_answer]
        a = random.choice(answers)
        answers.remove(a)
        b = random.choice(answers)
        answers.remove(b)
        c = random.choice(answers)
        answers.remove(c)
        d = random.choice(answers)
        answer_dict = {'a': a, 'b': b, 'c': c, 'd': d}
        print("Question {}. This is a/an {} question and the category is: {}".format(i + 1, difficulty, category))
        print(decode_utf(question))
        print("A. " + decode_utf(a))
        print("B. " + decode_utf(b))
        print("C. " + decode_utf(c))
        print("D. " + decode_utf(d))
        while True:
            user_answer = input().lower().strip()
            if user_answer not in ['a', 'b', 'c', 'd']:
                print("Invalid input.")
                continue
            else:
                break

        if answer_dict[user_answer] == correct_answer:
            print("Congratulation, you are correct!")
            correct_count += 1
        else:
            print("Incorrect. The correct answer is {}.".format(decode_utf(correct_answer)))
    print("Congrats! You got {} out of {} questions correct.".format(correct_count, num))
    if input("Do you want to play again?(Y/N)").strip().lower() == 'y':
        get_questions()


if __name__ == "__main__":
    get_questions()
    quit()
