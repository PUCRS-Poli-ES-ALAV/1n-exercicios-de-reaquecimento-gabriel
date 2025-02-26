def ex4(string,iter=0):
    if iter == len(string):
        return ''
    if len(string) == 0:
        return string
    return string[len(string)-iter-1] + ex4(string,iter+1)
a = "hello"
# print(a[len(a)-1])
print(ex4("hello"))