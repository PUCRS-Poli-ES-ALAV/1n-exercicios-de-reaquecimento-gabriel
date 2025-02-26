def ex3(N):
    if N == 1 :
        return 1
    # if N == denon:
        # return 1 + 1/N
    else: return 1/N + ex3(N-1) 

print(ex3(2))