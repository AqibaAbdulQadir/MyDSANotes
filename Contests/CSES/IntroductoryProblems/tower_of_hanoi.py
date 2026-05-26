n = int(input())


def tower(n, fro, to, aux):
    if n == 0: return
    tower(n-1, fro, aux, to)
    print(fro, to)
    tower(n-1, aux, to, fro)

print(2**n-1)
tower(n, 1, 3, 2)
