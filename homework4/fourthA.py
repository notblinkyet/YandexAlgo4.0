N = int(input())
a = [i for i in range(N+1)]


def foo(l, s):
    if len(l) == 1:
        print(*s, sep="")
        pass
    for k in range(1, len(l)):
        foo(l[:k] + l[k+1:], s + l[k:k+1])

foo(a, [])
