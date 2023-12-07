import random

s = input()


def hashing(seq: str) -> tuple:

    n = len(seq)
    mod = 10 ** 9 + 7
    x_ = 257
    x = [0] * (n + 1)
    x[0] = 1
    h = [0] * (n + 1)
    for i in range(1, n + 1):
        x[i] = (x[i-1] * x_) % mod
        h[i] = (h[i-1] * x_ + ord(seq[i-1])) % mod

    return x, h


def equal(x: list[int], h: list[int], l: int, f1: int, f2: int) -> bool:
    return (h[f1+l] + h[f2] * x[l]) % (10 ** 9 + 7) == (h[f2+l] + h[f1] * x[l]) % (10 ** 9 + 7)


def order(x: list[int], h: list[int], f1: int, f2: int, seq: str) -> bool:

    l, r = 0, len(seq) - max(f1, f2)
    eq = 0
    while l <= r:
        m = (l + r) // 2
        flag = equal(x, h, m, f1, f2)

        if flag:
            l = m + 1
            eq = m
        else:
            r = m - 1

    last1 = ord(seq[f1 + eq]) if f1 + eq < len(seq) else -1
    last2 = ord(seq[f2 + eq]) if f2 + eq < len(seq) else -1
    return last1 < last2

sufix = list(range(len(s)))
x, h = hashing(s)


def sort(arr: list):

    def treepointpart(l, r, pivot):
        n, g, e = l, l, l
        while n <= r:
            if order(x, h, arr[n], pivot, s):
                y = arr[n]
                arr[n] = arr[g]
                arr[g] = arr[e]
                arr[e] = y
                e += 1
                g += 1
            n += 1
        return e, g

    def quicksort(l, r):
        if l < r:
            pivot = arr[random.randint(l, r)]
            e, g = treepointpart(l, r, pivot)
            quicksort(l, e - 1)
            quicksort(g, r)

    quicksort(0, len(s) - 1)

sort(sufix)

for i in range(len(sufix)):
    print(s[sufix[i]:])
