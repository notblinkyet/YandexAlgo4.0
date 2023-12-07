N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


def main(graph, N):
    global best

    best = 0

    minof = [None] * N
    if N == 1:
        return 0
    for i in range(N):
        mincur = float("inf")
        for j in range(N):
            if graph[i][j] < mincur and graph[i][j] != 0:
                mincur = graph[i][j]
        minof[i] = mincur

    minall = sum(minof)

    vis = [False] * N
    now = 0
    for i in range(N):
        mindis = float("inf")
        next_ = -1
        for vertex, edge in enumerate(graph[now]):
            if i < N - 1:
                if edge != 0 and edge < mindis and not vis[vertex] and vertex != 0:
                    next_ = vertex
                    mindis = edge
            else:
                if edge != 0 and edge < mindis and not vis[vertex]:
                    next_ = vertex
                    mindis = edge
        if next_ == -1:
            return float("inf")
        best += mindis
        now = next_
        vis[now] = True

    def foo(cur, count, dist, vis, minost):
        global best

        if count == N:
            if best > dist and cur == 0:
                best = dist
            return
        if best <= dist + minost:
            return
        for vertex, edge in enumerate(graph[cur]):
            if not vis[vertex] and dist + edge < best and edge != 0:
                vis[vertex] = True
                foo(vertex, count+1, dist+edge, vis.copy(), minost - minof[vertex])
                vis[vertex] = False

    vis = [False] * N

    foo(0, 0, 0, vis, minall)
    return best

best = main(graph, N)
if best == float("inf"):
    print(-1)
else:
    print(best)
