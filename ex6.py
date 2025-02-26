def ex6(m,n):
    if m == 0:
        return n + 1
    elif n == 0 :
        return ex6(m-1,1)
    else: return ex6(m-1,ex6(m,n-1))

print(ex6(3,4))