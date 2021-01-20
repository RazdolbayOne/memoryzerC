a = 18
b = 30


def euklid(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


# print(euklid(645,381))

def shifr(num,mul_times,modul):
    mul_iterations=mul_times
    val=num*num
    while mul_iterations>0:
       val=val%modul
       val*=num
       mul_iterations-=1
    return val%modul


public_key=5
char_key=67
private_key=29
number=21
modulec=91

slovo="CLOUD"
shifrovan_list=[]
answer_list=[]

for char in slovo:
    shifrovan_list.append(shifr(ord(char),public_key,modulec))
print(*shifrovan_list)

for num in shifrovan_list:
    answer_list.append(chr(shifr(num,private_key,modulec)))
print(*answer_list)