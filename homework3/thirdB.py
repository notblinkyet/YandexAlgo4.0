N, S, F = tuple(map(int, input().split()))
adjli = [[-1]] * (N+1)
for i in range(1, N+1):
    a = list(map(int, input().split()))
    adjli[i] = [-1] + a
visit, dist = [False] * (N + 1), [float("inf")] * (N + 1)
prev = [-1] * (N+1)
dist[S] = 0
for i in range(1, N+1):
    mindis = float("inf")
    minid = -1
    for j in range(1, N+1):
        if not visit[j] and dist[j] < mindis:
            mindis = dist[j]
            minid = j
    for k in range(1, N+1):
        if adjli[minid][k] != -1 and dist[minid] + adjli[minid][k] < dist[k]:
            dist[k] = dist[minid] + adjli[minid][k]
            prev[k] = minid
    visit[minid] = True
res = []
while prev[F] != -1:
    res.append(F)
    F = prev[F]
if res:
    print(S, *res[::-1])
elif F == S:
    print(F)
else:
    print(-1)
