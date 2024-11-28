import random
x = 'qalesoz'
def func():
    global x
    x = 'salom'

func()



ls = [('a', 12), ('s', 43)]
d, e = ls
dc = dict()
for i in ls:
    dc[i[0]] = i[1]
print(dc)
print(*i)
print(*d, *e)
print(*ls)












# parol = 1001
# def parol_top(parol):
#     if isinstance(parol, int):
#         while True:
#             pasword = random.randint(1000, 9999)
#             if pasword == parol:
#                 print('parol topildi ', pasword)
#                 break
#             print(pasword)

# parol_top(parol)