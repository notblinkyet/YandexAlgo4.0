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


def compare(x1, h1, x2, h2, l, f1, f2, p):
    return (h1[f1 + l] + h2[f2]*x2[l]) % p == (h2[f2 + l] + h1[f1]*x1[l]) % p


def cubes(s):
    n = len(s)
    res = []
    invertx, inverth = hashing(s[::-1])
    x, h = hashing(s)
    if n % 2:
        k = n // 2 + 1
    else:
        k = n // 2
    for i in range(k, n):
        if compare(invertx, inverth, x, h, n - i, i, n - i, 10 ** 9 + 7):
            res.append(i)
    res.append(n)
    return res


l = list(map(int, input().split()))
cub = "".join(map(lambda x: chr(int(x)), input().split()))
print(*cubes(cub))
