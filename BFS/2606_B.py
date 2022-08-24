N = int(input())    # 컴퓨터 대수
pair = int(input())

adj_lst = [[] for _ in range(N + 1)]
for _ in range(pair):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)


Q = []
Q.append(1)
visited = [False] * (N + 1)

while Q:
    w = Q.pop(0)
    for node in adj_lst[w]:
        if not visited[node]:
            visited[node] = True
            Q.append(node)

cnt = -1
for node in visited:
    if node:
        cnt +=1

print(cnt)
