from sys import stdin

# N, M = map(int, input().split())
N, M = map(int, stdin.readline().split())
edge = [[num] for num in range(0, N + 1)]
visited = [0] * (N+1)
visited[0] = 1

for _ in range(M):
    u, v = map(int, stdin.readline().split())
    edge[u].append(v)
    edge[v].append(u)
cnt = 0
# print(edge)


def bfs():
    global cnt
    for v in range(len(edge)):
        Q = []
        if edge[v] and not visited[v]:
            Q.append(edge[v])
            visited[v] = 1
            cnt += 1

            while Q:
                w = Q.pop(0)
                for node in w:
                    if not visited[node]:
                        visited[node] = 1
                        Q.append(edge[node])
    #
    # for V in enumerate(edge):
    #     Q = []
    #     if V[1] and not visited[V[0]]:
    #         Q.append(V[1])
    #         visited[V[0]] = 1
    #         cnt += 1
    #
    #         while Q:
    #             w = Q.pop(0)
    #             for node in w:
    #                 if not visited[node]:
    #                     visited[node] = 1
    #                     Q.append(edge[node])


bfs()
print(cnt)