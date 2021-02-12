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


chinese_pinyin =  ["Zhù","Qián","Běijīng","Diànshì"]#["Chuáng","Guìzi","Shūjià","Zhuōzi","Yǐzi","Dēng","Dìtǎn","Zhàopiàn","Bēizi","Fángjiān"] #["Zǎoshang","Shàngwǔ","Zhōngwǔ","Xiàwǔ","Wǎnshàng"] #["Xiàmiàn", "Shàngmiàn", "Lǐ", "Qiánmiàn", "Hòumiàn"]
chinese_chars =  ["住","前","北京","电视"]#["床","柜子","书架","桌子","椅子","灯","地毯","照片","杯子","房间"]  #["早上","上午","中午","下午","晚上"] #["下面", "上面", "里", "前面", "后面"]
english = ["to live,tostay","before,early then","Beijing","tv"]#["bed","cabinet","bookshelves","table","chair","lamp","carpet","photo","cup","room"] #["morning","forenoon","nooon","afternoon","evening"] #["below", "above", "in", "front", "behind"]
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
