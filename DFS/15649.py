def dfs(n, num):
    if n == M:
        print(num[1:])
    L = len(lst)
    for i in range(L):
        if not visited[i]:
            visited[i] = 1
            new_num = lst[i]
            dfs(n+1, num +' '+new_num)
            visited[i] = 0


N, M = map(int, input().split())
visited = [0]*N
lst = list(map(str, range(1,N+1)))
dfs(0, '')