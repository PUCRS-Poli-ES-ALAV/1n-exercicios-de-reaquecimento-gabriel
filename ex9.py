alphabet = "abcdefghijklmnopqrstuvwxyz".upper()
# print(alphabet[:4])

def permut(list, prefix=""):
    if not list:
        print(prefix)
    else:
        for i in range(len(list)):
            actual_prefix = prefix + list[i]
            restante = list[:i] + list[i+1:]
            permut(restante, actual_prefix)

def func(n):
    leters = list(alphabet[:n])
    permut(leters)


func(3)
