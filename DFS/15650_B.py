N, M = map(int, input().split())
visited = [0] * (N+1)
lst = [str(st) for st in range(1, N+1)]


# n :depth, st: string
def dfs(n, st):
    if n == M:
        print(st)
        return
    for i in range(n, N):
        if not visited[i]:
            visited[i] = 1
            if not st:
                dfs(n+1, lst[i])
            else:
                dfs(n+1, st + ' ' + lst[i])
            visited[i] = 0


dfs(0, '')