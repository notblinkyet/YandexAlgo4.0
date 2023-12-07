def hashing(s):
    n = len(s)
    x_ = 257
    p = 10**9 + 7
    h = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    s = " " + s
    for i in range(1, n + 1):
        h[i] = (h[i - 1]*x_ + ord(s[i])) % p
        x[i] = (x[i - 1] * x_) % p
    return x, h


def compare(x, h, l, f1, f2, p):
    return (h[f1 + l] + h[f2]*x[l]) % p == (h[f2 + l] + h[f1]*x[l]) % p


def zfunc(s):
    n = len(s)
    res = [0] * n
    resx, resh = hashing(s)
    for i in range(1, n):
        l, r = 0, n - i
        while l <= r:
            m = (l + r) // 2
            b = compare(resx, resh, m, 0, i, 10**9 + 7)
            if b:
                res[i] = m
                l = m + 1
            else:
                r = m - 1
    return res
print(*zfunc(input()))
