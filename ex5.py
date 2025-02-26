def ex5(n):
    if n < 1: return 0
    if n ==1 or n==2:
        return n
    else: return 2 * ex5(n-1) + 3 * ex5(n-2)


print(ex5(4))