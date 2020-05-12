for i in range(1,101): #输出为1-100的数
    if (i % 7 == 0) or (i % 10 == 7) or (i // 10 ==7):
        continue  # 跳过当前循环
    print(i)
