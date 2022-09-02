N, M, V = map(int, input().split())

#방문처리 배열 생성
visited = [False] * (N + 1)

# 인접리스트 생성
adj_lst = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

# 각 노드별 오름차순 정렬
for ad in adj_lst:
    ad.sort()

# bfs
def bfs():
    Q = [V]
    visited[V] = True
    while Q:
        w = Q.pop(0)
        print(w)
        
        for node in adj_lst[w]:
            if not visited[node]:
                visited[node] = True
                Q.append(node)

bfs()

