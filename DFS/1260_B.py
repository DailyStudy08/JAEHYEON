
N, M, V = map(int, input().split())     # N : 정점 개수, M : 간선 개수, V : 탐색 시작 정점 번호
adj_lst = [[] for _ in range(N + 1)]    # 인접리스트 생성

for _ in range(M):                      # 간선이 연결하는 두 정점의 번호
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

visited_1 = [False] * (N+1)
visited_2 = [False] * (N+1)

def dfs(v):
    visited_1[v] = True
    print(v, end = ' ')
    for node in sorted(adj_lst[v]):
        if not visited_1[node]:
            dfs(node)

def bfs(v):
    queue = [v]
    visited_2[v] = True
    while queue:
        v = queue.pop(0)
        print(v, end= ' ')
        for node in sorted(adj_lst[v]):
            if not visited_2[node]:
                queue.append(node)
                visited_2[node] = True


dfs(V)
print()
bfs(V)
print()