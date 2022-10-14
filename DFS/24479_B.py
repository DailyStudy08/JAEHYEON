import sys
sys.setrecursionlimit(10**9)

def dfs(cnt, n):
    if cnt == N+1:
        return

    visited[n] = cnt
    adj_lst[n].sort()
    for node in adj_lst[n]:
        if not visited[node]:
            dfs(cnt + 1, node)


N, M, R = map(int, input().split())
adj_lst = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    adj_lst[u].append(v)
    adj_lst[v].append(u)


dfs(1, R)

for i in range(1, len(visited)):
    print(visited[i])
