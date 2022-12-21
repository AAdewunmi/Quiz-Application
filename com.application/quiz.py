# quiz.py

import pathlib
import random
from string import ascii_lowercase

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 11
QUESTIONS_PATH = pathlib.Path(__file__).parent / "/Users/adrianadewunmi/PyCharm/GitHub_Projects/Quiz-Application/com.application/questions.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())


def prepare_questions(path, num_questions):
    questions = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)


def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"    {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]


def ask_question(question, alternatives):
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0


def run_quiz():
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
    )
    num_correct = 0
    num = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    print(f'\nYou got {num_correct} correct out of {num} questions')


if __name__ == "__main__":
    run_quiz()
