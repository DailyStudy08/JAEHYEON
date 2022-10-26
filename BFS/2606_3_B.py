N = int(input())
M = int(input())
adj_lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

visited = [0] * (N + 1)
cnt = 0
Q = [1]
visited[1] = 1

while Q:
    w = Q.pop(0)
    for node in adj_lst[w]:
        if visited[node] == 0:
            visited[node] = 1
            Q.append(node)
            cnt += 1

print(cnt)