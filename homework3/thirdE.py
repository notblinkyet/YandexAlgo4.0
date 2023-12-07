#Импортирую и считываю


import collections
from queue import LifoQueue
N = int(input())
wait_speed = [0 for _ in range(N+1)]
for i in range(1, N+1):
    wait_speed[i] = tuple(map(int, input().split()))


#Начальный граф


dorogi = collections.defaultdict(list)
for _ in range(1, N):
    a, b, s = tuple(map(int, input().split()))
    dorogi[a].append((b, s))
    dorogi[b].append((a, s))

#Создание графа времени от каждой вершины, но сразу развернутый

graph = [[0] * (N+1) for _ in range(N+1)]
for v in range(2, N+1):
    times = [0] * (N+1)
    times[v] = wait_speed[v][0]
    visited = [0] * (N+1)
    visited[v] = 1
    q = collections.deque()
    q.append(v)
    while q:
        cur = q.popleft()
        for neib, s in dorogi[cur]:
            if visited[neib] != 1:
                visited[neib] = 1
                times[neib] = times[cur] + s / wait_speed[v][1]
                graph[neib][v] = times[neib]
                q.append(neib)

#Алгоритм дейстры

max_time = -1
times = [2 * 10**8] * (N + 1)
times[1] = 0
visited = [0] * (N+1)
prevs = [-1] * (N+1)
res_ind = -1
for i in range(1, N+1):
    mindis = 2 * 10**8
    minid = -1
    for j in range(1, N + 1):
        if visited[j] == 0 and times[j] < mindis:
            mindis = times[j]
            minid = j
    for k in range(1, N+1):
        if times[minid] + graph[minid][k] < times[k]:
            times[k] = times[minid] + graph[minid][k]
            prevs[k] = minid
    visited[minid] = 1

#Нахождение самого длинного пути


for i in range(1, N+1):
    if times[i] > max_time:
        res_ind = i
        max_time = times[i]


#Вывод


print(max_time)
while prevs[res_ind] != -1:
    print(res_ind, end=" ")
    res_ind = prevs[res_ind]

print(res_ind)
