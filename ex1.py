def ex1(n,x): # n*x
    if n ==1:
        return x
    else :
        return x + ex1(n-1,x)

print(ex1(2,6))