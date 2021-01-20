# TODO FIGURE OUT WHY ON THIS ALG DO NOT WORKS WITH LOWERCASE LATTERS
def shifr(num, mul_times, modul):
    mul_iterations = mul_times
    val = num * num
    while mul_iterations != 0:
        val = val % modul
        val *= num
        mul_iterations -= 1
    return val % modul


public_key = 5
char_key = 67
private_key = 29
number = 21
a_num = 13
b_num = 7
modulec = a_num * b_num

slovo = "i ANTI SHIFR WORKS!! realy"
shifrovan_list = []
answer_list = []

for char in slovo:
    shifrovan_list.append(shifr(ord(char), public_key, modulec))
print(*shifrovan_list)

for num in shifrovan_list:
    answer_list.append(chr(shifr(num, private_key, modulec)))
print(*answer_list)
