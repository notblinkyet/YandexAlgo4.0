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


def base(s):
    n = len(s)
    resx, resh = hashing(s)
    for i in range(1, n):
        res = compare(resx, resh, n - i, 0, i, 10**9 + 7)
        if res:
            return i
    return len(s)

print(base(input()))
