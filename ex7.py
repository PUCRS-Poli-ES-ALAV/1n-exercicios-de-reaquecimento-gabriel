def ex7(arr, iter = 0):
    return aux1(arr), aux2(arr)    

def aux1(arr,iter = 0):
    if iter == len(arr)-1:
        return arr[-1]
    else:
        return arr[iter] + aux1(arr,iter+1)   
def aux2(arr, iter = 0):
    if iter == len(arr)-1:
        return arr[-1]
    else:
        return arr[iter]  * aux2(arr,iter+1)

arr = [1,2,3, 4]

print(ex7(arr))
