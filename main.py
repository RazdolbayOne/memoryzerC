# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def memorizer(name_list, answer_list):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    word_length = (len(answer_list) - 1)
    index = random.randint(0, word_length)
    i = 0
    while (i != word_length):
        print("--------------")
        print(name_list[index])
        input()
        print(answer_list[index])
        print()
        index = random.randint(0, word_length)
        i += 1
    print("--------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    names = "(女儿) (几) (岁) (了) (今年) (有) (家) 口"
    answers = "daughter howMany yearOld newCircs thisYear toHave family measureWord"
    name_list = names.split()
    answers_list = answers.split()

    memorizer(name_list, answers_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
