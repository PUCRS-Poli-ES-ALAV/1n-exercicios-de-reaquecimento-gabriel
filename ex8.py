def ex8(string, iter = 0):
    pos1 = iter
    pos2 = len(string)-1 -iter
    print(pos2)
    if (pos2 == 0 and (string[pos1] == string[pos2])):
        return True
    elif  (string[pos1] != string[pos2]):
        return False
    else:
        return ex8(string,iter+1)
    
print(ex8("aba"))