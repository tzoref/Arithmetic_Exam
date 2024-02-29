import math
import random


def basic_operations_task():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    operator = random.choice(["+", "-", "*"])
    task = (str(a) + " " + operator + " " + str(b))
    print(task)
    correct = eval(task)
    return correct


def integral_squares_task():
    integer = random.randint(11, 29)
    print(integer)
    correct = integer ** 2
    return correct


def check_task(num):
    user_answer = " "
    while not user_answer.isnumeric():
        try:
            user_answer = input()
            message = "Incorrect Format"
            assert (user_answer.strip('-')).isnumeric(), message
            if int(user_answer) == num:
                check = "Right!"
            else:
                check = "Wrong!"
            print(check)
            return check
        except AssertionError as err:
            print(err)


# Executing the test
difficulty_msg = ("Which level do you want? Enter a number:\n"
                  "1 - simple operations with numbers 2-9\n"
                  "2 - integral squares of 11-29")
level = " "
while level != "1" and level != "2":
    print(difficulty_msg)
    level = input()
    if level == "1":
        level_description = "simple operations with numbers 2-9"
        n = 0
        for i in range(5):
            answer = basic_operations_task()
            mark = check_task(answer)
            if mark == "Right!":
                n += 1
        print(f'Your mark is {n}/5')
        break
    elif level == "2":
        level_description = "integral squares 11-29"
        n = 0
        for i in range(5):
            answer = integral_squares_task()
            mark = check_task(answer)
            if mark == "Right!":
                n += 1
        print(f'Your mark is {n}/5')
        break

save_file_query = "Would you like to save your result to the file? Enter yes or no."
print(save_file_query)
file_reply = input()
affirmative = ['yes', 'YES', 'y', 'Yes']
if file_reply in affirmative:
    name_query = "What is your name?"
    print(name_query)
    name = input()
    score_file = open('results.txt', 'a')
    score_file.write(f'{name}: {n}/5 in level {level} ({level_description})')
    score_file.close()
    print('The results are saved in "results.txt"')
else:
    exit()
