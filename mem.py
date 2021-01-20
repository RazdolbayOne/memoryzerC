import random


def mem_word(show_list, back_list):
    index = random.randint(0, len(show_list) - 1)
    old_index = index
    i = 0
    while i < len(show_list):
        print(show_list[index])
        input()
        print(back_list[index])
        print("-----------------------------")
        while index == old_index:
            index = random.randint(0, len(show_list) - 1)

        old_index = index
        i += 1


chinese_pinyin = ["Xiàmiàn", "Shàngmiàn", "Lǐ", "Qiánmiàn", "Hòumiàn"]
chinese_chars = ["下面", "上面", "里", "前面", "后面"]
english = ["below", "above", "in", "front", "behind"]
combination = []
for i in range(len(chinese_pinyin)):
    combination.append(chinese_chars[i] + chinese_pinyin[i])

still_working = True
switch = 1
while still_working:
    if switch == 1:
        mem_word(combination, english)
    else:
        mem_word(english, combination)
    print("to get out pres 'q' otherwise anykay")
    print("to switch shows press s")
    inp = input()
    if (inp == 'q'):
        still_working = False
    elif (inp == 's'):
        if switch != 1:
            switch = 1
        else:
            switch = 2
    # cleans screen
    for i in range(10):
        print()
