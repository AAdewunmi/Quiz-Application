# quiz.py
from typing import Dict, List

QUESTIONS: dict[str, list[str]] = {
    "When was the first known use of the word 'quiz'": ['1781', '1771', '1871', '1881'],
    "Which built-in function can get information from the user": ['input', 'get', 'print', 'write'],
    "Which keyword do you use to loop over a given list of elements": ['input', 'get', 'print', 'write'],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
}
print('Welcome to Python Quiz', '\n', '****************')
for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    for alternative in sorted(alternatives):
        print(f"  - {alternative}")

    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")


