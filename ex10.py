def fibog(f0,f1,n):
    if n == 0:
        return f0
    elif n == 1:
        return f1
    else:
        return fibog(f0,f1,n-1) + fibog(f0,f1,n-2)
    
print(fibog(2,3,5))
