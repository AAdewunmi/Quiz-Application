# quiz.py

# Get user input with input()

answer = input("When was the first known use of the word 'quiz'?")
if answer == '1781':
    print("Correct")
else:
    print(f"The answer is '1781', not {answer!r}")

answer = input("Which builtin function can get information from the user?")
if answer == 'input()':
    print("Correct!")
else:
    print(f"The answer is 'input()', not {answer!r}")

