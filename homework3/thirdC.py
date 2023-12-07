import heapq

N, K = tuple(map(int, input().split()))
adjli = [[] for _ in range(N+1)]
for i in range(K):
    a, b, l = list(map(int, input().split()))
    adjli[a].append((l, b))
    adjli[b].append((l, a))
S, F = list(map(int, input().split()))
visit, dist1 = [False] * (N + 1), [(float("inf"), i) for i in range(N+1)]
dist = [float("inf")] * (N+1)
dist[S] = 0
dist1[S] = (0, S)
heapq.heapify(dist1)
for i in range(1, N+1):
    m, minid = heapq.heappop(dist1)
    while dist and visit[minid]:
        m, minid = heapq.heappop(dist1)
    for l, b in adjli[minid]:
        if m + l < dist[b]:
            dist[b] = m + l
            heapq.heappush(dist1, (m+l, b))
    visit[minid] = True
if dist[F] != float("inf"):
    print(dist[F])
else:
    print(-1)
