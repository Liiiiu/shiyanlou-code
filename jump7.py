a = 0
while(a <= 99):
    a = a + 1
    if a % 7 == 0: #如果是七的倍数跳过循环
        continue
    elif a % 10 == 7: #个位是七
        continue
    elif a // 10 == 7: #十位是七
        continue
    else:
        print(a)
