import heapq

N = int(input())
d, v = list(map(int, input().split()))
R = int(input())
adjli = [[] for _ in range(N+1)]
for i in range(R):
    a, t1, b, t2 = list(map(int, input().split()))
    adjli[a].append((t1, b, t2))
visit, dist1 = [False] * (N + 1), [(float("inf"), i) for i in range(N+1)]
dist = [float("inf")] * (N+1)
dist[d] = 0
dist1[d] = (0, d)
heapq.heapify(dist1)
for i in range(1, N+1):
    t1, a = heapq.heappop(dist1)
    while dist1 and visit[a] and adjli[i] and t1 > dist[i]:
        t1, a = heapq.heappop(dist1)
    for t, b, t2 in adjli[a]:
        if t1 <= t and t2 < dist[b]:
            dist[b] = t2
            heapq.heappush(dist1, (t2, b))
    visit[a] = True
if dist[v] != float("inf"):
    print(dist[v])
else:
    print(-1)
