N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

best = 0
part = []


def foo(ver1, ver2, count, dl):
    global best, part
    if count == N:
        if best < dl:
            best = dl
            part = (ver1, ver2)
        return

    dl1, dl2 = 0, 0
    for v in ver1:
        dl1 += graph[v][count]
    foo(ver1, ver2 | set([count]), count+1, dl + dl1)
    for v in ver2:
        dl2 += graph[v][count]
    foo(ver1 | set([count]), ver2, count+1, dl + dl2)

foo(set([0]), set(), 1, 0)
print(best)
ver1, ver2 = part
for i in range(N):
    if i in ver1:
        print(2, end=" ")
    else:
        print(1, end=" ")
