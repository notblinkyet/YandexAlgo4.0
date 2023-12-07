def masnacer_odd(s):
    s = "$" + s + "^"
    n = len(s)
    res = [0] * n
    l, r = 0, 0
    for i in range(1, n - 1):
        res[i] = max(0, min(r - i, res[l + (r - i)]))
        while s[i - res[i]] == s[i + res[i]]:
            res[i] += 1
        if i + res[i] > r:
            l, r = i - res[i], i + res[i]
    return res[1:-1]


def manacer(s):
    res = masnacer_odd("#" + "#".join(s) + "#")[1:-1]
    return sum([x // 2 for x in res[::2]]) + sum([x // 2 for x in res[1::2]])

print(manacer(input()))
