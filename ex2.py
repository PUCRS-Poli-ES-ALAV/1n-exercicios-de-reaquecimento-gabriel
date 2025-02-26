def ex2(num):
    if num <=0:
        return num
    elif num == 1:
        return 1
    else: return num + ex2(num-1)


print(ex2(5))